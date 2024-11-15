import numpy as np

def analyze_data(data):
    return {
        "mean": np.mean(data),
        "median": np.median(data),
        "std_dev": np.std(data)
    }
