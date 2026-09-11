import os
import sys
from pathlib import Path
import argparse


from configs.config_reader import ConfigReader
from configs.exp_config import ExpConfig, DynamicExpConfig, ExpConfigFactory
from experiments.trainer import Trainer
from experiments.tester import Tester
from experiments.benign_tester import BenignTester
from utils.visualisations import AggregateVisualizer
from utils.select_best_cipher import find_best_cipher_across_runs, get_best_cipher_bundle, print_best_cipher_info
from ciphers.cipher import CipherBundle


# Experiment types that require both training and testing after each iteration
TRAIN_AND_TEST_EXP_TYPES = ["categories", "basic", "dynamic"]
# Experiment types that are test-only (no training iterations)
TEST_ONLY_EXP_TYPES = ["static"]
# Experiment types that are test-only and scored by the benign judge instead of the harm judge
BENIGN_TEST_EXP_TYPES = ["static_benign"]


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path to the experiment config", required=True)
    args = parser.parse_args()

    reader = ConfigReader(config_path=args.config)
    config_files = reader.read_config()
    config_factory = ExpConfigFactory()
    

    for config in config_files:
        print("=========================== Starting experiment ===========================")

        num_runs = config["num_runs"]

        for run in range(num_runs):
            print(f"--------------------------------- run {run+1}/{num_runs} ---------------------------------")

            config["run_number"] = run + 1
            result_config = config_factory.create_exp_config(config)

            exp_type = result_config.exp_type

            if exp_type in TRAIN_AND_TEST_EXP_TYPES:
                # --- Train + Test mode ---
                # Trainer runs trials and tests after each trial via the injected tester
                tester = Tester(result_config)
                trainer = Trainer(result_config, tester=tester)

                trainer.run()

            elif exp_type in TEST_ONLY_EXP_TYPES:
                # --- Test-only mode ---
                # Load the pre-configured cipher bundle and run testing directly
                tester = Tester(result_config)
                tester.cipher_bundle = result_config.cipher_bundle
                tester.test()

            elif exp_type in BENIGN_TEST_EXP_TYPES:
                # --- Benign test-only mode ---
                # Same as test-only, but answers are rated by the benign judge
                benign_tester = BenignTester(result_config)
                benign_tester.cipher_bundle = result_config.cipher_bundle
                benign_tester.test()

            else:
                raise ValueError(f"Unsupported experiment type: {exp_type}")

            # Summarize the last trial (set_trial only triggers for trials > 0)
            if hasattr(result_config.logger, 'curr_trial_dir') and os.path.isdir(result_config.logger.curr_trial_dir):
                result_config.logger.create_trial_summary()

        if exp_type in TRAIN_AND_TEST_EXP_TYPES: 
            # After all runs, generate aggregated plots
            print("=========================== Generating aggregated plots ===========================")
            try:
                experiment_log_dir = os.path.dirname(result_config.log_dir)
                visualizer = AggregateVisualizer(experiment_log_dir)
                visualizer.plot_aggregated_asr()
                print(f"[Success] Aggregated plots saved to {experiment_log_dir}")
            except Exception as e:
                print(f"[Warning] Failed to generate aggregated plots: {e}")

            # Find best cipher from validation and run final test
            print("\n=========================== Testing best validation cipher ===========================")
            try:
                experiment_log_dir = os.path.dirname(result_config.log_dir)
                run_name, trial_name, asr_score, bundle_path = find_best_cipher_across_runs(experiment_log_dir)

                if trial_name is not None and bundle_path is not None:
                    bundle_data = get_best_cipher_bundle(bundle_path)
                    print_best_cipher_info(trial_name, asr_score, bundle_data)

                    # Create cipher bundle and run test
                    best_cipher_bundle = CipherBundle(
                        module_path=bundle_data["module_path"],
                        description_json=bundle_data["description_json"],
                        name=bundle_data["name"],
                        base_cipher_prompt=bundle_data["base_cipher_prompt"]
                    )

                    # Create a new tester for final testing with a new logger for the new directory
                    from experiments.experiment_logger import ExperimentLogger
                    best_cipher_log_dir = os.path.join(experiment_log_dir, "best_cipher_test")
                    result_config.log_dir = best_cipher_log_dir
                    result_config.logger = ExperimentLogger(best_cipher_log_dir)
                    final_tester = Tester(result_config)
                    final_tester.cipher_bundle = best_cipher_bundle
                    final_tester.test()
                    print(f"[Success] Final test completed with best validation cipher")
                else:
                    print(f"[Warning] Could not find best validation cipher")
            except Exception as e:
                print(f"[Warning] Failed to test best validation cipher: {e}")

            





if __name__ == "__main__":
    main()
