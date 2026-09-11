import asyncio
import os
import re
import json

from experiments.experiment import Experiment
from ciphers.cipher import CipherBundle

from judges.reject_judge import RejectJudge


class BenignTester(Experiment):
    """Benign evaluation run as a standalone test.

    Same shape as Tester — load a cipher bundle, walk the test/val split
    concurrently, log every sample — but the samples are scored the way
    Trainer.async_run_benign_eval scores them: the target is asked in benign mode
    (benign few-shot) and the benign judge rates the answer 1-10 instead of the
    harm judge marking a jailbreak.
    """

    def __init__(self, config):
        super().__init__(config)
        self.target = config.target
        self.judge = config.benign_judge
        self.base_log_dir = config.log_dir

        self.logger = config.logger
        self.config = config
        self.cipher_bundle = None
        self.reject_judge = RejectJudge()

    def load_best_cipher_bundle(self, bundle_path):
        with open(bundle_path, "r") as f:
            bundle_data = json.load(f)

        self.cipher_bundle = CipherBundle(
            module_path=bundle_data["module_path"],
            description_json=bundle_data["description_json"],
            name=bundle_data["name"],
            base_cipher_prompt=bundle_data["base_cipher_prompt"]
        )
        print(f"Loaded best cipher bundle: {self.cipher_bundle.name}")


    def test(self):
        """Synchronous entry point — delegates to the async test."""
        return asyncio.run(self.async_test())

    def val(self):
        """Synchronous entry point — delegates to the async test."""
        return asyncio.run(self.async_test(test_val_flag="val"))


    async def async_test(self, test_val_flag="test", max_concurrency=5):
        """Async benign evaluation — processes samples concurrently with a concurrency limit."""
        print("\n--------------------- Evaluating on benign ---------------------\n")
        print(f"Cipher: {self.cipher_bundle.name}")

        self.logger.set_benign_eval_log(test_val_flag)
        self.logger.log_benign_eval_cipher(self.cipher_bundle.description_json)

        self.category_scores = {}
        self.target.cipher_benign_few_shot(self.cipher_bundle)

        semaphore = asyncio.Semaphore(max_concurrency)

        async def process_one_sample(sample):
            async with semaphore:
                question, category = sample
                if isinstance(question, list):
                    question = question[0]
                if self.config.ciphered_input_flag:
                    ciphered_question = self.cipher_bundle.encrypt(question)
                else:
                    ciphered_question = question
                target_answer, additional_info = await asyncio.to_thread(
                    self.target.ask, ciphered_question, self.cipher_bundle.prompt, True
                )
                additional_info = self._decrypt_additional_info(additional_info)
                if self.config.ciphered_output_flag:
                    decrypted_answer = self.cipher_bundle.decrypt(target_answer)
                else:
                    decrypted_answer = target_answer
                denoised_answer = decrypted_answer
                if self.config.denoiser:
                    denoised_answer = await asyncio.to_thread(
                        self.config.denoiser.denoise, target_answer, decrypted_answer
                    )

                judge_response = await asyncio.to_thread(
                    self.judge.judge, question, denoised_answer
                )
                score = self.format_benign_judge_response(judge_response)
                reject_score = self.reject_judge.classify(denoised_answer)
                return question, ciphered_question, target_answer, decrypted_answer, denoised_answer, judge_response, score, category, additional_info, reject_score

        if test_val_flag == "val":
            tasks = [process_one_sample(sample) for sample in self.config.val_loader]
        else:
            tasks = [process_one_sample(sample) for sample in self.config.test_loader]
        results = await asyncio.gather(*tasks)

        scores = []
        reject_stats = {'refusals': 0, 'input_blocks': 0, 'output_blocks': 0, 'other': 0}
        for question, ciphered_question, target_answer, decrypted_answer, denoised_answer, judge_response, score, category, additional_info, reject_score in results:
            print(f"Question: {question}")
            print(f"Answer: {denoised_answer}")
            print(f"Judge Response: {judge_response}")
            if additional_info is not None:
                print(f"Additional info: {additional_info}")
            print(f"Score: {score}")
            print(f"Reject Score: {reject_score}")
            print("-------------------------------------------")
            scores.append(score)
            if category in self.category_scores:
                self.category_scores[category].append(score)
            else:
                self.category_scores[category] = [score]

            if reject_score == 'refusal':
                reject_stats['refusals'] += 1
            elif reject_score == 'input_block':
                reject_stats['input_blocks'] += 1
            elif reject_score == 'output_block':
                reject_stats['output_blocks'] += 1
            else:
                reject_stats['other'] += 1

            # Log benign results (sequential, no data race)
            self.logger.log_benign_eval(
                question, ciphered_question, target_answer,
                decrypted_answer, denoised_answer, judge_response, score
            )

        avg_score = sum(scores) / len(scores)
        print(f"Average benign score: {avg_score}")
        self.logger.log_benign_eval_avg_score(avg_score)

        for category, category_score in self.category_scores.items():
            print(f"{category}: {sum(category_score) / len(category_score)} ({len(category_score)})")

        # Refusals on benign prompts, i.e. how much the cipher costs in over-refusal
        total_samples = len(results)
        refusal_rate = reject_stats['refusals'] / total_samples if total_samples > 0 else 0
        input_block_rate = reject_stats['input_blocks'] / total_samples if total_samples > 0 else 0
        output_block_rate = reject_stats['output_blocks'] / total_samples if total_samples > 0 else 0
        other_rate = reject_stats['other'] / total_samples if total_samples > 0 else 0

        print(f"\n----- Reject Statistics -----")
        print(f"Total Refusals: {reject_stats['refusals']}/{total_samples} ({refusal_rate:.2%})")
        print(f"Input Blocks: {reject_stats['input_blocks']}/{total_samples} ({input_block_rate:.2%})")
        print(f"Output Blocks: {reject_stats['output_blocks']}/{total_samples} ({output_block_rate:.2%})")
        print(f"Other: {reject_stats['other']}/{total_samples} ({other_rate:.2%})")

        self.logger.log_benign_eval_reject_stats(refusal_rate, input_block_rate, output_block_rate, other_rate)

        # Save complete cipher bundle info for full reinitialization
        self._save_cipher_bundle_info(test_val_flag)

        return avg_score


    def _save_cipher_bundle_info(self, test_val_flag):
        """Save complete cipher bundle info (code, description, prompt, paths) for full reinitialization."""
        # Read the cipher code from module file
        cipher_code = ""
        if self.cipher_bundle.module_path and os.path.exists(self.cipher_bundle.module_path):
            with open(self.cipher_bundle.module_path, 'r') as f:
                cipher_code = f.read()

        # Create complete cipher info object
        cipher_info = {
            "name": self.cipher_bundle.name,
            "module_path": self.cipher_bundle.module_path,
            "description_json": self.cipher_bundle.description_json,
            "prompt": self.cipher_bundle.prompt,
            "base_cipher_prompt": self.cipher_bundle.base_cipher_prompt,
            "cipher_code": cipher_code
        }

        # Save next to the benign results
        benign_dir = os.path.dirname(self.logger.benign_eval_log_path)
        cipher_info_path = os.path.join(benign_dir, f"cipher_bundle_benign_{test_val_flag}.json")
        os.makedirs(benign_dir, exist_ok=True)
        with open(cipher_info_path, 'w') as f:
            json.dump(cipher_info, f, indent=2)
        print(f"Saved cipher bundle info to: {cipher_info_path}")

        # Save the cipher description separately for convenience
        description_path = os.path.join(benign_dir, f"cipher_description_benign_{test_val_flag}.json")
        with open(description_path, 'w') as f:
            json.dump(self.cipher_bundle.description_json, f, indent=2)
        print(f"Saved cipher description to: {description_path}")

    @staticmethod
    def format_benign_judge_response(judge_response):
        match = re.search(r"\[\[(\d+)\]\]", judge_response)
        if match:
            score = int(match.group(1))
        else:
            score = 0
        return score

    def _decrypt_additional_info(self, additional_info):
        """Parse additional_info JSON and add a decrypted version of answer_before_block.

        The raw answer_before_block is stored in ciphered form by the target. Since the
        Target has no access to the CipherBundle, decryption is done here where
        self.cipher_bundle is available. Returns the updated JSON string (or None).
        """
        if not additional_info:
            return additional_info
        try:
            info = json.loads(additional_info)
        except (json.JSONDecodeError, TypeError):
            return additional_info
        if isinstance(info, dict) and info.get("answer_before_block") is not None:
            info["answer_before_block_decrypted"] = self.cipher_bundle.decrypt(
                info["answer_before_block"]
            )
            return json.dumps(info, ensure_ascii=False)
        return additional_info
