# Linear Algebra : Machine learning uses vectors,matrices and mathematical operation extensively.

import numpy as np

# Matric Multiplication : 
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

result=np.dot(a,b)
# Matrix multiplication 
print(result)
print(a@b)

# Element wise multiplication
print(a*b)

# Transpose : Converts rows into columns and columns into rows.
arr=np.array([[1,2,3],
              [4,5,6]])

print(arr.T)

# Determinant : 
arr=np.array([[1,2],[3,4]])
print(np.linalg.det(arr))

# Inverse of matrix : Calculates the inverse if the matrix is invertible
print(np.linalg.inv(arr))

# Solving linear equations :
# 2x + y = 5
# x + 3y = 6

# Use Numpy : 
A=np.array([[2,3],[4,5]])
B=np.array([6,7])
solution= np.linalg.solve(A,B)
print(solution)
