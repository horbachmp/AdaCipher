from datasets import load_dataset
from torch.utils.data import DataLoader


class HarmBenchDataset:
    def __init__(self, size, max_length=None, seed=0, category=None):
        self.size = size
        self.query_max_length = max_length
        self.seed = seed
        self.category = category

        data = load_dataset("walledai/HarmBench", "standard", split="train")
        self.data = data

        data = data.shuffle(seed=self.seed)
        texts = list(zip(data["prompt"], data["category"]))
        if self.category:
            categories = data["category"]
            texts = [(x, y) for x, y in texts if y == self.category]

        if len(texts) > self.size:
            texts = texts[:self.size]
        else:
            self.size = len(texts)
            print(f"Dataset is too small, only {len(texts)} samples available. Using reduced size.")

        

        filtered = [
            (x.strip(), y)
            for x,y in texts
            if isinstance(x, str) and len(x.strip()) > 10
        ]


        if self.query_max_length is not None:
            filtered = [(x[:self.query_max_length], y) for x,y in filtered]

        self.dataset = filtered
        self.loader = DataLoader(self.dataset, batch_size=1, shuffle=False, collate_fn=lambda batch: batch[0])
        self.categories = set([y for x,y in self.dataset])

