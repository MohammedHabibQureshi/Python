# Day 9: NumPy Operations

⬅️ Previous: [Day 8](../Day-08-NumPy-Basics/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 10](../Day-10-Pandas-Basics/README.md)

---

# 📌 Overview

NumPy provides powerful operations for accessing, modifying, and performing mathematical calculations on arrays. These operations are much faster than traditional Python lists because NumPy performs vectorized computations.

---

# 1. Array Indexing

## 📖 Definition

Array indexing is used to access a specific element from a NumPy array using its position.

## 🎯 Purpose

- Retrieve individual elements
- Modify values
- Access data efficiently

## 📝 Syntax

```python
array[index]
```

## 💻 Example

```python
import numpy as np

arr = np.array([10,20,30,40])

print(arr[2])
```

Output

```text
30
```

---

# 2. Array Slicing

## 📖 Definition

Array slicing extracts a portion of an array.

## 🎯 Purpose

Retrieve multiple elements at once.

## 📝 Syntax

```python
array[start:stop:step]
```

## 💻 Example

```python
arr = np.array([10,20,30,40,50])

print(arr[1:4])
```

Output

```text
[20 30 40]
```

---

# 3. Array Indexing (2D)

## 📖 Definition

Access elements from a two-dimensional array using row and column indices.

## 🎯 Purpose

Retrieve data from matrices and tables.

## 📝 Syntax

```python
array[row, column]
```

## 💻 Example

```python
matrix = np.array([
    [10,20,30],
    [40,50,60]
])

print(matrix[1,2])
```

Output

```text
60
```

---

# 4. Mathematical Operations

## 📖 Definition

NumPy performs element-wise mathematical operations on arrays.

## 🎯 Purpose

Perform calculations efficiently.

## 📝 Syntax

```python
array + value
array - value
array * value
array / value
```

## 💻 Example

```python
arr = np.array([10,20,30])

print(arr + 5)
print(arr * 2)
```

Output

```text
[15 25 35]

[20 40 60]
```

---

# 5. Array Addition

## 📖 Definition

Adds corresponding elements of two arrays.

## 🎯 Purpose

Combine numerical datasets.

## 📝 Syntax

```python
array1 + array2
```

## 💻 Example

```python
a = np.array([1,2,3])

b = np.array([4,5,6])

print(a + b)
```

Output

```text
[5 7 9]
```

---

# 6. Array Multiplication

## 📖 Definition

Multiplies corresponding elements of two arrays.

## 🎯 Purpose

Perform element-wise multiplication.

## 📝 Syntax

```python
array1 * array2
```

## 💻 Example

```python
a = np.array([1,2,3])

b = np.array([4,5,6])

print(a * b)
```

Output

```text
[4 10 18]
```

---

# 7. Broadcasting

## 📖 Definition

Broadcasting allows NumPy to perform operations between arrays of different shapes.

## 🎯 Purpose

Avoid writing loops for mathematical operations.

## 📝 Syntax

```python
array + value
```

## 💻 Example

```python
arr = np.array([10,20,30])

print(arr + 100)
```

Output

```text
[110 120 130]
```

---

# 8. Aggregate Functions

## 📖 Definition

Aggregate functions perform calculations on an entire array.

## 🎯 Purpose

Summarize numerical data.

## 📝 Syntax

```python
np.function(array)
```

## 💻 Example

```python
arr = np.array([10,20,30,40])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
```

Output

```text
100
25.0
40
10
```

---

# 9. Mean

## 📖 Definition

Returns the average value of the array.

## 🎯 Purpose

Measure the central value of data.

## 📝 Syntax

```python
np.mean(array)
```

## 💻 Example

```python
marks = np.array([75,80,90,85])

print(np.mean(marks))
```

Output

```text
82.5
```

---

# 10. Standard Deviation

## 📖 Definition

Measures how spread out the values are from the mean.

## 🎯 Purpose

Analyze variation in data.

## 📝 Syntax

```python
np.std(array)
```

## 💻 Example

```python
marks = np.array([75,80,90,85])

print(np.std(marks))
```

---

# 🌍 Real-World Use Case

Suppose a company records monthly sales.

```python
sales = np.array([12000,15000,18000,20000])
```

Using NumPy you can:

- Calculate total sales
- Find average monthly sales
- Identify the highest and lowest sales
- Increase all sales by 10% using broadcasting

Example

```python
updated_sales = sales * 1.10
```

---

# ⚠️ Common Mistakes

### ❌ Using Python loops for calculations

```python
numbers = [10,20,30]

result = []

for num in numbers:
    result.append(num + 10)
```

### ✅ Better Practice

```python
numbers = np.array([10,20,30])

print(numbers + 10)
```

---

# 💼 Interview Questions

## Q1. What is Broadcasting?

**Answer**

Broadcasting is a NumPy feature that allows arrays of different shapes to perform arithmetic operations without manually resizing them.

---

## Q2. Difference between Python Lists and NumPy Arrays?

| Python List | NumPy Array |
|-------------|-------------|
| Slower | Faster |
| Stores mixed data types | Stores homogeneous data |
| Limited mathematical operations | Supports vectorized operations |

---

## Q3. Why are NumPy arrays faster?

**Answer**

- Contiguous memory allocation
- Implemented in C
- Vectorized operations
- Optimized numerical computations

---

# ✅ Summary

Today you learned:

- Array Indexing
- Array Slicing
- 2D Array Indexing
- Mathematical Operations
- Array Addition
- Array Multiplication
- Broadcasting
- Aggregate Functions
- Mean
- Standard Deviation

These operations make NumPy a powerful library for handling numerical data efficiently and form the foundation for data analysis and machine learning.
