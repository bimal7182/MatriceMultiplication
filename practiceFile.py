import numpy as np

matrixA = np.array([[1,2,3],[4,5,6],[7,8,9]])

#size of the matrix which gives dimension -row and column size
print(matrixA.shape)

#get specific element in a array
print(matrixA[1,1])

#get a specific row in matrix
print(matrixA[1,:])

#get specific row and elements/rows after the specific row
print(matrixA[0:])

#get all the columns in a specific column
print(matrixA[:,1])

#initializing Matrix/arrays
matrixB = np.zeros((4,4,4))
print(matrixB)
