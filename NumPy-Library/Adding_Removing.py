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

# Adding row in array :
original = np.array([[1,2],[3,4],[5,6]])
new_row=np.array([[7,8]])
with_new_row=np.vstack((original,new_row))
print(with_new_row)

# Adding column in array :
new_col=np.array([[8],[9],[10],[11]])
with_new_col=np.hstack((with_new_row,new_col))
print(with_new_col)