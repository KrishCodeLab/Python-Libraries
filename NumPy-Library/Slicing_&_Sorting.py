# Slicing in NumPy : Slicing means accessing sub part of sequence .

import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9,10])
print("Basic slicing : ",array[1:4])
print("With Step : ",array[0:8:2])
print("Negative indexing : ", array[-4])
print("Negative Slicing : ",array[-4:-1])