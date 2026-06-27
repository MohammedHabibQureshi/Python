# Import Module
import math

print("Square Root:", math.sqrt(25))

# Import Specific Function
from math import factorial

print("Factorial:", factorial(5))

# Import with Alias
import numpy as np

numbers = np.array([1, 2, 3, 4])
print("NumPy Array:", numbers)

# Create Your Own Module
# calculator.py
# def add(a, b):
#     return a + b

# main.py
# import calculator
# print(calculator.add(10, 20))

# Write to a File
with open("sample.txt", "w") as file:
    file.write("Welcome to Python\n")

# Append to a File
with open("sample.txt", "a") as file:
    file.write("Learning File Handling")

# Read File
with open("sample.txt", "r") as file:
    print("\nFile Contents:")
    print(file.read())
