import numpy as np

# Matriks awal
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Menghitung matriks invers
if np.linalg.det(matrix) != 0:
    inverse_matrix = np.linalg.inv(matrix)
    print("Matriks Invers:")
    print(inverse_matrix)
else:
      print("Matriks tidak memilik")
