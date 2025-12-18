import numpy as np
import torch

def generate_sample(n_points=10):
    points = np.random.randn(n_points, 2)

    marked_point = points[0]
    centroid = points.mean(axis=0)

    label = int(marked_point[1] > centroid[1])

    perm = np.random.permutation(n_points)
    points = points[perm]
    marked_index = np.where(perm == 0)[0][0]

    return points.astype(np.float32), marked_index, label


def generate_dataset(n_samples=5000):
    X, idxs, y = [], [], []
    for _ in range(n_samples):
        pts, idx, label = generate_sample()
        X.append(pts)
        idxs.append(idx)
        y.append(label)

    return (
        torch.tensor(X),
        torch.tensor(idxs),
        torch.tensor(y)
    )


if __name__ == "__main__":
    X, idxs, y = generate_dataset(1000)
    print(X.shape, idxs.shape, y.float().mean())
