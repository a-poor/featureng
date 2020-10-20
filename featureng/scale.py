
import numpy as np


def min_max_scale(data: np.ndarray):
    min_, max_ = np.min(data), np.max(data)
    return (data - min_) / (max_ - min_)

def standardize(data: np.ndarray):
    mean = np.mean(data)
    std = np.std(data)
    return (data - mean) / std

def l2_norm(data: np.ndarray):
    mag = np.sqrt(np.sum(data * data))
    return data / mag
