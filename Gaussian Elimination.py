import numpy as np
import numpy.linalg as ng
from scipy.linalg import lu

matrixGaus = np.array([[2, 2, 1, 7], [-1, 2, 0, 3], [3, 2, 1, 8], [4, 2, 0, 8]])

rowLenGauss = len(matrixGaus)
columnLenGaus = len(matrixGaus[0])

if columnLenGaus == rowLenGauss :
    print("square matrix")
    print(ng.linalg.matrix_rank(matrixGaus))
    matrixGausRank = lu(matrixGaus,permute_l=True )
    print(matrixGausRank)
    pl, rankNew = ng.linalg.matrix_rank(matrixGausRank)
    if rankNew == len(matrixGaus):
        print("its a full rank matrix")
    else:
        print("its not a full rank matrix")
else:
    print("not a square matrix")