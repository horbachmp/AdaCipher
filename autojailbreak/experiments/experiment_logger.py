import os
import json
import yaml
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict


from utils.json_utils import extract_json

ATTACK_LOG_FILE = "attack_log.jsonl"
JUDGE_LOG_FILE = "judge_log.jsonl"
ATTACK_STRATEGY_LOG_FILE = "attack_strategy_log.jsonl"

STRATEGIST_LOG_FILE = "strategist_log.jsonl"
VERIFICATION_LOG_FILE = "verification_log.jsonl"
CONFIG_FILE = "config.yaml"
EXP_SUMMARY_FILE = "experiment_summary.txt"
TRIAL_SUMMARY_FILE = "trial_summary.txt"
TEST_SUMMARY_FILE = "test_summary.txt"
ASR_FILE = "test_asr.txt"
REJECT_STATS_FILE = "test_reject_stats.txt"
CIPHER_INFO_FILE = "cipher_info.txt"
TRIAL_HISTORY_FILE = "trial_history.json"
CIPHER_BUNDLE_FILE = "cipher_bundle.json"

TRIAL_FOLDER_NAME = "attack_trial_{trial_num}"
ITER_FOLDER_NAME = "iter_{iter_num}"

TEST_FOLDER_NAME = "tests"
TEST_LOG_FILE = "test_log.jsonl"

VAL_FOLDER_NAME = "val"
VAL_LOG_FILE = "val_log.jsonl"

BENIGN_EVAL_LOG_FILE = "benign_eval_log.jsonl"
BENIGN_FOLDER_NAME = "benign"


