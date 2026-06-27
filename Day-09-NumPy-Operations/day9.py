import numpy as np

# Create Arrays
arr = np.array([10, 20, 30, 40, 50])

# Indexing
print("Indexing:")
print(arr[2])

# Slicing
print("\nSlicing:")
print(arr[1:4])

# 2D Array Indexing
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n2D Indexing:")
print(matrix[1, 2])

# Mathematical Operations
print("\nAdd 5:")
print(arr + 5)

print("\nMultiply by 2:")
print(arr * 2)

# Array Addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nArray Addition:")
print(a + b)

# Array Multiplication
print("\nArray Multiplication:")
print(a * b)

# Broadcasting
print("\nBroadcasting:")
print(arr + 100)

# Aggregate Functions
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Standard Deviation
marks = np.array([75, 80, 90, 85])

print("\nAverage Marks:", np.mean(marks))
print("Standard Deviation:", np.std(marks))
