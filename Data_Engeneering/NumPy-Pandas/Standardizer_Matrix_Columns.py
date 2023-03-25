import numpy as np                                      

def mat_col_stand(matrix):
    stand_mtx = []

    for col in range(matrix.shape[1]):
        col_mean = np.mean(matrix[:, col])
        col_std = np.std(matrix[:, col])
        stand_mtx.append(list((matrix[:, col] - col_mean) / col_std))

    return list(np.transpose(stand_mtx))
  
mtx = np.array([[1,2], [3,4], [5,6]])                     #should i specifie = np.array() and why?
print(mat_col_stand(mtx))



def matrix_columns_standardizer(matrix):                     #standardizes each column of a matrix separately
    stand_matrix = []

    for column in list(zip(*matrix)):
        col_mean = np.mean(column)
        col_std = np.std(column)
        stand_matrix.append(list((column - col_mean) / col_std))

    return list(zip(*stand_matrix))

matrix = np.array([[1,2], [3,4], [5,6]])                     #should i specifie = np.array() and why?
stand_matrix = matrix_columns_standardizer(matrix)
print(stand_matrix)


