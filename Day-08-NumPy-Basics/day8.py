import numpy as np

# Create Array
arr = np.array([10, 20, 30, 40])
print("Array:")
print(arr)

# Array Dimensions
print("\nDimensions:")
print(arr.ndim)

# Shape
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("\nShape:")
print(matrix.shape)

# Data Type
print("\nData Type:")
print(arr.dtype)

# Zeros
print("\nZeros Array:")
print(np.zeros((2, 3)))

# Ones
print("\nOnes Array:")
print(np.ones((2, 2)))

# Arange
print("\nArange:")
print(np.arange(1, 11))

# Linspace
print("\nLinspace:")
print(np.linspace(0, 10, 5))

# Reshape
print("\nReshape:")
numbers = np.arange(1, 13)
print(numbers.reshape(3, 4))
