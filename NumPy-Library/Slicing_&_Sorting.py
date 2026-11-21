# Slicing in NumPy : Slicing means accessing sub part of sequence .

import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9,10])
print("Basic slicing : ",array[1:4])
print("With Step : ",array[0:8:2])
print("Negative indexing : ", array[-4])
print("Negative Slicing : ",array[-4:-1])

# Sorting : Sorting is method of arranging all elements of sequence in ascending or decsending order.
unsorted=np.array([3,5,9,2,1,0,4,6])
print("Sorted array : ")
print(np.sort(unsorted))
# Storing sorted array
sorted=np.sort(unsorted)
print(sorted)

# 2D array sorting :
unsorted=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Sorted 2D array : ")
print(np.sort(unsorted))


# Sorting 2D array axis wise
# Column wise means axis=0 --->To sort columns from left to right.
# Rows wise means axis=1 ---->To sort rows from top to bottom.

array_2d_unsorted=np.sort(unsorted,axis=0)
print("Array sorted by columns : ",array_2d_unsorted)

array_2d_unsorted=np.sort(unsorted,axis=1)
print("Array sorted by rows : ",array_2d_unsorted)


