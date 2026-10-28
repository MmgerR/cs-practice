import numpy as np

def reshape_rows(values, width):
    if len(values) % width != 0:
        return []
    return np.array(values).reshape(-1, width).tolist()

