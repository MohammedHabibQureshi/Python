# Day 8: NumPy Basics

⬅️ Previous: [Day 7](../Day-07-Exception-Handling/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 9](../Day-09-NumPy-Operations/README.md)

---

# 📌 Overview

NumPy (Numerical Python) is a powerful Python library used for numerical computing. It provides a high-performance multidimensional array object along with tools to perform mathematical and statistical operations efficiently.

NumPy is the foundation of many Data Science and Machine Learning libraries such as Pandas, SciPy, Scikit-learn, TensorFlow, and PyTorch.

---

# Why NumPy?

Python lists are flexible but slow for numerical computations.

NumPy arrays are:

- Faster
- Memory efficient
- Easy to perform mathematical operations
- Optimized for large datasets

---

# 1. Import NumPy

## 📖 Definition

Before using NumPy, you need to import the library.

## 🎯 Purpose

Allows access to NumPy functions and methods.

## 📝 Syntax

```python
import numpy as np
```

## 💻 Example

```python
import numpy as np

print(np.__version__)
```

---

# 2. Create NumPy Array

## 📖 Definition

A NumPy array is a collection of elements stored in contiguous memory.

## 🎯 Purpose

Store numerical data efficiently.

## 📝 Syntax

```python
np.array(iterable)
```

## 💻 Example

```python
import numpy as np

arr = np.array([10,20,30,40])

print(arr)
```

Output

```text
[10 20 30 40]
```

---

# 3. Array Dimensions

## 📖 Definition

The `ndim` attribute returns the number of dimensions of an array.

## 🎯 Purpose

Determine whether an array is 1D, 2D, or higher.

## 📝 Syntax

```python
array.ndim
```

## 💻 Example

```python
arr = np.array([[1,2],[3,4]])

print(arr.ndim)
```

Output

```text
2
```

---

# 4. Array Shape

## 📖 Definition

The `shape` attribute returns the number of rows and columns.

## 🎯 Purpose

Know the structure of the array.

## 📝 Syntax

```python
array.shape
```

## 💻 Example

```python
arr = np.array([[1,2,3],
                [4,5,6]])

print(arr.shape)
```

Output

```text
(2, 3)
```

---

# 5. Array Data Type

## 📖 Definition

The `dtype` attribute returns the data type of array elements.

## 🎯 Purpose

Identify how data is stored.

## 📝 Syntax

```python
array.dtype
```

## 💻 Example

```python
arr = np.array([1,2,3])

print(arr.dtype)
```

Output

```text
int64
```

---

# 6. zeros()

## 📖 Definition

Creates an array filled with zeros.

## 🎯 Purpose

Initialize arrays before assigning values.

## 📝 Syntax

```python
np.zeros(shape)
```

## 💻 Example

```python
arr = np.zeros((2,3))

print(arr)
```

Output

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

---

# 7. ones()

## 📖 Definition

Creates an array filled with ones.

## 🎯 Purpose

Initialize arrays with default values.

## 📝 Syntax

```python
np.ones(shape)
```

## 💻 Example

```python
arr = np.ones((2,2))

print(arr)
```

Output

```text
[[1. 1.]
 [1. 1.]]
```

---

# 8. arange()

## 📖 Definition

Creates an array with evenly spaced values.

## 🎯 Purpose

Generate sequences of numbers.

## 📝 Syntax

```python
np.arange(start, stop, step)
```

## 💻 Example

```python
arr = np.arange(1,11)

print(arr)
```

Output

```text
[1 2 3 4 5 6 7 8 9 10]
```

---

# 9. linspace()

## 📖 Definition

Creates evenly spaced values between two numbers.

## 🎯 Purpose

Generate equally spaced values.

## 📝 Syntax

```python
np.linspace(start, stop, number_of_values)
```

## 💻 Example

```python
arr = np.linspace(0,10,5)

print(arr)
```

Output

```text
[0.  2.5 5.  7.5 10.]
```

---

# 10. reshape()

## 📖 Definition

Changes the shape of an array without changing its data.

## 🎯 Purpose

Convert arrays into different dimensions.

## 📝 Syntax

```python
array.reshape(rows, columns)
```

## 💻 Example

```python
arr = np.arange(1,13)

matrix = arr.reshape(3,4)

print(matrix)
```

Output

```text
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
```

---

# 🌍 Real-World Use Case

Suppose you have temperature readings collected every hour.

```python
temperatures = np.array([30,31,29,28,32,34,35])
```

Using NumPy, you can efficiently:

- Calculate the average temperature.
- Find the maximum and minimum values.
- Apply mathematical operations to the entire dataset.
- Prepare data for Machine Learning models.

---

# ⚠️ Common Mistakes

### ❌ Creating arrays using Python lists for heavy calculations

```python
numbers = [1,2,3,4]
```

### ✅ Better Practice

```python
numbers = np.array([1,2,3,4])
```

NumPy arrays are significantly faster than Python lists for numerical operations.

---

# 💼 Interview Questions

## Q1. What is NumPy?

**Answer**

NumPy is a Python library used for numerical computing. It provides fast multidimensional arrays and mathematical functions.

---

## Q2. Why is NumPy faster than Python lists?

**Answer**

- Stores homogeneous data.
- Uses contiguous memory allocation.
- Optimized using C language internally.
- Supports vectorized operations.

---

## Q3. Difference between `arange()` and `linspace()`?

| arange() | linspace() |
|----------|------------|
| Uses step size | Uses number of values |
| Stop value may not be included | Includes stop value by default |

---

# ✅ Summary

Today you learned:

- Import NumPy
- NumPy Arrays
- Array Dimensions (`ndim`)
- Array Shape (`shape`)
- Array Data Type (`dtype`)
- `zeros()`
- `ones()`
- `arange()`
- `linspace()`
- `reshape()`

These are the fundamental concepts of NumPy and form the basis for efficient numerical computing in Python.
