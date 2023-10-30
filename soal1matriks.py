import numpy as np
#penjumlahan dan pengulangan matrix
matriks1 = np.array([[1,2,3], [4,5,6] , [7,8,9]])


for x in range(0,len(matriks1)):
    for y in range(0,len(matriks1[0])):
        print(matriks1[x][y]+ matriks1[x][y])