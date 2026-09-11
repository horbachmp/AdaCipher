import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict


class AggregateVisualizer:
    """Aggregates ASR plots across multiple runs of the same experiment."""

    def __init__(self, experiment_log_dir: str):
        """
        Args:
            experiment_log_dir: Path to the top-level experiment directory containing run_1, run_2, etc.
        """
        self.experiment_log_dir = Path(experiment_log_dir)
        self.runs_data = {}  # run_num -> plot_data

    def load_runs_data(self):
        """
        Load plot data from all run directories.
        Expects structure: experiment_dir/run_X/plots/plot_data/asr_over_trials.json
        """
        # Find all run directories
        run_dirs = sorted([
            d for d in self.experiment_log_dir.iterdir()
            if d.is_dir() and d.name.startswith("run_")
        ], key=lambda x: int(x.name.split("_")[1]))

        if not run_dirs:
            raise FileNotFoundError(f"No run directories found in {self.experiment_log_dir}")

        for run_dir in run_dirs:
            run_num = int(run_dir.name.split("_")[1])
            plot_data_dir = run_dir / "plots" / "plot_data"

            if plot_data_dir.exists():
                self.runs_data[run_num] = {
                    "asr_over_trials": self._load_json(plot_data_dir / "asr_over_trials.json"),
                    "plot_data_dir": plot_data_dir
                }

                # Load all per-category files
                for json_file in plot_data_dir.glob("asr_*.json"):
                    if json_file.name not in ["asr_over_trials.json", "asr_all_categories.json"]:
                        category = json_file.stem.replace("asr_", "")
                        if "categories" not in self.runs_data[run_num]:
                            self.runs_data[run_num]["categories"] = {}
                        self.runs_data[run_num]["categories"][category] = self._load_json(json_file)

    @staticmethod
    def _load_json(path: Path) -> dict:
        """Load JSON file, return empty dict if file doesn't exist."""
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def aggregate_asr_data(self, metric_type: str = "test") -> Dict[str, Dict]:
        """
        Aggregate ASR data across runs.

        Args:
            metric_type: "test", "train", or "val"

        Returns:
            Dict with overall and per-category aggregated data:
            {
                "overall": {"trials": [...], "mean": [...], "std": [...]},
                "categories": {
                    "cat1": {"trials": [...], "mean": [...], "std": [...]},
                    ...
                }
            }
        """
        if not self.runs_data:
            self.load_runs_data()

        aggregated = {"overall": {}, "categories": {}}

        # Aggregate overall ASR
        overall_by_trial = defaultdict(list)
        for run_num, data in self.runs_data.items():
            asr_data = data.get("asr_over_trials", {})
            if metric_type in asr_data:
                trials = asr_data[metric_type].get("trials", [])
                asrs = asr_data[metric_type].get("asr", [])
                for trial, asr in zip(trials, asrs):
                    overall_by_trial[trial].append(asr)
        if overall_by_trial:
            trials_sorted = sorted(overall_by_trial.keys())
            means = [np.mean(overall_by_trial[t]) for t in trials_sorted]
            stds = [np.std(overall_by_trial[t]) for t in trials_sorted]
            aggregated["overall"] = {
                "trials": trials_sorted,
                "mean": means,
                "std": stds
            }

        # Aggregate per-category ASR
        categories_by_trial = defaultdict(lambda: defaultdict(list))
        for run_num, data in self.runs_data.items():
            categories = data.get("categories", {})
            for category, cat_data in categories.items():
                if metric_type in cat_data:
                    trials = cat_data[metric_type].get("trials", [])
                    asrs = cat_data[metric_type].get("asr", [])
                    for trial, asr in zip(trials, asrs):
                        categories_by_trial[category][trial].append(asr)

        for category in categories_by_trial:
            trials_sorted = sorted(categories_by_trial[category].keys())
            means = [np.mean(categories_by_trial[category][t]) for t in trials_sorted]
            stds = [np.std(categories_by_trial[category][t]) for t in trials_sorted]
            aggregated["categories"][category] = {
                "trials": trials_sorted,
                "mean": means,
                "std": stds
            }

        return aggregated

    def plot_aggregated_asr(self, output_dir: Optional[str] = None):
        """
        Create aggregated ASR plots with all metrics (train, test, val) on same graph.

        Args:
            output_dir: Output directory. If None, uses experiment_log_dir
        """
        if output_dir is None:
            output_dir = self.experiment_log_dir
        else:
            output_dir = Path(output_dir)

        output_dir.mkdir(parents=True, exist_ok=True)

        # Load data once for all metric types
        if not self.runs_data:
            self.load_runs_data()

        # 1. Plot overall aggregated ASR (all metrics)
        self._plot_overall_all_metrics(output_dir)

        # 2. Plot per-category aggregated ASR (all metrics)
        self._plot_categories_all_metrics(output_dir)

        # 3. Plot all categories on one graph (test + val)
        self._plot_all_categories_all_metrics(output_dir)

    def _plot_overall_all_metrics(self, output_dir: Path):
        """Plot overall aggregated ASR with all metrics (train, test, val) with confidence bands."""
        fig, ax = plt.subplots(figsize=(12, 7))

        colors = {'train': '#2c7bb6', 'test': '#d7191c', 'val': '#1a9850'}
        markers = {'train': 'o', 'test': 's', 'val': '^'}
        linestyles = {'train': '-', 'test': '--', 'val': ':'}

        for metric_type in ['train', 'test', 'val']:
            aggregated = self.aggregate_asr_data(metric_type)
            if aggregated["overall"]:
                data = aggregated["overall"]
                trials = data["trials"]
                means = data["mean"]
                stds = data["std"]

                # Plot mean line
                ax.plot(trials, means, marker=markers[metric_type], linestyle=linestyles[metric_type],
                        linewidth=2.5, label=f'{metric_type.capitalize()} ASR (mean)',
                        color=colors[metric_type])

                # Plot ±1σ shaded region
                lower = np.array(means) - np.array(stds)
                upper = np.array(means) + np.array(stds)
                ax.fill_between(trials, lower, upper, alpha=0.15, color=colors[metric_type])

        ax.set_xlabel('Trial', fontsize=12)
        ax.set_ylabel('ASR', fontsize=12)
        ax.set_title('Aggregated ASR over Trials (Train, Test, Val – Mean ± Std)', fontsize=13)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(-0.05, 1.05)

        output_path = output_dir / "aggregated_asr_over_trials_all_metrics.png"
        fig.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        print(f"[Aggregated Plot] Saved {output_path}")

    def _plot_categories_all_metrics(self, output_dir: Path):
        """Plot per-category aggregated ASR with all metrics."""
        # First, collect all unique categories
        all_categories = set()
        for metric_type in ['train', 'test', 'val']:
            aggregated = self.aggregate_asr_data(metric_type)
            all_categories.update(aggregated["categories"].keys())

        colors = {'train': '#2c7bb6', 'test': '#d7191c', 'val': '#1a9850'}
        markers = {'train': 'o', 'test': 's', 'val': '^'}
        linestyles = {'train': '-', 'test': '--', 'val': ':'}

        for category in sorted(all_categories):
            fig, ax = plt.subplots(figsize=(12, 7))
            safe_category = category.replace('/', '_').replace(' ', '_')

            for metric_type in ['train', 'test', 'val']:
                aggregated = self.aggregate_asr_data(metric_type)
                if category in aggregated["categories"]:
                    data = aggregated["categories"][category]
                    trials = data["trials"]
                    means = data["mean"]
                    stds = data["std"]

                    # Plot mean line
                    ax.plot(trials, means, marker=markers[metric_type], linestyle=linestyles[metric_type],
                            linewidth=2.5, label=f'{metric_type.capitalize()} ASR (mean)',
                            color=colors[metric_type])

                    # Plot ±1σ shaded region
                    lower = np.array(means) - np.array(stds)
                    upper = np.array(means) + np.array(stds)
                    ax.fill_between(trials, lower, upper, alpha=0.15, color=colors[metric_type])

            ax.set_xlabel('Trial', fontsize=12)
            ax.set_ylabel('ASR', fontsize=12)
            ax.set_title(f'Aggregated {category} ASR (Train, Test, Val – Mean ± Std)', fontsize=13)
            ax.legend(fontsize=10)
            ax.grid(True, alpha=0.3)
            ax.set_ylim(-0.05, 1.05)

            output_path = output_dir / f"aggregated_asr_{safe_category}_all_metrics.png"
            fig.savefig(output_path, dpi=150, bbox_inches='tight')
            plt.close(fig)
            print(f"[Aggregated Plot] Saved {output_path}")

    def _plot_all_categories_all_metrics(self, output_dir: Path):
        """Plot all categories on one graph with test and val metrics."""
        # Collect all unique categories
        all_categories = set()
        for metric_type in ['test', 'val']:
            aggregated = self.aggregate_asr_data(metric_type)
            all_categories.update(aggregated["categories"].keys())

        if not all_categories:
            print("[Info] No per-category data found")
            return

        fig, ax = plt.subplots(figsize=(16, 9))
        colors = plt.cm.tab10(np.linspace(0, 1, len(all_categories)))
        markers = {'test': 's', 'val': '^'}
        linestyles = {'test': '--', 'val': ':'}

        for idx, category in enumerate(sorted(all_categories)):
            color = colors[idx]

            for metric_type in ['test', 'val']:
                aggregated = self.aggregate_asr_data(metric_type)
                if category in aggregated["categories"]:
                    data = aggregated["categories"][category]
                    trials = data["trials"]
                    means = data["mean"]
                    stds = data["std"]

                    # Plot mean line
                    ax.plot(trials, means, marker=markers[metric_type], linestyle=linestyles[metric_type],
                            linewidth=2, label=f'{category} – {metric_type.capitalize()}',
                            color=color, alpha=0.8)

                    # Plot ±1σ shaded region
                    lower = np.array(means) - np.array(stds)
                    upper = np.array(means) + np.array(stds)
                    ax.fill_between(trials, lower, upper, alpha=0.1, color=color)

        ax.set_xlabel('Trial', fontsize=12)
        ax.set_ylabel('ASR', fontsize=12)
        ax.set_title('Aggregated ASR over Trials – All Categories (Test & Val, Mean ± Std)', fontsize=13)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(-0.05, 1.05)

        output_path = output_dir / "aggregated_asr_all_categories_all_metrics.png"
        fig.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        print(f"[Aggregated Plot] Saved {output_path}")
