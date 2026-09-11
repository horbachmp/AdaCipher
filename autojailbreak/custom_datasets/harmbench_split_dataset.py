from datasets import load_dataset
from torch.utils.data import DataLoader
import random


class HarmBenchSplitDataset:
    def __init__(
        self,
        train_size,
        val_size,
        test_size,
        max_length=None,
        train_category=None,
        val_category=None,
        test_category=None,
        seed=0,
        allow_fallback_to_other_categories=True
    ):
        self.train_size = train_size
        self.val_size = val_size
        self.test_size = test_size
        self.query_max_length = max_length
        self.train_category = train_category
        self.val_category = val_category
        self.test_category = test_category
        self.seed = seed
        self.allow_fallback_to_other_categories = allow_fallback_to_other_categories

        data = load_dataset("walledai/HarmBench", "standard", split="train")

        texts = [
            (prompt.strip(), category)
            for prompt, category in zip(data["prompt"], data["category"])
            if isinstance(prompt, str) and len(prompt.strip()) > 10
        ]

        rng = random.Random(self.seed)
        rng.shuffle(texts)

        used = set()

        def take_split(size, category, split_name):


            candidates = [
                i for i, (_, cat) in enumerate(texts)
                if i not in used and (category is None or cat == category)
            ]

            selected_idx = candidates[:size]

            if len(selected_idx) < size and self.allow_fallback_to_other_categories:
                print(f"[{split_name}] Requested {size}, got {len(selected_idx)}. "
                      f"Fallback to other categories.")
                
                need = size - len(selected_idx)
                fallback = [
                    i for i, _ in enumerate(texts)
                    if i not in used and i not in selected_idx
                ]
                selected_idx.extend(fallback[:need])

                

            if len(selected_idx) < size:
                print(
                    f"[{split_name}] Requested {size}, got {len(selected_idx)}. "
                    f"Not enough samples for category={category!r}."
                )

            for i in selected_idx:
                used.add(i)

            split = [texts[i] for i in selected_idx]

            if self.query_max_length is not None:
                split = [(x[:self.query_max_length], y) for x, y in split]

            return split

        self.train_dataset = take_split(self.train_size, self.train_category, "train")
        self.val_dataset = take_split(self.val_size, self.val_category, "val")
        self.test_dataset = take_split(self.test_size, self.test_category, "test")

        self.train_loader = DataLoader(
            self.train_dataset, batch_size=1, shuffle=False, collate_fn=lambda b: b[0]
        )
        self.val_loader = DataLoader(
            self.val_dataset, batch_size=1, shuffle=False, collate_fn=lambda b: b[0]
        )
        self.test_loader = DataLoader(
            self.test_dataset, batch_size=1, shuffle=False, collate_fn=lambda b: b[0]
        )
