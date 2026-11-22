# Adding and removing data
import numpy as np


# array concatanation combines two array.
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
combined=np.concatenate((arr1,arr2))
print(combined)

# array compatibility :
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([7,8])
print("Compatibility Shapes : ",a.shape ==b.shape)
print("Compatibilty Shapes : ",a.shape==c.shape)

