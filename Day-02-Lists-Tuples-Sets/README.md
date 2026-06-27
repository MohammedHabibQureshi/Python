# Day 2: Lists, Tuples & Sets

## 📌 Overview

In Day 2, you'll learn Python's built-in data structures used to store collections of data. Lists are mutable and ordered, tuples are immutable and ordered, and sets store unique unordered values. These data structures are widely used in Data Analysis, Machine Learning, and Python programming.

---

# 1. List

## 📖 Definition

A List is an ordered, mutable (changeable) collection of items. It can store different data types in a single collection.

## 🎯 Purpose

- Store multiple values
- Modify existing data
- Iterate through items
- Perform data manipulation

## 📝 Syntax

```python
list_name = [item1, item2, item3]
```

## 💻 Example

```python
scores = [85, 92, 78, 95, 88]

print(scores)
```

---

# 2. Access List Items

## 📖 Definition

List items can be accessed using their index. Python indexing starts from 0.

## 🎯 Purpose

Retrieve a specific element from the list.

## 📝 Syntax

```python
list_name[index]
```

## 💻 Example

```python
scores = [85, 92, 78, 95, 88]

print(scores[0])
print(scores[3])
```

Output

```text
85
95
```

---

# 3. List Slicing

## 📖 Definition

Slicing retrieves a portion of the list using a range of indices.

## 🎯 Purpose

Extract multiple elements from a list.

## 📝 Syntax

```python
list_name[start:end]
```

## 💻 Example

```python
scores = [85, 92, 78, 95, 88]

print(scores[1:4])
```

Output

```text
[92, 78, 95]
```

---

# 4. Append()

## 📖 Definition

The `append()` method adds a new element to the end of the list.

## 🎯 Purpose

Insert new data into a list.

## 📝 Syntax

```python
list_name.append(value)
```

## 💻 Example

```python
scores = [85, 92, 78]

scores.append(91)

print(scores)
```

Output

```text
[85, 92, 78, 91]
```

---

# 5. Remove()

## 📖 Definition

The `remove()` method removes the first occurrence of a specified value.

## 🎯 Purpose

Delete unwanted elements from a list.

## 📝 Syntax

```python
list_name.remove(value)
```

## 💻 Example

```python
scores = [85, 92, 78, 95]

scores.remove(78)

print(scores)
```

---

# 6. Sort()

## 📖 Definition

The `sort()` method arranges list elements in ascending order by default.

## 🎯 Purpose

Organize data for searching and analysis.

## 📝 Syntax

```python
list_name.sort()
```

## 💻 Example

```python
scores = [92, 85, 95, 78]

scores.sort()

print(scores)
```

Output

```text
[78, 85, 92, 95]
```

---

# 7. len()

## 📖 Definition

The `len()` function returns the total number of elements in a list.

## 🎯 Purpose

Find the size of a collection.

## 📝 Syntax

```python
len(list_name)
```

## 💻 Example

```python
scores = [85, 92, 78, 95]

print(len(scores))
```

Output

```text
4
```

---

# 8. List Comprehension

## 📖 Definition

List Comprehension provides a concise way to create new lists from existing iterables.

## 🎯 Purpose

Write cleaner and faster Python code.

## 📝 Syntax

```python
[new_expression for item in iterable]
```

## 💻 Example

```python
numbers = [1,2,3,4,5]

square = [x**2 for x in numbers]

print(square)
```

Output

```text
[1, 4, 9, 16, 25]
```

---

# 9. Conditional List Comprehension

## 📖 Definition

Conditional List Comprehension filters elements while creating a new list.

## 🎯 Purpose

Extract only matching values.

## 📝 Syntax

```python
[expression for item in iterable if condition]
```

## 💻 Example

```python
scores = [85,92,78,95,88]

high_scores = [x for x in scores if x > 85]

print(high_scores)
```

Output

```text
[92, 95, 88]
```

---

# 10. Tuple

## 📖 Definition

A Tuple is an ordered and immutable collection of elements.

## 🎯 Purpose

Store data that should not be modified.

## 📝 Syntax

```python
tuple_name = (item1, item2, item3)
```

## 💻 Example

```python
coordinates = (10.5, 20.3)

print(coordinates)
```

---

# 11. Set

## 📖 Definition

A Set is an unordered collection of unique elements.

## 🎯 Purpose

Remove duplicate values and perform mathematical set operations.

## 📝 Syntax

```python
set_name = {value1, value2, value3}
```

## 💻 Example

```python
numbers = {1,2,2,3,3,4}

print(numbers)
```

Output

```text
{1,2,3,4}
```

---

# 12. Set Operations

## 📖 Definition

Python provides methods to perform union, intersection, and difference between sets.

## 🎯 Purpose

Compare datasets and find common or unique values.

## 📝 Syntax

```python
A.union(B)

A.intersection(B)

A.difference(B)
```

## 💻 Example

```python
A = {1,2,3}

B = {3,4,5}

print(A.union(B))

print(A.intersection(B))

print(A.difference(B))
```

Output

```text
{1,2,3,4,5}

{3}

{1,2}
```

---

# ✅ Summary

In Day 2, you learned:

- Lists
- Accessing List Elements
- List Slicing
- append()
- remove()
- sort()
- len()
- List Comprehension
- Conditional List Comprehension
- Tuples
- Sets
- Set Operations

These data structures are fundamental in Python and are heavily used in Data Analysis for storing, filtering, and processing datasets.
