from datasets import load_dataset
from torch.utils.data import DataLoader
import random
import json
import os
import uuid
from datetime import datetime
from collections import defaultdict


class HarmBenchTrainTestDataset:
    def __init__(
        self,
        test_ratio=0.2,
        max_length=None,
        train_category=None,
        seed=0,
        log_dir=None,
        train_max_len=None,
        test_max_len=None,
    ):
        self.query_max_length = max_length
        self.train_category = train_category
        self.seed = seed
        self.train_max_len = train_max_len
        self.test_max_len = test_max_len

        data = load_dataset("walledai/HarmBench", "standard", split="train")

        texts = [
            (prompt.strip(), category)
            for prompt, category in zip(data["prompt"], data["category"])
            if isinstance(prompt, str) and len(prompt.strip()) > 10
        ]

        rng = random.Random(self.seed)

        # Group texts by category
        by_category = defaultdict(list)
        for idx, (text, cat) in enumerate(texts):
            by_category[cat].append((idx, text, cat))

        # --- TEST SPLIT: take test_ratio from each category ---
        test_indices = set()
        test_raw = []

        for cat, items in by_category.items():
            rng.shuffle(items)
            n_test = max(1, int(len(items) * test_ratio))
            for idx, text, cat_name in items[:n_test]:
                test_indices.add(idx)
                test_raw.append((text, cat_name))

        # --- TRAIN SPLIT ---
        if self.train_category is None:
            # Take everything not used in test
            train_candidates = [
                (text, cat) for idx, (text, cat) in enumerate(texts)
                if idx not in test_indices
            ]
        else:
            # Take only the specified category, excluding test samples
            train_candidates = [
                (text, cat) for idx, (text, cat) in enumerate(texts)
                if idx not in test_indices and cat == self.train_category
            ]

        rng.shuffle(train_candidates)
        train_dataset = train_candidates

        # Apply train_max_len with proportional reduction per category
        if self.train_max_len is not None:
            by_category = defaultdict(list)
            for text, cat in train_dataset:
                by_category[cat].append((text, cat))

            # Calculate target count for each category
            total = len(train_dataset)
            train_dataset = []

            for cat, items in by_category.items():
                ratio = len(items) / total
                target_count = max(1, int(self.train_max_len * ratio))
                train_dataset.extend(items[:target_count])

            # Shuffle again to maintain randomization
            rng.shuffle(train_dataset)

        if self.query_max_length is not None:
            train_dataset = [(x[:self.query_max_length], y) for x, y in train_dataset]
            test_dataset = [(x[:self.query_max_length], y) for x, y in test_raw]
        else:
            test_dataset = test_raw

        if self.test_max_len is not None:
            test_dataset = test_dataset[:self.test_max_len]

        self.train_dataset = train_dataset
        self.test_dataset = test_dataset

        self.train_loader = DataLoader(
            self.train_dataset, batch_size=1, shuffle=False, collate_fn=lambda b: b[0]
        )
        self.test_loader = DataLoader(
            self.test_dataset, batch_size=1, shuffle=False, collate_fn=lambda b: b[0]
        )

        # --- LOGGING ---
        self._log_split(log_dir)

    def _log_split(self, log_dir=None):
        """Log train and test splits to JSON files in a uniquely-named folder."""
        if log_dir is None:
            log_dir = "dataset_splits"

        split_id = str(uuid.uuid4())[:8]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_name = f"split_{timestamp}_{split_id}"
        save_path = os.path.join(log_dir, folder_name)
        os.makedirs(save_path, exist_ok=True)

        # Save config
        config = {
            "test_ratio": self.test_ratio if hasattr(self, 'test_ratio') else None,
            "train_category": self.train_category,
            "seed": self.seed,
            "query_max_length": self.query_max_length,
            "train_size": len(self.train_dataset),
            "test_size": len(self.test_dataset),
        }
        with open(os.path.join(save_path, "config.json"), "w") as f:
            json.dump(config, f, indent=2)

        # Save train split
        train_records = [
            {"prompt": text, "category": cat}
            for text, cat in self.train_dataset
        ]
        with open(os.path.join(save_path, "train.json"), "w") as f:
            json.dump(train_records, f, indent=2, ensure_ascii=False)

        # Save test split
        test_records = [
            {"prompt": text, "category": cat}
            for text, cat in self.test_dataset
        ]
        with open(os.path.join(save_path, "test.json"), "w") as f:
            json.dump(test_records, f, indent=2, ensure_ascii=False)

        print(f"[HarmBenchTrainTestDataset] Split saved to {save_path}/")
