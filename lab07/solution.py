import numpy as np

def reshape_rows(values, width):
    if len(values) % width != 0:
        return []
    return np.array(values).reshape(-1, width).tolist()

def block(matrix, rows, columns):
    arr = np.array(matrix, dtype=float)
    return arr[rows][:,columns].tolist()

def column_means(matrix):
    arr = np.array(matrix, dtype=float)
    if arr.size == 0:
        return []
    return (arr.sum(axis=0) / arr.shape[0]).tolist()

def column_range(matrix, column):
    arr = np.array(matrix, dtype=float)
    col = arr[:, column]
    return float(col.max() - col.min())
