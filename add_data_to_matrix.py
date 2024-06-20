import numpy as np

def add_data_to_matrix(data_to_save, data_matrix):
    if len(data_matrix) == 0:
        data_matrix = data_to_save
        return data_matrix
    data_matrix = np.concatenate([data_matrix, data_to_save], axis=2)
    return data_matrix
