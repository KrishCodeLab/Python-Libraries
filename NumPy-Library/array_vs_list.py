# What is difference between array and list :
# array is collection of similar data types Homogeneous , while list is collection of similar as well as different data types Heterogeneous.
# array's size is fixed but list's size is dynamic.
# Elements stored in contegious memory side by side , in list elements stored in no contegious memory
# Array is useful for faster mathemathical calculations and list is useful for resizing.

import numpy as np

# python list
py_list=[1,2,3]
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(py_list * 3) #---> Here list will print 3 times 

np_array=np.array([1,2,3])
# [3 6 9]
print(np_array * 3) #---> Here all elements of array will multiplied by 3


# perform addition
print(np_array + 10) # ---> Adds 10 in all elements of array


# Array performs operation in very less time rather than list
import time
start=time.time()
py_list=[i * 2 for i in range(100000)]
print("List operation time : ",time.time()-start)

start=time.time()
np_array=np.array([i*2 for i in range(100000)])
print("Array operation time : ",time.time()-start)
