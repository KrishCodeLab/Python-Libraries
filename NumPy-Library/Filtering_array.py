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