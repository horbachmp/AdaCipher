from datasets import load_dataset
from torch.utils.data import DataLoader
import random


# alpaca is a benign dataset: the category is the same for every prompt
BENIGN_CATEGORY = "benign"


class AlpacaSplitDataset:
    def __init__(
        self,
        train_size,
        val_size,
        test_size,
        max_length=None,
        seed=0
    ):
        self.train_size = train_size
        self.val_size = val_size
        self.test_size = test_size
        self.query_max_length = max_length
        self.seed = seed

        # load the raw json file instead of the dataset script
        data = load_dataset(
            "json",
            data_files="hf://datasets/tatsu-lab/alpaca_eval/alpaca_eval.json",
            split="train",
        )

        texts = [
            (prompt.strip(), BENIGN_CATEGORY)
            for prompt in data["instruction"]
            if isinstance(prompt, str) and len(prompt.strip()) > 10
        ]

        rng = random.Random(self.seed)
        rng.shuffle(texts)

        used = set()

        def take_split(size, split_name):

            candidates = [i for i, _ in enumerate(texts) if i not in used]

            selected_idx = candidates[:size]

            if len(selected_idx) < size:
                print(
                    f"[{split_name}] Requested {size}, got {len(selected_idx)}. "
                    f"Not enough samples left in the dataset."
                )

            for i in selected_idx:
                used.add(i)

            split = [texts[i] for i in selected_idx]

            if self.query_max_length is not None:
                split = [(x[:self.query_max_length], y) for x, y in split]

            return split

        self.train_dataset = take_split(self.train_size, "train")
        self.val_dataset = take_split(self.val_size, "val")
        self.test_dataset = take_split(self.test_size, "test")

        self.train_loader = DataLoader(
            self.train_dataset, batch_size=1, shuffle=False, collate_fn=lambda b: b[0]
        )
        self.val_loader = DataLoader(
            self.val_dataset, batch_size=1, shuffle=False, collate_fn=lambda b: b[0]
        )
        self.test_loader = DataLoader(
            self.test_dataset, batch_size=1, shuffle=False, collate_fn=lambda b: b[0]
        )
