import numpy as np
import scipy as sp

mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[1, 3], [7, 5]])
mat3 = np.dot(mat1, mat2)
det = sp.linalg.det(mat3)
print("Определитель матрицы равен {:.2f}".format(det))
