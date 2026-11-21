# Creating array from scratch :

import numpy as np
# zeros array : 
zeros=np.zeros((3,4))
print("Zeros array : \n",zeros)

# ones array :
ones=np.ones((4,4))
print("Ones array : \n",ones)


# full array :
full = np.full((2,2),7)
print("Full array : \n",full)

# random array :
random=np.random.random((2,3))
print("Random array : \n",random)

# sequence array :
sequence=np.arange(0,11,2)
print(sequence)

# Defined data type of array :
arr=np.array([1,2,3,4,5],dtype=np.float32)
print(arr)
print(arr.dtype)


# Type conversion using astype() 
# Suppose you have a flat array and want to convert it into integers.
arr=np.array([10.5,44,5,30.99])
new_arr=arr.astype(int)
print(new_arr)