class ExperimentLogger:
    def __init__(self, log_dir, config_dict=None):
        self.log_dir = log_dir
        self.curr_iter = 0
        self.curr_trial = 0
        self.is_static = config_dict and config_dict.get('exp_type') in ['static']

        if os.path.exists(log_dir):
            raise FileExistsError(f"Log directory {log_dir} already exists. Please remove it or choose a different log path.")

        os.makedirs(log_dir, exist_ok=False)

        if config_dict:
            with open(os.path.join(log_dir, CONFIG_FILE), "w") as f:
                yaml.dump(config_dict, f)

        self.test_log_path = os.path.join(self.log_dir, TEST_FOLDER_NAME, TEST_LOG_FILE)
        os.makedirs(os.path.dirname(self.test_log_path), exist_ok=False)

        # Only create val folder for dynamic experiments
        if not self.is_static:
            self.val_log_path = os.path.join(self.log_dir, VAL_FOLDER_NAME, VAL_LOG_FILE)
            os.makedirs(os.path.dirname(self.val_log_path), exist_ok=False)
        else:
            self.val_log_path = None

        self.benign_eval_log_path = None

    def set_test_log_for_current_trial(self):
        """Redirect test logging to a per-trial subdirectory inside tests/.
        Structure: tests/trial_{trial_num}/test_log.jsonl
        """
        self.test_log_path = os.path.join(
            self.log_dir, TEST_FOLDER_NAME,
            f"trial_{self.curr_trial}",
            TEST_LOG_FILE
        )
        os.makedirs(os.path.dirname(self.test_log_path), exist_ok=True)

    def set_val_log_for_current_trial(self):
        """Redirect val logging to a per-trial subdirectory inside val/.
        Structure: val/trial_{trial_num}/val_log.jsonl
        Only called for dynamic experiments.
        """
        if self.is_static:
            self.val_log_path = None
            return

        self.val_log_path = os.path.join(
            self.log_dir, VAL_FOLDER_NAME,
            f"trial_{self.curr_trial}",
            VAL_LOG_FILE
        )
        os.makedirs(os.path.dirname(self.val_log_path), exist_ok=True)

        


    def set_iteration(self, iteration_num):
        """Set the current iteration for logging. Logs will be written to iter_{iteration_num}/ subdirectory."""
        self.curr_iter = iteration_num
        self.curr_iter_dir = os.path.join(self.curr_trial_dir, ITER_FOLDER_NAME.format(iter_num=self.curr_iter))
        self.attack_log_path = os.path.join(self.curr_iter_dir, ATTACK_LOG_FILE)
        self.judge_log_path = os.path.join(self.curr_iter_dir, JUDGE_LOG_FILE)
        self.benign_eval_log_path = os.path.join(self.curr_iter_dir, BENIGN_EVAL_LOG_FILE)
        os.makedirs(self.curr_iter_dir, exist_ok=False)


    def set_trial(self, trial_num):
        """Set the current trial for logging. Logs will be written to attack_trial_{trial_num}/ subdirectory.

        Automatically sets up per-trial logging directories for:
          - Test: tests/trial_{trial_num}/test_log.jsonl
          - Val: val/trial_{trial_num}/val_log.jsonl

        When moving to a new trial (trial_num > 0), automatically creates a summary
        of the previous trial via create_trial_summary().
        """
        # Summarize the previous trial before switching
        if trial_num > 0 and hasattr(self, 'curr_trial_dir') and os.path.isdir(self.curr_trial_dir):
            self.create_trial_summary()

        self.curr_trial = trial_num
        self.curr_trial_dir = os.path.join(self.log_dir, TRIAL_FOLDER_NAME.format(trial_num=self.curr_trial))
        os.makedirs(self.curr_trial_dir, exist_ok=False)

        # Automatically set up per-trial test and val logging directories
        self.set_test_log_for_current_trial()
        self.set_val_log_for_current_trial()


    def _get_log_path(self, log_file):
        """Get the full path for a log file, considering current iteration."""
        return os.path.join(self.curr_iter_dir, log_file)

    def log_attack(self, question, ciphered_question, target_answer, decrypted_answer, denoised_answer, category=None, judge_response=None, additional_info=None, original_question=None, reject_score=None):
        """Log question, ciphered question, raw answer, decrypted answer, denoised answer, category, and judge response"""
        entry = {
            "original_question": original_question,
            "question": question,
            "ciphered_question": ciphered_question,
            "target_answer": target_answer,
            "decrypted_answer": decrypted_answer,
            "denoised_answer": denoised_answer,
            "category": category,
            "judge_response": judge_response,
            "additional_info": additional_info,
            "reject_score": reject_score
        }
        log_path = self._get_log_path(ATTACK_LOG_FILE)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def log_judge_summary(self, summarised_response, jailbreak_success):
        """Log summarised judge responses"""
        entry = {
            "summarised_response": summarised_response,
            "jailbreak_success": jailbreak_success
        }
        log_path = self._get_log_path(JUDGE_LOG_FILE)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    
    def log_test_cipher(self, best_cipher):
        entry = {
            "best_cipher": best_cipher
        }
        with open(self.test_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    
    def log_test(self, question, ciphered_question, target_answer, decrypted_answer, denoised_answer, judge_response, score, category, additional_info=None, original_question=None, reject_score=None):
        """Log test results including question, answers, judge response and score"""
        entry = {
            "original_question": original_question,
            "question": question,
            "ciphered_question": ciphered_question,
            "target_answer": target_answer,
            "decrypted_answer": decrypted_answer,
            "denoised_answer": denoised_answer,
            "judge_response": judge_response,
            "score": score,
            "category": category,
            "additional_info": additional_info,
            "reject_score": reject_score
        }

        with open(self.test_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def log_attack_strategy_transform(self, original_question, transformed_question, category=None):
        """Log prompt transformation by attack strategy (before and after)"""
        entry = {
            "original_question": original_question,
            "transformed_question": transformed_question,
            "category": category
        }
        # Save to test log directory
        log_path = os.path.join(os.path.dirname(self.test_log_path), ATTACK_STRATEGY_LOG_FILE)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def log_strategist_response(self, cipher_json):
        """Log strategist response with generated cipher"""
        entry = {
            "cipher": cipher_json
        }
        log_path = self._get_log_path(STRATEGIST_LOG_FILE)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def log_verification_feedback(self, verification_feedback, verdict):
        """Log cipher verification feedback for current iteration"""
        entry = {
            "iteration": self.curr_iter,
            "verdict": verdict,
            "feedback": verification_feedback
        }
        log_path = self._get_log_path(VERIFICATION_LOG_FILE)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


   

    def log_val(self, question, ciphered_question, target_answer, decrypted_answer, denoised_answer, judge_response, score, category, additional_info=None, original_question=None, reject_score=None):
        """Log val results including question, answers, judge response and score. Skip for static experiments."""
        if self.is_static or self.val_log_path is None:
            return

        entry = {
            "original_question": original_question,
            "question": question,
            "ciphered_question": ciphered_question,
            "target_answer": target_answer,
            "decrypted_answer": decrypted_answer,
            "denoised_answer": denoised_answer,
            "judge_response": judge_response,
            "score": score,
            "category": category,
            "additional_info": additional_info,
            "reject_score": reject_score
        }

        with open(self.val_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


    def log_val_cipher(self, cipher_bundle):
        """Log val cipher bundle with all necessary info to recreate it. Skip for static experiments."""
        if self.is_static or self.val_log_path is None:
            return

        entry = {
            "cipher_bundle": {
                "name": cipher_bundle.name,
                "module_path": cipher_bundle.module_path,
                "description_json": cipher_bundle.description_json,
                "base_cipher_prompt": cipher_bundle.base_cipher_prompt,
                "prompt": cipher_bundle.prompt
            }
        }
        with open(self.val_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

        # Also save cipher bundle as separate JSON file in val directory
        val_dir = os.path.dirname(self.val_log_path)
        bundle_file = os.path.join(val_dir, "cipher_bundle.json")
        with open(bundle_file, "w", encoding="utf-8") as f:
            json.dump(entry["cipher_bundle"], f, indent=2, ensure_ascii=False)
        print(f"[Val] Cipher bundle saved to {bundle_file}")

    
    def log_val_avg_score(self, score):
        """Log val results. Skip for static experiments."""
        if self.is_static or self.val_log_path is None:
            return

        entry = {
            "avg_score": score
        }

        with open(self.val_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


    def set_benign_eval_log(self, test_val_flag="test"):
        """Point benign-eval logging at benign/{test|val}/benign_eval_log.jsonl.

        Used by standalone benign runs (see BenignTester), which have no trial or
        iteration directories to write into.
        """
        self.benign_eval_log_path = os.path.join(
            self.log_dir, BENIGN_FOLDER_NAME, test_val_flag, BENIGN_EVAL_LOG_FILE
        )
        os.makedirs(os.path.dirname(self.benign_eval_log_path), exist_ok=True)
        return self.benign_eval_log_path


    def log_benign_eval_cipher(self, cipher_json):
        """Log val cipher"""
        entry = {
            "cipher": cipher_json
        }
        with open(self.benign_eval_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


    def log_benign_eval(self, question, ciphered_question, target_answer, decrypted_answer, denoised_answer, judge_response, score):
        """Log val results including question, answers, judge response and score"""
        entry = {
            "question": question,
            "ciphered_question": ciphered_question,
            "target_answer": target_answer,
            "decrypted_answer": decrypted_answer,
            "denoised_answer": denoised_answer,
            "judge_response": judge_response,
            "score": score
        }
        
        with open(self.benign_eval_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


    def log_benign_eval_avg_score(self, score):
        """Log eval results """
        entry = {
            "avg_score": score
        }

        with open(self.benign_eval_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


    def log_benign_eval_reject_stats(self, refusal_pct, input_block_pct, output_block_pct, other_pct):
        """Log how often the target refused or was blocked on benign prompts (over-refusal)."""
        entry = {
            "refusal_rate": refusal_pct,
            "input_block_rate": input_block_pct,
            "output_block_rate": output_block_pct,
            "other_rate": other_pct
        }

        with open(self.benign_eval_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")



    def log_asr_score(self, score, test_val_flag="test"):
        asr_path = os.path.join(os.path.dirname(self.test_log_path), ASR_FILE)
        if test_val_flag == "val":
            if self.is_static or self.val_log_path is None:
                return
            asr_path = os.path.join(os.path.dirname(self.val_log_path), ASR_FILE)
        with open(asr_path, "a") as f:
            f.write(f"General ASR score: {str(score)}\n\n")


    def log_asr_per_category(self, dict_category_score, test_val_flag="test"):
        asr_path = os.path.join(os.path.dirname(self.test_log_path), ASR_FILE)
        if test_val_flag == "val":
            if self.is_static or self.val_log_path is None:
                return
            asr_path = os.path.join(os.path.dirname(self.val_log_path), ASR_FILE)
        with open(asr_path, "a") as f:
            for category, score in dict_category_score.items():
                f.write(f"{category}: {score}\n")

    def log_reject_stats(self, refusal_pct, input_block_pct, output_block_pct, other_pct, test_val_flag="test"):
        """Log overall reject statistics (percentages)"""
        reject_path = os.path.join(os.path.dirname(self.test_log_path), REJECT_STATS_FILE)
        if test_val_flag == "val":
            reject_path = os.path.join(os.path.dirname(self.val_log_path), REJECT_STATS_FILE)
        with open(reject_path, "a") as f:
            f.write(f"General Reject Statistics:\n")
            f.write(f"  Refusals: {refusal_pct:.2%}\n")
            f.write(f"  Input Blocks: {input_block_pct:.2%}\n")
            f.write(f"  Output Blocks: {output_block_pct:.2%}\n")
            f.write(f"  Other: {other_pct:.2%}\n\n")

    def log_reject_stats_per_category(self, category_reject_stats, test_val_flag="test"):
        """Log per-category reject statistics.
        category_reject_stats: dict[category] -> (refusal_pct, input_block_pct, output_block_pct, other_pct, total_count)
        """
        reject_path = os.path.join(os.path.dirname(self.test_log_path), REJECT_STATS_FILE)
        if test_val_flag == "val":
            reject_path = os.path.join(os.path.dirname(self.val_log_path), REJECT_STATS_FILE)
        with open(reject_path, "a") as f:
            for category, stats in category_reject_stats.items():
                refusal_pct, input_block_pct, output_block_pct, other_pct, total_count = stats
                f.write(f"{category} (n={total_count}):\n")
                f.write(f"  Refusals: {refusal_pct:.2%}\n")
                f.write(f"  Input Blocks: {input_block_pct:.2%}\n")
                f.write(f"  Output Blocks: {output_block_pct:.2%}\n")
                f.write(f"  Other: {other_pct:.2%}\n")

    def log_cipher_info(self, cipher_json, cipher_prompt):
        """Log cipher_json and cipher_prompt to a txt file in current trial directory"""
        cipher_info_path = os.path.join(self.curr_trial_dir, CIPHER_INFO_FILE)
        with open(cipher_info_path, "a", encoding="utf-8") as f:
            f.write(f"===== Trial: {self.curr_trial} =====\n")
            f.write(f"Cipher JSON:\n{json.dumps(cipher_json, indent=2, ensure_ascii=False)}\n\n")
            f.write(f"Cipher Prompt:\n{cipher_prompt}\n")
            f.write("=" * 50 + "\n\n")

    # ──────────────────────────────────────────────
    # Per-trial history (machine-readable, for resuming a crashed run)
    # ──────────────────────────────────────────────

    def log_trial_history(self, trial_state, cipher_bundle=None):
        """Write the full state of the current trial to trial_history.json in the trial dir.

        This is the machine-readable counterpart of trial_summary.txt: ``trial_state``
        is the trainer's own snapshot of everything needed to restart the experiment
        from the trial that follows this one (see ``Trainer.snapshot_state``).

        The cipher bundle used in this trial is additionally saved as cipher_bundle.json
        next to it, so it can be reused directly via the 'cipher_bundle_path' config field.
        """
        trial_dir = self.curr_trial_dir
        os.makedirs(trial_dir, exist_ok=True)

        if cipher_bundle is not None:
            cipher_bundle.save(os.path.join(trial_dir, CIPHER_BUNDLE_FILE))

        entry = {
            "trial": self.curr_trial,
            "trial_dir": trial_dir,
            "log_dir": self.log_dir,
            "cipher_bundle_path": os.path.join(trial_dir, CIPHER_BUNDLE_FILE) if cipher_bundle is not None else None,
        }
        entry.update(trial_state or {})

        history_path = os.path.join(trial_dir, TRIAL_HISTORY_FILE)
        with open(history_path, "w", encoding="utf-8") as f:
            json.dump(entry, f, indent=2, ensure_ascii=False)
        print(f"[Trial History] Saved {history_path}")

    @staticmethod
    def format_category_asr(category_asr):
        """Normalise {category: (asr, count)} into a JSON-friendly dict."""
        if not category_asr:
            return {}
        formatted = {}
        for category, value in category_asr.items():
            if isinstance(value, (tuple, list)) and len(value) == 2:
                formatted[category] = {"asr": value[0], "count": value[1]}
            else:
                formatted[category] = {"asr": value, "count": None}
        return formatted

    @staticmethod
    def read_trial_history(log_dir):
        """Read all trial_history.json files of a run, ordered by trial number.

        Use this to resume an experiment that crashed: the last entry holds the
        cipher bundle, the judge feedback and the strategist memory to continue from.
        """
        history = []
        if not os.path.isdir(log_dir):
            return history

        for name in os.listdir(log_dir):
            history_path = os.path.join(log_dir, name, TRIAL_HISTORY_FILE)
            if name.startswith("attack_trial_") and os.path.isfile(history_path):
                with open(history_path, "r", encoding="utf-8") as f:
                    history.append(json.load(f))

        history.sort(key=lambda entry: entry.get("trial", 0))
        return history

    def export_plot_tracking(self):
        """Serialise the per-trial ASR tracking state (JSON-friendly)."""
        def points(pairs):
            return [list(pair) for pair in pairs]

        def category_points(category_dict):
            return {cat: points(pairs) for cat, pairs in category_dict.items()}

        return {
            "train_asr_per_trial": points(getattr(self, "_train_asr_per_trial", [])),
            "test_asr_per_trial": points(getattr(self, "_test_asr_per_trial", [])),
            "val_asr_per_trial": points(getattr(self, "_val_asr_per_trial", [])),
            "train_category_asr": category_points(getattr(self, "_train_category_asr", {})),
            "test_category_asr": category_points(getattr(self, "_test_category_asr", {})),
            "val_category_asr": category_points(getattr(self, "_val_category_asr", {})),
        }

    def restore_plot_tracking(self, plot_tracking):
        """Reload ASR tracking from a saved run so resumed plots keep earlier trials.

        Must be called after init_plot_tracking(), which resets the tracking state.
        """
        if not plot_tracking:
            return

        def points(pairs):
            return [tuple(pair) for pair in pairs]

        def category_points(category_dict):
            return defaultdict(list, {cat: points(pairs) for cat, pairs in (category_dict or {}).items()})

        self._train_asr_per_trial = points(plot_tracking.get("train_asr_per_trial", []))
        self._test_asr_per_trial = points(plot_tracking.get("test_asr_per_trial", []))
        self._val_asr_per_trial = points(plot_tracking.get("val_asr_per_trial", []))
        self._train_category_asr = category_points(plot_tracking.get("train_category_asr"))
        self._test_category_asr = category_points(plot_tracking.get("test_category_asr"))
        self._val_category_asr = category_points(plot_tracking.get("val_category_asr"))

    # ──────────────────────────────────────────────
    # Per-trial summary (written into trial directory)
    # ──────────────────────────────────────────────

    def create_trial_summary(self):
        """
        Create a human-readable summary of the current trial and save it as
        trial_summary.txt inside the trial directory.
        Reads data from:
          - attack_log.jsonl (last iteration)
          - judge_log.jsonl (last iteration)
          - strategist_log.jsonl (last iteration)
          - cipher_info.txt
          - tests/trial_{trial_num}/test_log.jsonl (if exists)
          - tests/trial_{trial_num}/test_asr.txt (if exists)
        """
        trial_dir = self.curr_trial_dir
        if not os.path.isdir(trial_dir):
            return

        output_file = os.path.join(trial_dir, TRIAL_SUMMARY_FILE)

        with open(output_file, "w", encoding="utf-8") as out:
            def log(text=""):
                out.write(str(text) + "\n")

            log(f"Trial: {self.curr_trial}")
            log(f"{'=' * 60}")
            log()

            # ── Cipher info ──
            cipher_info_path = os.path.join(trial_dir, CIPHER_INFO_FILE)
            if os.path.isfile(cipher_info_path):
                log("--- Cipher Info ---")
                with open(cipher_info_path, "r", encoding="utf-8") as f:
                    log(f.read())
                log()

            # ── Find last iteration dir ──
            iter_dirs = sorted([
                os.path.join(trial_dir, d)
                for d in os.listdir(trial_dir)
                if d.startswith("iter_")
            ])
            if not iter_dirs:
                log("[No iterations found in this trial]")
                return

            last_iter_dir = iter_dirs[-1]
            last_iter_num = int(os.path.basename(last_iter_dir).split("_")[-1])
            log(f"--- Iteration: {last_iter_num} (last) ---")
            log()

            # ── Strategist log ──
            strategist_path = os.path.join(last_iter_dir, STRATEGIST_LOG_FILE)
            strategist_data = []
            if os.path.isfile(strategist_path):
                with open(strategist_path, "r", encoding="utf-8") as f:
                    strategist_data = [json.loads(line) for line in f if line.strip()]
            if strategist_data:
                log("Strategist cipher suggestion:")
                log(json.dumps(strategist_data[0], indent=4, ensure_ascii=False))
                log()

            # ── Attack log ──
            attack_path = os.path.join(last_iter_dir, ATTACK_LOG_FILE)
            attack_data = []
            if os.path.isfile(attack_path):
                with open(attack_path, "r", encoding="utf-8") as f:
                    attack_data = [json.loads(line) for line in f if line.strip()]

            # ── Judge log ──
            judge_path = os.path.join(last_iter_dir, JUDGE_LOG_FILE)
            judge_data = []
            if os.path.isfile(judge_path):
                with open(judge_path, "r", encoding="utf-8") as f:
                    judge_data = [json.loads(line) for line in f if line.strip()]

            for sample_idx in range(len(attack_data)):
                log(f"Attack sample {sample_idx}:")
                log(json.dumps(attack_data[sample_idx], indent=4, ensure_ascii=False))
                log()

                if sample_idx < len(judge_data):
                    try:
                        judge_response = extract_json(
                            judge_data[sample_idx]["reject_judge_response"]
                        )
                    except Exception:
                        judge_response = judge_data[sample_idx]
                    log("Judge evaluation:")
                    log(json.dumps(judge_response, indent=4, ensure_ascii=False))
                    log()

            # ── Judge summary (last entry in judge log) ──
            summary_entries = [j for j in judge_data if "summarised_response" in j]
            if summary_entries:
                last_summary = summary_entries[-1]
                log("--- Judge Summary ---")
                log(f"Summarised response: {last_summary['summarised_response']}")
                log(f"Jailbreak success rate: {last_summary['jailbreak_success']}")
                log()

            # ── Test results for this trial (if any) ──
            test_trial_dir = os.path.join(
                self.log_dir, TEST_FOLDER_NAME, f"trial_{self.curr_trial}"
            )
            test_log_path = os.path.join(test_trial_dir, TEST_LOG_FILE)
            if os.path.isfile(test_log_path):
                log("--- Test Results ---")
                with open(test_log_path, "r", encoding="utf-8") as f:
                    test_lines = [json.loads(line) for line in f if line.strip()]
                # Skip the first line (best_cipher entry), process the rest as test samples
                for entry in test_lines[1:]:
                    log(f"Question: {entry.get('question', 'N/A')}")
                    log(f"Ciphered question: {entry.get('ciphered_question', 'N/A')}")
                    log(f"Target answer: {entry.get('target_answer', 'N/A')}")
                    log(f"Decrypted Answer: {entry.get('decrypted_answer', 'N/A')}")
                    log(f"Denoised Answer: {entry.get('denoised_answer', 'N/A')}")
                    log(f"Score: {entry.get('score', 'N/A')}")
                    log(f"Category: {entry.get('category', 'N/A')}")
                    log()

            test_asr_path = os.path.join(test_trial_dir, ASR_FILE)
            if os.path.isfile(test_asr_path):
                log("--- Test ASR ---")
                with open(test_asr_path, "r", encoding="utf-8") as f:
                    log(f.read())
                log()

        print(f"[Trial Summary] Saved {output_file}")

    # ──────────────────────────────────────────────
    # Plotting helpers for dynamic experiments
    # ──────────────────────────────────────────────

    def init_plot_tracking(self):
        """Initialize per-trial ASR tracking storage."""
        self._train_asr_per_trial = []       # list of (trial_num, asr)
        self._test_asr_per_trial = []        # list of (trial_num, asr)
        self._val_asr_per_trial = []         # list of (trial_num, asr)
        self._train_category_asr = defaultdict(list)  # category -> list of (trial_num, asr)
        self._test_category_asr = defaultdict(list)  # category -> list of (trial_num, asr)
        self._val_category_asr = defaultdict(list)   # category -> list of (trial_num, asr)

    def record_train_asr(self, trial_num, asr, category_asr_dict=None):
        """Record train ASR (overall and per-category) for a given trial."""
        self._train_asr_per_trial.append((trial_num, asr))
        if category_asr_dict:
            for cat, (cat_asr, _count) in category_asr_dict.items():
                self._train_category_asr[cat].append((trial_num, cat_asr))

    def record_test_asr(self, trial_num, asr, category_asr_dict=None):
        """Record test ASR (overall and per-category) for a given trial."""
        self._test_asr_per_trial.append((trial_num, asr))
        if category_asr_dict:
            for cat, (cat_asr, _count) in category_asr_dict.items():
                self._test_category_asr[cat].append((trial_num, cat_asr))

    def record_val_asr(self, trial_num, asr, category_asr_dict=None):
            """Record val ASR (overall and per-category) for a given trial."""
            self._val_asr_per_trial.append((trial_num, asr))
            if category_asr_dict:
                for cat, (cat_asr, _count) in category_asr_dict.items():
                    self._val_category_asr[cat].append((trial_num, cat_asr))

    def _ensure_plots_dir(self):
        """Create plots/ subdirectory inside log_dir."""
        plots_dir = os.path.join(self.log_dir, "plots")
        os.makedirs(plots_dir, exist_ok=True)
        return plots_dir

    def _save_plot_data_json(self, plots_dir):
        """
        Save all plot data as JSON files inside <plots_dir>/plot_data/.
        One JSON file per graph, containing the raw metrics (trial numbers and ASR values)
        so that multiple experiments can be aggregated later.

        Files saved:
          - plot_data/asr_over_trials.json       – overall train + test + val ASR
          - plot_data/asr_{category}.json         – per-category train + test + val ASR
          - plot_data/asr_all_categories.json     – combined: overall + per-category test + val ASR

        Raises:
          ValueError: if train ASR data is empty
        """
        if not self._train_asr_per_trial:
            raise ValueError("Train ASR data is empty. Cannot generate plots without training results.")

        data_dir = os.path.join(plots_dir, "plot_data")
        os.makedirs(data_dir, exist_ok=True)

        # ── 1. Overall train + test + val ASR ──
        overall = {}
        trials_t, asrs_t = zip(*self._train_asr_per_trial)
        overall["train"] = {"trials": list(trials_t), "asr": list(asrs_t)}

        if self._test_asr_per_trial:
            trials_te, asrs_te = zip(*self._test_asr_per_trial)
            overall["test"] = {"trials": list(trials_te), "asr": list(asrs_te)}

        if self._val_asr_per_trial:
            trials_v, asrs_v = zip(*self._val_asr_per_trial)
            overall["val"] = {"trials": list(trials_v), "asr": list(asrs_v)}

        overall_path = os.path.join(data_dir, "asr_over_trials.json")
        with open(overall_path, "w", encoding="utf-8") as f:
            json.dump(overall, f, indent=2, ensure_ascii=False)
        print(f"[Plot Data] Saved {overall_path}")

        # ── 2. Per-category ASR ──
        all_categories = set(self._train_category_asr.keys()) | set(self._test_category_asr.keys()) | set(self._val_category_asr.keys())

        for category in all_categories:
            cat_data = {}

            if category in self._train_category_asr:
                train_points = self._train_category_asr[category]
                trials_train, asrs_train = zip(*train_points)
                cat_data["train"] = {"trials": list(trials_train), "asr": list(asrs_train)}

            if category in self._test_category_asr:
                test_points = self._test_category_asr[category]
                trials_c, asrs_c = zip(*test_points)
                cat_data["test"] = {"trials": list(trials_c), "asr": list(asrs_c)}

            if category in self._val_category_asr:
                val_points = self._val_category_asr[category]
                trials_v, asrs_v = zip(*val_points)
                cat_data["val"] = {"trials": list(trials_v), "asr": list(asrs_v)}

            safe_cat = category.replace('/', '_').replace(' ', '_')
            cat_path = os.path.join(data_dir, f"asr_{safe_cat}.json")
            with open(cat_path, "w", encoding="utf-8") as f:
                json.dump(cat_data, f, indent=2, ensure_ascii=False)
            print(f"[Plot Data] Saved {cat_path}")

        # ── 3. Combined: all categories + overall test + val ASR ──
        combined = {}
        if self._test_asr_per_trial:
            trials_te, asrs_te = zip(*self._test_asr_per_trial)
            combined["overall_test"] = {"trials": list(trials_te), "asr": list(asrs_te)}

        if self._val_asr_per_trial:
            trials_v, asrs_v = zip(*self._val_asr_per_trial)
            combined["overall_val"] = {"trials": list(trials_v), "asr": list(asrs_v)}

        combined["categories"] = {}
        for category in all_categories:
            if category in self._test_category_asr:
                points = self._test_category_asr[category]
                trials_c, asrs_c = zip(*points)
                combined["categories"][category] = {"test": {"trials": list(trials_c), "asr": list(asrs_c)}}

            if category in self._val_category_asr:
                points = self._val_category_asr[category]
                trials_v, asrs_v = zip(*points)
                if category in combined["categories"]:
                    combined["categories"][category]["val"] = {"trials": list(trials_v), "asr": list(asrs_v)}
                else:
                    combined["categories"][category] = {"val": {"trials": list(trials_v), "asr": list(asrs_v)}}

        combined_path = os.path.join(data_dir, "asr_all_categories.json")
        with open(combined_path, "w", encoding="utf-8") as f:
            json.dump(combined, f, indent=2, ensure_ascii=False)
        print(f"[Plot Data] Saved {combined_path}")

    def plot_asr_over_trials(self):
        """
        Generate and save:
          1. asr_over_trials.png  – train + test + val ASR on one graph
          2. asr_{category}.png   – one file per category with train + test + val ASR
          3. asr_all_categories.png – combined: all categories + overall test + val ASR

        Additionally saves raw plot data as JSON files in <plots_dir>/plot_data/
        for later aggregation across experiments.

        Files are saved in <log_dir>/plots/ and overwritten each call.
        """
        plots_dir = self._ensure_plots_dir()

        # ── Save raw data as JSON first ──
        self._save_plot_data_json(plots_dir)

        # ── 1. Overall train + test + val ASR ──
        fig, ax = plt.subplots(figsize=(8, 5))

        trials_t, asrs_t = zip(*self._train_asr_per_trial)
        ax.plot(trials_t, asrs_t, marker='o', linestyle='-', label='Train ASR', color='#2c7bb6')

        if self._test_asr_per_trial:
            trials_te, asrs_te = zip(*self._test_asr_per_trial)
            ax.plot(trials_te, asrs_te, marker='s', linestyle='--', label='Test ASR', color='#d7191c')

        if self._val_asr_per_trial:
            trials_v, asrs_v = zip(*self._val_asr_per_trial)
            ax.plot(trials_v, asrs_v, marker='^', linestyle=':', label='Val ASR', color='#1a9850')

        ax.set_xlabel('Trial')
        ax.set_ylabel('ASR')
        ax.set_title('ASR over trials')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_ylim(-0.05, 1.05)

        overall_path = os.path.join(plots_dir, "asr_over_trials.png")
        fig.savefig(overall_path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        print(f"[Plot] Saved {overall_path}")

        # ── 2. Per-category ASR ──
        all_categories = set(self._train_category_asr.keys()) | set(self._test_category_asr.keys()) | set(self._val_category_asr.keys())

        for category in all_categories:
            fig_cat, ax_cat = plt.subplots(figsize=(8, 5))

            # Plot train ASR for this category (always present)
            if category in self._train_category_asr:
                train_points = self._train_category_asr[category]
                trials_train, asrs_train = zip(*train_points)
                ax_cat.plot(trials_train, asrs_train, marker='o', linestyle='-', label='Train ASR', color='#2c7bb6')

            # Plot test ASR for this category if available
            if category in self._test_category_asr:
                test_points = self._test_category_asr[category]
                trials_c, asrs_c = zip(*test_points)
                ax_cat.plot(trials_c, asrs_c, marker='s', linestyle='--', label='Test ASR', color='#d7191c')

            # Plot val ASR for this category if available
            if category in self._val_category_asr:
                val_points = self._val_category_asr[category]
                trials_v, asrs_v = zip(*val_points)
                ax_cat.plot(trials_v, asrs_v, marker='^', linestyle=':', label='Val ASR', color='#1a9850')

            ax_cat.set_xlabel('Trial')
            ax_cat.set_ylabel('ASR')
            ax_cat.set_title(f'ASR – {category}')
            ax_cat.legend()
            ax_cat.grid(True, alpha=0.3)
            ax_cat.set_ylim(-0.05, 1.05)

            safe_cat = category.replace('/', '_').replace(' ', '_')
            cat_path = os.path.join(plots_dir, f"asr_{safe_cat}.png")
            fig_cat.savefig(cat_path, dpi=150, bbox_inches='tight')
            plt.close(fig_cat)
            print(f"[Plot] Saved {cat_path}")

        # ── 3. Combined plot: all categories + overall test + val ASR on one graph ──
        fig_combined, ax_combined = plt.subplots(figsize=(10, 6))

        # Plot overall test ASR if available
        if self._test_asr_per_trial:
            trials_te, asrs_te = zip(*self._test_asr_per_trial)
            ax_combined.plot(trials_te, asrs_te, marker='o', linestyle='-', linewidth=2.5,
                             label='Overall Test ASR', color='black')

        # Plot overall val ASR if available
        if self._val_asr_per_trial:
            trials_v, asrs_v = zip(*self._val_asr_per_trial)
            ax_combined.plot(trials_v, asrs_v, marker='^', linestyle=':', linewidth=2.5,
                             label='Overall Val ASR', color='#1a9850')

        # Plot each category's test + val ASR
        colors = plt.cm.tab10.colors
        for idx, category in enumerate(all_categories):
            color = colors[idx % len(colors)]

            if category in self._test_category_asr:
                test_points = self._test_category_asr[category]
                trials_c, asrs_c = zip(*test_points)
                ax_combined.plot(trials_c, asrs_c, marker='s', linestyle='--', linewidth=1.5,
                                 label=f'Test ASR – {category}', color=color, alpha=0.8)

            if category in self._val_category_asr:
                val_points = self._val_category_asr[category]
                trials_v, asrs_v = zip(*val_points)
                ax_combined.plot(trials_v, asrs_v, marker='v', linestyle=':', linewidth=1.5,
                                 label=f'Val ASR – {category}', color=color, alpha=0.6)

        ax_combined.set_xlabel('Trial')
        ax_combined.set_ylabel('ASR')
        ax_combined.set_title('Test + Val ASR over trials – all categories + overall')
        ax_combined.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
        ax_combined.grid(True, alpha=0.3)
        ax_combined.set_ylim(-0.05, 1.05)

        combined_path = os.path.join(plots_dir, "asr_all_categories.png")
        fig_combined.savefig(combined_path, dpi=150, bbox_inches='tight')
        plt.close(fig_combined)
        print(f"[Plot] Saved {combined_path}")
    