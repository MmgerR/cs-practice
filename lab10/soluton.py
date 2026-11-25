import numpy as np

def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr = np.array(matrix)
    return arr[row_start:row_stop, column_start]

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    result = np.array(matrix, copy=True)
    result[row_start:row_stop, column_start:column_stop] = value
    return result.tolist()
