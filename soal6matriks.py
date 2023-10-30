import numpy as np

# Membuat matriks 4x4
matrix_4x4 = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])

# Mengubah bentuk matriks menjadi 2x8
matrix_2x8 = matrix_4x4.reshape(2, 8)

# Menampilkan matriks hasil
print(matrix_2x8)