from torch.utils.data import DataLoader
import os

class RandomDataset:
    def __init__(self, size, max_length, dataset_path):
        self.size = size
        self.query_max_length = max_length
        self.dataset_path = dataset_path
        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(f"Dataset file {self.dataset_path} not found")

        with open(self.dataset_path, "r") as f:
            lines = f.readlines()
        if self.size == "None":
            self.size = len(lines)
        self.dataset = lines[:self.size]

        if self.query_max_length is not None:
            self.dataset = [x[:self.query_max_length] for x in self.dataset]

        self.loader = DataLoader(self.dataset, batch_size=1, shuffle=False)
