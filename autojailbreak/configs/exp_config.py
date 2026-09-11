import os
import json

from models.api_model import OpenRouterModel
from models.local_models.qwen_model import QwenModel
from ciphers.caesar import CaesarCipher
from ciphers.random_bijection import RandomBijectionCipher
from ciphers.qwerty import QwertyCipher
from ciphers.cipher import CipherBundle
from custom_datasets.harmbench_dataset import HarmBenchDataset
from custom_datasets.harmbench_split_dataset import HarmBenchSplitDataset
from custom_datasets.harmbench_train_test_dataset import HarmBenchTrainTestDataset
from custom_datasets.alpaca_dataset import AlpacaDataset
from custom_datasets.alpaca_split import AlpacaSplitDataset
from denoiser.denoiser import LLMDenoiser
from summariser.summariser import LLMSummariser
from strategist.strategist import Strategist
from target.target import Target
from judges.harmbench_judge import HarmBenchJudge
from judges.benign_judge import BenignJudge
from judges.process_judge import ProcessJudge
from experiments.experiment_logger import ExperimentLogger, TRIAL_FOLDER_NAME, TRIAL_HISTORY_FILE
from guardrail.llamaguard import LocalLlamaGuard
from guardrail.llamaguard_openrouter import OpenRouterLlamaGuard
from guardrail.gpt_oss import OpenRouterGPTOSSSafeguard
from static_attacks.roleplay import RoleplayAttack
from static_attacks.persona import PersonaAttack


DYNAMIC_EXPS_TYPES = ["categories", "dynamic"]
STATIC_EXPS_TYPES = ["static", "static_benign"]


CIPHER_FLAG = "c"

# static experiments only: "<input><output>", 'c' = enciphered, 'p' = plain
CIPHERED_CHAR = "c"
PLAIN_CHAR = "p"
DEFAULT_CIPHER_FLAG = "cc"
PLAIN_CIPHER_FLAG = "pp"
VALID_CIPHER_FLAGS = ("cc", "cp", "pc", "pp")
ID_CIPHER_NAME = "id"

USER_TEXT_FLAG = "user: "
ASSISTANT_TEXT_FLAG = "assistant: "
EXAMPLES_TEXT_FLAG = "examples"
ROLE = "role"
CONTENT = "content"
USER = "user"
ASSISTANT = "assistant"


class ExpConfig:
    def __init__(self):

        self.num_runs = None

        self.strategist = None
        self.target = None
        self.target_name = None
        self.process_judge = None
        self.final_judge = None

        self.target_system_prompt = None

        self.config = None
        self.exp_type = None
        self.exp_name = None
        self.devices = None
        self.strategy_model_max_new_tokens = None
        self.code_model_max_new_tokens = None
        self.target_max_new_tokens = None
        self.process_judge_max_new_tokens = None
        self.final_judge_max_new_tokens = None
        self.start_cipher_bundle = None
        self.base_cipher_prompt = None
        self.temperature = None
        self.seed = None
        self.log_postfix = None
        self.log_dir = None
        self.max_length = None
        self.dataset = None
        self.raw_config_dict = None
        # self.system_prompt = None
        self.few_shot = None
        self.enciphered_input = None
        self.enciphered_output = None
        self.use_denoiser = None
        self.denoiser = None
        self.use_summariser = None
        self.summariser = None
        self.max_cipher_generation_iters = None

        self.num_trials = None

        # state of a previous run to resume from (see 'restore_trial')
        self.restore_state = None

        self.logger = None

        # training
        self.train_loader = None
        self.train_max_len = None

        # testing
        self.test_loader = None

        # eval
        self.benign_judge = None
        self.benign_eval = None
        self.benign_loader = None
        self.benign_judge_max_new_tokens = None

        # validation
        self.val_loader = None


        # static attack strategy
        self.attack = None


class DynamicExpConfig(ExpConfig):
    def __init__(self, config_dict):
        super().__init__()
        pass


