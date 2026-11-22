# Filter : Filtering a NumPy array means extracting specific elements from an existing array to create a new array
import numpy as np

numbers=np.array([1,2,3,4,5,6,7,8,])
print(numbers)

# Even numbers using filter
even_numbers=numbers[numbers%2==0]
print("Even :",even_numbers)

# Odd numbers using filter
odd_numbers=numbers[numbers%2==1]
print("Odd : ", odd_numbers)


array=np.array([1,-3,-6,-3,5,7,-56,-99,45,78,-4,-1,44])
print(array)

# print positive numbers
positive_numbers=array[array > 0]
print("Positive : ",positive_numbers)

# print negative numbers
negative_numbers=array[array < 0]
print("Negative : ",negative_numbers)


# Mask : Condition used for filtering
mask=array > 0
print("Positive : ",array[mask])

mask=array < 0
print("Negative : ",array[mask])


# Fancy indexing vs np.where()
nums=np.array([1,2,3,4,5,6,7,8,9,10])
indices=[0,2,4,6]
print(nums[indices])

# 2D Array :
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

rows = [0, 1, 2]
cols = [2, 1, 0]

# Selects (0,2), (1,1), and (2,0)
print(matrix[rows, cols])
# Output: [3 5 7]



