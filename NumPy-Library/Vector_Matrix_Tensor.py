import numpy as np
# Vector (1D / Rank 1): An ordered array of values that can represent magnitude and direction in space or a list of features for one item. Example: [3, 4] or a single movie's feature list.
vector=np.array([1,2,3])
print("=======Vector======")
print(vector)

# Matrix (2D / Rank 2): A rectangular grid of m rows and n columns often used for tables, linear transformations, or grayscale images. Example: a 3 × 3 grid of numbers
matrix=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print("=======Matrix======")

print(matrix)

# Tensor (Multi-dimensional / Rank n): A generalized array across multiple axes. In deep learning, a 3D tensor can represent an RGB image (height, width, color channels), while 4D or 5D tensors represent batches of images or videos
tensor=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print("=======Tensor======")

print(tensor)
