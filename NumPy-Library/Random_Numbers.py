# Random numbers are useful for simulations,experiments and ML training.
# User random generate API :
import numpy as np

# 1D array of 5 floats

rng=np.random.default_rng()
print(rng)

arr_1d = rng.random(5)
print(arr_1d)

# 2D array (3 rows, 4 columns)
arr_2d = rng.random((3, 4))
print(arr_2d)

# Generate random numbers from 1 to 100
print(rng.integers(1,101))

# Generate random numbers matrix
print(rng.integers(1,101,size=(3,3)))

# Normal Distribution : 
# Generate five random numbers from normal distribution with mean 0 and standard deviation 1.
print(rng.normal(loc=0,scale=1,size=5))
