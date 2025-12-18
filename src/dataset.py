from torch.utils.data import Dataset
from data.generate_data import generate_dataset

class MarkedPointDataset(Dataset):
    def __init__(self, n_samples=5000):
        self.X, self.marked_idx, self.y = generate_dataset(n_samples)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return {
            "points": self.X[idx],
            "marked_idx": self.marked_idx[idx],
            "label": self.y[idx]
        }
