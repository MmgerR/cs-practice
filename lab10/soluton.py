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

def matrix_vector_product(matrix, vector):
    np_matrix = np.array(matrix)
    np_vector = np.array(vector)
    return (np_matrix @ np_vector).tolist()

def matrix_multiply(left, right):
    np_left = np.array(left)
    np_right = np.array(right)
    return (np_left @ np_right).tolist()
        
