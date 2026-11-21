# Array Properties : shape,dimensions,size,datatype,itemsize,nbytes
import numpy as np
arr=np.array([[1,2,3,4,],
             [5,6,7,8]])

print("Shape of array : ",arr.shape)
print("Dimension of array : ",arr.ndim)
print("Size of array : ",arr.size)
print("Data type of array elements : ",arr.dtype)
print("Item size of array elements : ",arr.itemsize)
