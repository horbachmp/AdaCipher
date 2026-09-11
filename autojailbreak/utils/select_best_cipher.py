import os
import json
import re


def find_best_cipher_across_runs(experiment_dir):
    """Find the best cipher across all runs in an experiment.

    Args:
        experiment_dir: Path to experiment folder containing run_1, run_2, etc.

    Returns:
        tuple: (run_name, trial_name, asr_score, bundle_path) or (None, None, None, None) if not found
    """
    if not os.path.exists(experiment_dir):
        print(f"[Error] Experiment directory not found: {experiment_dir}")
        return None, None, None, None

    # Find all run directories
    run_dirs = []
    for item in os.listdir(experiment_dir):
        run_path = os.path.join(experiment_dir, item)
        if os.path.isdir(run_path) and re.match(r"run_\d+", item):
            run_dirs.append((item, run_path))

    if not run_dirs:
        print(f"[Warning] No run directories found in {experiment_dir}")
        return None, None, None, None

    run_dirs.sort()  # Sort numerically: run_1, run_2, ...

    best_run = None
    best_trial = None
    best_asr = -1
    best_bundle_path = None

    for run_name, run_path in run_dirs:
        trial_name, asr_score, bundle_path = find_best_validation_cipher(run_path)

        if asr_score is not None and asr_score > best_asr:
            best_asr = asr_score
            best_run = run_name
            best_trial = trial_name
            best_bundle_path = bundle_path

    if best_run is None:
        print(f"[Warning] Could not find best cipher across all runs")
        return None, None, None, None

    return best_run, best_trial, best_asr, best_bundle_path


def find_best_validation_cipher(log_dir):
    """Find cipher with highest ASR from validation logs.

    Returns:
        tuple: (trial_name, asr_score, bundle_path) or (None, None, None) if not found
    """
    val_dir = os.path.join(log_dir, "val")

    if not os.path.exists(val_dir):
        print(f"[Warning] Validation directory not found: {val_dir}")
        return None, None, None

    # Find all trial directories in val/
    trial_dirs = []
    for item in os.listdir(val_dir):
        trial_path = os.path.join(val_dir, item)
        if os.path.isdir(trial_path) and item.startswith("trial_"):
            trial_dirs.append((item, trial_path))

    if not trial_dirs:
        print(f"[Warning] No validation trials found in {val_dir}")
        return None, None, None

    # Read ASR scores for each trial
    best_trial = None
    best_asr = -1
    best_bundle_path = None

    for trial_name, trial_path in trial_dirs:
        asr_file = os.path.join(trial_path, "test_asr.txt")
        bundle_file = os.path.join(trial_path, "cipher_bundle.json")

        if not os.path.exists(asr_file) or not os.path.exists(bundle_file):
            continue

        # Read ASR score from test_asr.txt
        try:
            with open(asr_file, "r") as f:
                first_line = f.readline().strip()
                # Parse "General ASR score: 0.75"
                if "General ASR score:" in first_line:
                    asr_score = float(first_line.split(": ")[1])
                    if asr_score > best_asr:
                        best_asr = asr_score
                        best_trial = trial_name
                        best_bundle_path = bundle_file
        except (ValueError, IndexError) as e:
            print(f"[Warning] Failed to parse ASR from {asr_file}: {e}")
            continue

    if best_trial is None:
        print(f"[Warning] Could not find best cipher from validation trials")
        return None, None, None

    return best_trial, best_asr, best_bundle_path


def get_best_cipher_bundle(bundle_path):
    """Load cipher bundle from JSON file.

    Args:
        bundle_path: Path to cipher_bundle.json

    Returns:
        dict: Bundle data with name, module_path, description_json, base_cipher_prompt, prompt
    """
    with open(bundle_path, "r", encoding="utf-8") as f:
        bundle_data = json.load(f)
    return bundle_data


def print_best_cipher_info(trial_name, asr_score, bundle_data, run_name=None):
    """Print information about the best cipher found"""
    print(f"\n{'='*60}")
    print(f"[Best Validation Cipher]")
    if run_name:
        print(f"  Run: {run_name}")
    print(f"  Trial: {trial_name}")
    print(f"  ASR Score: {asr_score:.4f}")
    print(f"  Cipher Name: {bundle_data.get('name', 'Unknown')}")
    print(f"  Module: {bundle_data.get('module_path', 'Unknown')}")
    print(f"{'='*60}\n")
