# Indexing in NumPy : Indexing means accessing individual elements from an array.

import numpy as np

# 1D array indexing : array's indexing starts from 0 similarly like list , tuple etc

arr=np.array([10,20,30,40,50])
print("Positive Indexing : ")
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

# Numpy also supports negative indexing just like python list.
print("Negative Indexing : ")
print(arr[-1])
print(arr[-2])
print(arr[-3])
print(arr[-4])
print(arr[-5])

# 2D array indexing : 
array=np.array([
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [10,11,12]
])
print(array)
print("2D Array Indexing : ")
print(array[0,0])
print(array[1,2])
print(array[0,1])
print(array[3,2])

# Accessing entire row :
print(array[0])

# Accessing entire column :
print(array[:,1])
# The : colon means selecting all elements along that axis.


