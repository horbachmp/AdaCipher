from datasets import load_dataset
from torch.utils.data import DataLoader


class AlpacaDataset:
    def __init__(self, size, max_length, seed=0):
        self.size = size
        self.query_max_length = max_length
        self.seed = seed

        # load the raw json file instead of the dataset script
        data = load_dataset(
            "json",
            data_files="hf://datasets/tatsu-lab/alpaca_eval/alpaca_eval.json",
            split="train",
        )

        data = data.shuffle(seed=self.seed).select(range(min(self.size, len(data))))
        texts = data["instruction"]

        filtered = [
            x.strip()
            for x in texts
            if isinstance(x, str) and len(x.strip()) > 10
        ]

        if self.query_max_length is not None:
            filtered = [x[:self.query_max_length] for x in filtered]

        self.dataset = filtered
        self.loader = DataLoader(self.dataset, batch_size=1, shuffle=False)
        self.test_loader = DataLoader(self.dataset, batch_size=1, shuffle=False)
