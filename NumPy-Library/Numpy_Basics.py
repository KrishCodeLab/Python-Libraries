# What is numpy : Numpy is used to work with numerical values while working on ML , AI etc
# NumPy : Numerical Python
# NumPy (Numerical Python) is an open-source Python library for fast numerical and scientific computing, centered on multi-dimensional arrays (ndarray) and high-level mathematical functions
import numpy as np
print(np)

# What is array : Array is collection of elements with similar data type in contegious memory.
# Creating array using list and numpy array 

arr=np.array([1,2,3,4,5])
print(arr)
# We used list to pass values to the array method because array method recieves only one argument

# What is one dimensional array and two dimensional array :

# one dimensional : Simple or by default array
arr_1d=np.array([1,2,3,4,5,6,7,8,9,10])
print("One Dimensional Array : ")
print(arr_1d)

# Two dimensional : Array with rows and columns like matrix
arr_2d=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print("Two Dimensional Array : ")
print(arr_2d)