class StaticExpConfig(ExpConfig):
    def __init__(self, config_dict):
        super().__init__()
        self.cipher_class_path = None

        # set from the 'cipher_flag' config field (see parse_cipher_flag)
        self.ciphered_input_flag = None
        self.ciphered_output_flag = None




class ExpConfigFactory:


    @staticmethod
    def initialise_common_fields(config, config_dict):
        models_run_ids = {}
        config.seed = config_dict.get('seed', 0)

        
        config.config = config_dict
        config.exp_type = config_dict['exp_type']
        config.num_runs = config_dict['num_runs']
        config.target_name = config_dict['target_model_name']
        config.exp_name = config_dict["exp_name"]
        config.log_postfix = config_dict.get('log_postfix', '')
        log_dir_name = config.exp_name
        if config.log_postfix:
            log_dir_name = f"{config.exp_name}"
        config.log_dir = os.path.join(config_dict['log_path'], config.exp_type, config_dict['dataset'], log_dir_name, f"{config.target_name.split('/')[-1]}".replace("-","_").replace(".","_")+f"_{config.log_postfix}", f"run_{config_dict['run_number']}")

        config.logger = ExperimentLogger(config.log_dir, config_dict=config.config)
        config.devices = config_dict.get('devices', None)

        config.target_max_new_tokens = config_dict['target_max_new_tokens']

        config.final_judge_max_new_tokens = config_dict['final_judge_max_new_tokens']

        

        target_system_prompt = ExpConfigFactory.read_system_prompt(system_prompt_path=config_dict['target_system_prompt'])
        final_judge_system_prompt = ExpConfigFactory.read_system_prompt(system_prompt_path=config_dict["final_judge_system_prompt"])

        # config.cipher = ExpConfigFactory.create_cipher(config_dict['cipher'])
        # config.system_prompt = config.cipher.create_cipher_prompt(config.system_prompt, config.exp_type)
        # print(f"Final system prompt for experiment:\n{config.system_prompt}")

        # few shot
        final_judge_few_shot = ExpConfigFactory.create_few_shot_examples(examples_path=config_dict["final_judge_few_shot_path"])
        target_few_shot = ExpConfigFactory.create_few_shot_examples(examples_path=config_dict["target_few_shot_path"])



        train_dataset_size = config_dict.get('train_dataset_size', None)
        val_dataset_size = config_dict.get('val_dataset_size', None)
        test_dataset_size = config_dict.get('test_dataset_size', None)
        train_dataset_category = config_dict.get('train_category', None)
        if train_dataset_category == "None":
            train_dataset_category = None
        val_dataset_category = config_dict.get('val_category', None)
        if val_dataset_category == "None":
            val_dataset_category = None
        test_dataset_category = config_dict.get('test_category', None)
        if test_dataset_category == "None":
            test_dataset_category = None
        test_ratio = config_dict.get("test_ratio", None)
        train_max_len = config_dict.get("train_max_len", None)
        max_length = config_dict['query_max_length']
        config.train_max_len = train_max_len
        config.dataset = ExpConfigFactory.create_dataset(
            dataset_name=config_dict['dataset'],
            dataset_size=(train_dataset_size, val_dataset_size, test_dataset_size),
            query_max_length=max_length,
            seed=config.seed,
            category=(train_dataset_category, val_dataset_category, test_dataset_category),
            test_ratio=test_ratio,
            log_dir=config.log_dir,
            train_max_len=train_max_len
        )
        config.train_loader = config.dataset.train_loader
        if val_dataset_size is not None:
            config.val_loader = config.dataset.val_loader
        config.test_loader = config.dataset.test_loader
        
        # target

        print("Configuring target...")
        target_model, target_run_id = ExpConfigFactory.create_model(
            model_type=config_dict['target_model_type'],
            model_name=config_dict['target_model_name'],
            max_new_tokens=config.target_max_new_tokens,
            devices=config.devices,
            seed=config.seed,
            temperature=config.temperature
        )
        models_run_ids['target_model'] = target_run_id

        target_benign_few_shot = None
        if config_dict.get("target_benign_few_shot_path", None) is not None:
            target_benign_few_shot = ExpConfigFactory.create_few_shot_examples(examples_path=config_dict["target_benign_few_shot_path"])


        use_input_guard = config_dict.get("use_input_guard", False)
        use_output_guard = config_dict.get("use_output_guard", False)

        guard = None
        if (use_input_guard or use_output_guard) and config_dict.get("guard_type", None) is not None:
            guard = ExpConfigFactory.create_guard(config_dict.get("guard_type"), devices=config.devices)

        config.target = Target(target_model, target_system_prompt, target_few_shot, target_benign_few_shot, guard, use_input_guard, use_output_guard)
        

        # final judge
        print("Configuring final judge...")
        final_judge_model, final_judge_run_id = ExpConfigFactory.create_model(
            model_type=config_dict['final_judge_model_type'],
            model_name=config_dict['final_judge_model_name'],
            max_new_tokens=config.final_judge_max_new_tokens,
            devices=config.devices,
            seed=config.seed,
            temperature=config.temperature
        )
        models_run_ids['final_judge_model'] = final_judge_run_id
        if config_dict["final_judge_type"] == "harm_bench":
            config.final_judge = HarmBenchJudge(final_judge_model, final_judge_system_prompt, final_judge_few_shot)
        else:
            raise NotImplementedError("Final judge type not implemented")

        
        config.denoiser = ExpConfigFactory.create_denoiser(config_dict=config_dict, seed=config.seed)

        return config, models_run_ids



    @staticmethod
    def create_dynamic_config(config_dict):
        models_run_ids = {}
        config = DynamicExpConfig(config_dict)
        config, models_run_ids_common = ExpConfigFactory.initialise_common_fields(config, config_dict)
        models_run_ids.update(models_run_ids_common)

        config.base_cipher_prompt = ExpConfigFactory.read_system_prompt(system_prompt_path=config_dict['base_cipher_prompt'])

        # state of a crashed run to continue from, if requested
        config.restore_state = ExpConfigFactory.load_restore_state(config_dict)

        with open(config_dict['start_cipher_description_path'], "r", encoding="utf-8") as f:
            start_cipher_description = json.load(f)

        config.start_cipher_bundle = CipherBundle(module_path=config_dict['start_cipher_module_path'], description_json=start_cipher_description, name=config_dict['start_cipher_name'], base_cipher_prompt=config.base_cipher_prompt)
        config.temperature = config_dict.get('temperature', 0.0)


        config.strategy_model_max_new_tokens = config_dict['strategy_model_max_new_tokens']
        config.code_model_max_new_tokens = config_dict['code_model_max_new_tokens']
        config.process_judge_max_new_tokens = config_dict['process_judge_max_new_tokens']
        config.max_cipher_generation_iters = config_dict['max_cipher_generation_iters']
        config.num_trials = config_dict.get('num_trials', 1)

        strategy_system_prompt = ExpConfigFactory.read_system_prompt(system_prompt_path=config_dict["strategy_system_prompt"])
        code_system_prompt = ExpConfigFactory.read_system_prompt(system_prompt_path=config_dict["code_system_prompt"])
        process_judge_system_prompt = ExpConfigFactory.read_system_prompt(system_prompt_path=config_dict["process_judge_system_prompt"])
    
        #few shot
        strategy_few_shot = ExpConfigFactory.create_few_shot_examples(examples_path=config_dict["strategy_few_shot_path"])
        code_few_shot = ExpConfigFactory.create_few_shot_examples(examples_path=config_dict["code_few_shot_path"])
        process_judge_few_shot = ExpConfigFactory.create_few_shot_examples(examples_path=config_dict["process_judge_few_shot_path"])


        #Strategist
        print("Configuring strategist...")
        strategy_model, strategist_run_id = ExpConfigFactory.create_model(
            model_type=config_dict['strategy_model_type'],
            model_name=config_dict['strategy_model_name'],
            max_new_tokens=config.strategy_model_max_new_tokens,
            devices=config.devices,
            seed=config.seed,
            temperature=config.temperature,
        )
        models_run_ids['strategy_model'] = strategist_run_id

        code_model, code_run_id = ExpConfigFactory.create_model(
            model_type=config_dict['code_model_type'],
            model_name=config_dict['code_model_name'],
            max_new_tokens=config.code_model_max_new_tokens,
            devices=config.devices,
            seed=config.seed,
            temperature=config.temperature
        )
        models_run_ids['code_model'] = code_run_id


        verification_tests_path = config_dict.get('verification_tests_path', None)

        config.strategist = Strategist(strategy_model, code_model, config.max_cipher_generation_iters, strategy_system_prompt, code_system_prompt, base_cipher_prompt=config.base_cipher_prompt, strategy_few_shot=strategy_few_shot, code_few_shot=code_few_shot, log_dir=config.log_dir, logger=config.logger, verification_tests_path=verification_tests_path)


        #benign judge
        config.benign_eval = config_dict['benign_eval']
        if config.benign_eval:
            print("Configuring benign judge...")
            config.benign_judge_max_new_tokens = config_dict['benign_judge_max_new_tokens']
            benign_judge_few_shot = ExpConfigFactory.create_few_shot_examples(examples_path=config_dict["benign_judge_few_shot_path"])
            benign_judge_system_prompt = ExpConfigFactory.read_system_prompt(system_prompt_path=config_dict["benign_judge_system_prompt"])

            benign_judge_model, benign_judge_run_id = ExpConfigFactory.create_model(
                model_type=config_dict['benign_judge_model_type'],
                model_name=config_dict['benign_judge_model_name'],
                max_new_tokens=config.benign_judge_max_new_tokens,
                devices=config.devices,
                seed=config.seed,
                temperature=config.temperature
            )
            models_run_ids['benign_judge_model'] = benign_judge_run_id
            config.benign_judge = BenignJudge(benign_judge_model, benign_judge_system_prompt, benign_judge_few_shot)

            config.benign_dataset = ExpConfigFactory.create_dataset(
                dataset_name=config_dict['benign_eval_dataset'],
                dataset_size=config_dict['benign_eval_dataset_size'],
                query_max_length=config_dict['query_max_length'],
                seed=config.seed
            )

        # process judge
        print("Configuring process judge...")
        process_judge_model, process_judge_run_id = ExpConfigFactory.create_model(
            model_type=config_dict['process_judge_model_type'],
            model_name=config_dict['process_judge_model_name'],
            max_new_tokens=config.process_judge_max_new_tokens,
            devices=config.devices,
            seed=config.seed,
            temperature=config.temperature
        )
        models_run_ids['process_judge_model'] = process_judge_run_id
        if config_dict["process_judge_type"] == "None":
            config.process_judge = ProcessJudge(process_judge_model, process_judge_system_prompt, process_judge_few_shot)
        else:
            raise NotImplementedError("Process judge type not implemented")

        config.summariser = ExpConfigFactory.create_summariser(config_dict=config_dict, seed=config.seed)

        return config, models_run_ids
    


    @staticmethod
    def create_static_config(config_dict):
        models_run_ids = {}
        config = StaticExpConfig(config_dict)
        config, models_run_ids_common = ExpConfigFactory.initialise_common_fields(config, config_dict)
        models_run_ids.update(models_run_ids_common)

        cipher_flag = config_dict.get('cipher_flag', DEFAULT_CIPHER_FLAG)
        config.ciphered_input_flag, config.ciphered_output_flag = ExpConfigFactory.parse_cipher_flag(cipher_flag)
        # the few-shot examples must be enciphered on the same sides as the conversation
        config.target.set_cipher_flags(config.ciphered_input_flag, config.ciphered_output_flag)

        cipher_description_path = ExpConfigFactory.get_optional_path(config_dict, 'cipher_description_path')
        cipher_bundle_path = ExpConfigFactory.get_optional_path(config_dict, 'cipher_bundle_path')

        if config_dict.get('cipher_name', None) == ID_CIPHER_NAME:
            config.base_cipher_prompt = ""
            config.cipher_bundle = CipherBundle(
                module_path=config_dict['cipher_module_path'],
                description_json={},
                name=ID_CIPHER_NAME,
                base_cipher_prompt=config.base_cipher_prompt
            )
        elif cipher_description_path is not None:
            with open(cipher_description_path, "r", encoding="utf-8") as f:
                cipher_description = json.load(f)
            config.base_cipher_prompt = ExpConfigFactory.read_system_prompt(system_prompt_path=config_dict['base_cipher_prompt'])
            config.cipher_bundle = CipherBundle(
                module_path=config_dict['cipher_module_path'],
                description_json=cipher_description,
                name=config_dict['cipher_name'],
                base_cipher_prompt=config.base_cipher_prompt
            )
        else:
            if cipher_bundle_path is None:
                raise ValueError(
                    "Static config must define either 'cipher_description_path' "
                    "(together with 'cipher_name', 'cipher_module_path' and 'base_cipher_prompt') "
                    "or 'cipher_bundle_path' pointing to a saved cipher bundle JSON."
                )
            print(f"Loading cipher bundle from {cipher_bundle_path}...")
            config.cipher_bundle = CipherBundle.load(cipher_bundle_path)
            config.base_cipher_prompt = config.cipher_bundle.base_cipher_prompt

        # nothing is enciphered, so the cipher must be a no-op
        plain_run = not config.ciphered_input_flag and not config.ciphered_output_flag
        if plain_run and config.cipher_bundle.name != ID_CIPHER_NAME:
            raise ValueError(
                f"cipher_flag '{PLAIN_CIPHER_FLAG}' leaves both input and output plain, "
                f"so the cipher must be '{ID_CIPHER_NAME}', got '{config.cipher_bundle.name}'."
            )

        config.cipher_bundle.save(os.path.join(config.log_dir, "cipher_bundle.json"))

        # benign judge — used by BenignTester, i.e. the 'static_benign' experiments
        config.benign_eval = config_dict.get('benign_eval', False)
        if config.benign_eval:
            print("Configuring benign judge...")
            config.benign_judge_max_new_tokens = config_dict['benign_judge_max_new_tokens']
            benign_judge_few_shot = ExpConfigFactory.create_few_shot_examples(examples_path=config_dict["benign_judge_few_shot_path"])
            benign_judge_system_prompt = ExpConfigFactory.read_system_prompt(system_prompt_path=config_dict["benign_judge_system_prompt"])

            benign_judge_model, benign_judge_run_id = ExpConfigFactory.create_model(
                model_type=config_dict['benign_judge_model_type'],
                model_name=config_dict['benign_judge_model_name'],
                max_new_tokens=config.benign_judge_max_new_tokens,
                devices=config.devices,
                seed=config.seed,
                temperature=config.temperature
            )
            models_run_ids['benign_judge_model'] = benign_judge_run_id
            config.benign_judge = BenignJudge(benign_judge_model, benign_judge_system_prompt, benign_judge_few_shot)


        print("Configuring attack...")
        attack_type = config_dict.get("attack_type", None)
        if attack_type is not None:
            model_name = config_dict["model_name"]
            config.attack = ExpConfigFactory.create_attack(attack_type, model_name)
        return config, models_run_ids



    @staticmethod
    def create_exp_config(config_dict):
        config = None
        exp_type = config_dict['exp_type']

        models_run_ids = {}

        ################################# DYNAMIC CONFIGURATION #############################
        if exp_type in DYNAMIC_EXPS_TYPES:
            config, models_run_ids_dyn = ExpConfigFactory.create_dynamic_config(config_dict)
            models_run_ids.update(models_run_ids_dyn)
            
        ############################### STATIC CONFIGURATION #############################

        elif exp_type in STATIC_EXPS_TYPES:
            config, models_run_ids_stat = ExpConfigFactory.create_static_config(config_dict)
            models_run_ids.update(models_run_ids_stat)

        else:
            raise ValueError(f"Unsupported experiment type: {exp_type}")
        
        models_registry_path = os.path.join(config.log_dir, "models_run_ids.json")
        with open(models_registry_path, 'w', encoding='utf-8') as f:
            json.dump(models_run_ids, f, indent=2, ensure_ascii=False)

        return config


    # ──────────────────────────────────────────────
    # Resuming a crashed run from a saved trial ('restore_trial')
    # ──────────────────────────────────────────────

    @staticmethod
    def resolve_restore_trial_path(config_dict):
        """Resolve the 'restore_trial' config field into a trial_history.json path.

        Accepted values:
          - path to a trial_history.json file
          - path to an attack_trial_{n} directory
          - path to a run log directory (the last saved trial is used)
          - a trial number, together with 'restore_log_dir' pointing at the run log directory
        Returns None when 'restore_trial' is not set.
        """
        restore_trial = config_dict.get('restore_trial', None)
        if restore_trial is None or restore_trial in ("None", ""):
            return None

        restore_log_dir = ExpConfigFactory.get_optional_path(config_dict, 'restore_log_dir')

        # a bare trial number needs the run directory it belongs to
        if isinstance(restore_trial, int) or str(restore_trial).isdigit():
            if restore_log_dir is None:
                raise ValueError(
                    "'restore_trial' is a trial number, so 'restore_log_dir' must point "
                    "at the log directory of the run to resume."
                )
            history_path = os.path.join(
                restore_log_dir,
                TRIAL_FOLDER_NAME.format(trial_num=int(restore_trial)),
                TRIAL_HISTORY_FILE
            )
        elif os.path.isdir(restore_trial):
            history_path = os.path.join(restore_trial, TRIAL_HISTORY_FILE)
            if not os.path.isfile(history_path):
                # a run directory: fall back to the last trial that was saved
                history = ExperimentLogger.read_trial_history(restore_trial)
                if not history:
                    raise FileNotFoundError(
                        f"No {TRIAL_HISTORY_FILE} found in '{restore_trial}' or its trial directories."
                    )
                history_path = os.path.join(
                    restore_trial,
                    TRIAL_FOLDER_NAME.format(trial_num=history[-1]["trial"]),
                    TRIAL_HISTORY_FILE
                )
        else:
            history_path = restore_trial

        if not os.path.isfile(history_path):
            raise FileNotFoundError(f"Trial history file '{history_path}' does not exist.")

        return history_path


    @staticmethod
    def load_restore_state(config_dict):
        """Read the trial state pointed at by 'restore_trial'. None if not requested."""
        history_path = ExpConfigFactory.resolve_restore_trial_path(config_dict)
        if history_path is None:
            return None

        with open(history_path, "r", encoding="utf-8") as f:
            restore_state = json.load(f)

        print(f"Restoring experiment state from {history_path} (trial {restore_state.get('trial')})")
        return restore_state


    @staticmethod
    def create_cipher_bundle_from_dict(bundle_dict):
        """Build a CipherBundle from its serialised form (as stored in trial_history.json)."""
        return CipherBundle(
            module_path=bundle_dict["module_path"],
            description_json=bundle_dict["description_json"],
            name=bundle_dict["name"],
            base_cipher_prompt=bundle_dict.get("base_cipher_prompt", "")
        )


    @staticmethod
    def restore_trainer_state(trainer, restore_state):
        """Load a saved trial state into a Trainer so it continues from the next trial.

        Puts back everything the trainer carries across trials: the current cipher
        bundle (and the target few-shot built from it), every bundle produced so far,
        the best bundle, the strategist memory, the judge feedback the next trial
        starts from, and the logger's ASR tracking for the plots.

        No-op when restore_state is None, i.e. a normal run starting from trial 0.
        """
        if not restore_state:
            return trainer

        bundle_dict = restore_state.get("cipher_bundle", None)
        if bundle_dict is None:
            raise ValueError("Restore state contains no 'cipher_bundle' — cannot resume the run.")

        trainer.cipher_bundle = ExpConfigFactory.create_cipher_bundle_from_dict(bundle_dict)
        trainer.target.cipher_few_shot(trainer.cipher_bundle)

        trainer.ciphers = [
            ExpConfigFactory.create_cipher_bundle_from_dict(bundle)
            for bundle in restore_state.get("ciphers", []) if bundle
        ]

        best_bundle_dict = restore_state.get("best_cipher_bundle", None)
        trainer.best_cipher_bundle = (
            ExpConfigFactory.create_cipher_bundle_from_dict(best_bundle_dict)
            if best_bundle_dict else trainer.cipher_bundle
        )
        trainer.best_cipher_jailbreak_number = restore_state.get("best_cipher_jailbreak_number", 0)

        trainer.process_judge_feedback = [
            tuple(item) for item in restore_state.get("process_judge_feedback", [])
        ]
        trainer.summarised_response = restore_state.get("summarised_response", None)
        trainer.restored_plot_tracking = restore_state.get("plot_tracking", None)

        trainer.start_trial = restore_state.get("next_trial", restore_state.get("trial", -1) + 1)
        trainer.current_trial = trainer.start_trial

        print(
            f"Trainer restored: continuing from trial {trainer.start_trial} "
            f"with cipher '{trainer.cipher_bundle.name}' "
            f"({len(trainer.process_judge_feedback)} feedback entries in memory)"
        )
        return trainer


    @staticmethod
    def create_denoiser(config_dict, seed=0):
        if config_dict.get('use_denoiser', False):
            return LLMDenoiser(seed=seed)
        else:
            return None


    @staticmethod
    def create_summariser(config_dict, seed=0):
        if config_dict.get('use_summariser', False):
            return LLMSummariser(seed=seed)
        else:
            return None

    @staticmethod
    def create_guard(guard_name, devices=None):
        if guard_name is None or guard_name == "None":
            return None

        if guard_name == 'local_llamaguard':
            return LocalLlamaGuard(devices=devices)
        elif guard_name == 'llamaguard':
            return OpenRouterLlamaGuard()
        elif guard_name == "gptoss":
            return OpenRouterGPTOSSSafeguard()
        else:
            raise NotImplementedError(f"Guard type '{guard_name}' not implemented")


    @staticmethod
    def create_model(model_type, model_name, max_new_tokens, devices=None, seed=0, temperature=0.0):
        model = None
        if "local" in model_type:
            if model_name.startswith("qwen"):
                model = QwenModel(
                    model_name=model_name,
                    max_new_tokens=max_new_tokens,
                    seed=seed,
                    devices=devices,
                )
            else:
                raise ValueError(f"Unsupported local model: {model_name}")
        elif "openrouter" in model_type:
            model = OpenRouterModel(
                model_name=model_name,
                max_new_tokens=max_new_tokens,
                seed=seed,
                temperature=temperature,
            )
        else:
            raise NotImplementedError(f"API Model {model_type} not implemented")
        model_run_id = model.run_id
        return model, model_run_id


    @staticmethod
    def create_dataset(dataset_name, dataset_size, query_max_length, seed, dataset_path=None, category=None, test_ratio=None, log_dir=None, train_max_len=None):
        if dataset_name == "harmbench":
            dataset = HarmBenchDataset(dataset_size, query_max_length, seed=seed, category=category)
        elif dataset_name == "alpaca":
            dataset = AlpacaDataset(dataset_size, query_max_length, seed=seed)
        elif dataset_name == "alpaca_split":
            dataset = AlpacaSplitDataset(dataset_size[0], dataset_size[1], dataset_size[2], query_max_length, seed=seed)
        elif dataset_name == "harmbench_split":
            dataset = HarmBenchSplitDataset(dataset_size[0], dataset_size[1], dataset_size[2], query_max_length, seed=seed, train_category=category[0], val_category=category[1], test_category=category[2])
        elif dataset_name == "harmbench_train_test":
            dataset = HarmBenchTrainTestDataset(test_ratio=test_ratio, max_length=query_max_length, train_category=category[0], seed=seed, log_dir=log_dir, train_max_len=train_max_len)
        else:
            raise NotImplementedError(f"Dataset {dataset_name} not implemented")
        return dataset


    @staticmethod
    def create_cipher(cipher_name, seed=0):
        if cipher_name[:6] == "caesar":
            shift = int(cipher_name.split("_")[1])
            return CaesarCipher(shift)
        elif cipher_name == "random_bijection":
            return RandomBijectionCipher(seed=seed)
        elif cipher_name == "qwerty":
            return QwertyCipher()
        else:
            raise NotImplementedError(f"Cipher {cipher_name} not implemented")


    @staticmethod
    def parse_cipher_flag(cipher_flag):
        """Split the static-experiment 'cipher_flag' into (ciphered_input, ciphered_output).

        The flag is two characters, "<input><output>", where 'c' means the text is
        enciphered and 'p' means it stays plain: "cc" (default) enciphers both,
        "cp" enciphers the input only, "pc" the output only, "pp" neither.
        """
        if cipher_flag is None or cipher_flag == "None" or cipher_flag == "":
            cipher_flag = DEFAULT_CIPHER_FLAG

        cipher_flag = str(cipher_flag).strip().lower()
        if cipher_flag not in VALID_CIPHER_FLAGS:
            raise ValueError(
                f"Unsupported cipher_flag '{cipher_flag}', expected one of {VALID_CIPHER_FLAGS}"
            )

        input_char, output_char = cipher_flag
        return input_char == CIPHERED_CHAR, output_char == CIPHERED_CHAR


    @staticmethod
    def get_optional_path(config_dict, key):
        path = config_dict.get(key, None)
        if path is None or path == "None" or path == "":
            return None
        return path


    @staticmethod
    def read_system_prompt(system_prompt_path):
        prompt = ""
        if system_prompt_path != "None":
            with open(system_prompt_path) as f:
                prompt += f.read() + "\n"

        return prompt

    # @staticmethod
    # def create_few_shot_examples(examples_path):
    #     few_shot = []
    #     with open(examples_path) as f:
    #         for line in f:
    #             if line.startswith(USER_TEXT_FLAG):
    #                 content = line[len(USER_TEXT_FLAG):]
    #                 few_shot.append({ROLE: USER, CONTENT:content})
    #             elif line.startswith(ASSISTANT_TEXT_FLAG):
    #                 content = line[len(ASSISTANT_TEXT_FLAG):]
    #                 few_shot.append({ROLE: ASSISTANT, CONTENT:content})
    #     return few_shot


    @staticmethod
    def create_few_shot_examples(examples_path):
        with open(examples_path, encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, dict) and EXAMPLES_TEXT_FLAG in data:
            data = data[EXAMPLES_TEXT_FLAG]

        few_shot = []
        for item in data:
            role = item.get(ROLE)
            content = item.get(CONTENT)

            if role in (USER, ASSISTANT) and content is not None:
                few_shot.append({ROLE: role, CONTENT: content})

        return few_shot


    @staticmethod
    def create_attack(attack_type, model_name):
        model = OpenRouterModel(model_name=model_name)
        if attack_type == "roleplay":
            return RoleplayAttack()
        elif attack_type == "persona":
            return PersonaAttack(model=model)
        else:
            raise NotImplementedError(f"Attack type {attack_type} not implemented")
