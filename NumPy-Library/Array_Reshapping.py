# Array Reshaping :
import numpy as np
arr=np.arange(12)
print("Original Array : ",arr)

# reshpaed method automatically arranges element in specified rows and columns
Reshaped=arr.reshape((3,4))
print("Reshaped Array : ",Reshaped)

# flattend method automatically rearrange elements in single dimension array.
Flattend=Reshaped.flatten()
print("Flattend array : ",Flattend)

# ravel method also converts multidimensional arrays into a 1D array, just like flatten()
Raveled=Reshaped.ravel()
print("Raveled array : ",Raveled)

# Transpose 
Transpose=Reshaped.T
print("Transpose array : ",Transpose)
