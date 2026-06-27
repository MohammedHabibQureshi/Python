# Day 3: Dictionaries

⬅️ Previous: [Day 2](../Day-02-Lists-Tuples-Sets/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 4](../Day-04-Conditionals-Loops/README.md)

---

# 📌 Overview

A Dictionary is one of Python's most powerful built-in data structures. It stores data as **key-value pairs**, allowing fast retrieval, updates, and management of information.

Dictionaries are widely used in **Data Analysis, Machine Learning, APIs, JSON data, databases, and configuration files**.

---

# 1. Create Dictionary

## 📖 Definition

A Dictionary is a mutable collection that stores data in **key-value pairs**. Each key must be unique, while values can be duplicated.

## 🎯 Purpose

- Store structured data
- Fast data lookup
- Easy data modification
- Represent real-world objects

## 📝 Syntax

```python
dictionary_name = {
    "key1": value1,
    "key2": value2
}
```

## 💻 Example

```python
employee = {
    "name": "John",
    "age": 30,
    "department": "Sales"
}

print(employee)
```

Output

```text
{'name': 'John', 'age': 30, 'department': 'Sales'}
```

---

# 2. Access Dictionary Values

## 📖 Definition

Dictionary values can be accessed using their corresponding key.

## 🎯 Purpose

Retrieve specific information from a dictionary.

## 📝 Syntax

```python
dictionary[key]
```

## 💻 Example

```python
employee = {
    "name": "John",
    "age": 30
}

print(employee["name"])
```

Output

```text
John
```

---

# 3. Safe Access using get()

## 📖 Definition

The `get()` method retrieves a value without causing an error if the key does not exist.

## 🎯 Purpose

Safely access dictionary values.

## 📝 Syntax

```python
dictionary.get(key, default_value)
```

## 💻 Example

```python
employee = {
    "name": "John",
    "age": 30
}

print(employee.get("salary", 0))
```

Output

```text
0
```

---

# 4. Add or Update Keys

## 📖 Definition

Assigning a value to a new key adds it to the dictionary. Assigning to an existing key updates its value.

## 🎯 Purpose

Insert or modify dictionary data.

## 📝 Syntax

```python
dictionary["key"] = value
```

## 💻 Example

```python
employee = {
    "name": "John"
}

employee["salary"] = 75000

print(employee)
```

Output

```text
{'name': 'John', 'salary': 75000}
```

---

# 5. Delete Keys

## 📖 Definition

The `del` keyword removes a key-value pair from a dictionary.

## 🎯 Purpose

Delete unnecessary information.

## 📝 Syntax

```python
del dictionary["key"]
```

## 💻 Example

```python
employee = {
    "name": "John",
    "age": 30
}

del employee["age"]

print(employee)
```

Output

```text
{'name': 'John'}
```

---

# 6. keys()

## 📖 Definition

Returns all keys present in the dictionary.

## 🎯 Purpose

View available fields in a dictionary.

## 📝 Syntax

```python
dictionary.keys()
```

## 💻 Example

```python
employee = {
    "name": "John",
    "age": 30
}

print(employee.keys())
```

Output

```text
dict_keys(['name', 'age'])
```

---

# 7. values()

## 📖 Definition

Returns all values stored in the dictionary.

## 🎯 Purpose

Retrieve all stored data.

## 📝 Syntax

```python
dictionary.values()
```

## 💻 Example

```python
employee = {
    "name": "John",
    "age": 30
}

print(employee.values())
```

Output

```text
dict_values(['John', 30])
```

---

# 8. items()

## 📖 Definition

Returns both keys and values as tuples.

## 🎯 Purpose

Iterate through complete dictionary entries.

## 📝 Syntax

```python
dictionary.items()
```

## 💻 Example

```python
employee = {
    "name": "John",
    "age": 30
}

print(employee.items())
```

Output

```text
dict_items([('name', 'John'), ('age', 30)])
```

---

# 9. Dictionary Comprehension

## 📖 Definition

Dictionary Comprehension creates dictionaries using a concise syntax similar to list comprehension.

## 🎯 Purpose

Generate dictionaries efficiently.

## 📝 Syntax

```python
{key_expression: value_expression for item in iterable}
```

## 💻 Example

```python
prices = {
    "Apple": 100,
    "Orange": 80,
    "Banana": 50
}

discount = {
    k: v * 0.9
    for k, v in prices.items()
}

print(discount)
```

Output

```text
{'Apple': 90.0, 'Orange': 72.0, 'Banana': 45.0}
```

---

# 10. Nested Dictionary

## 📖 Definition

A Nested Dictionary is a dictionary that contains another dictionary as its value.

## 🎯 Purpose

Store hierarchical or structured information.

## 📝 Syntax

```python
dictionary = {
    key: {
        nested_key: value
    }
}
```

## 💻 Example

```python
students = {
    "student1": {
        "name": "John",
        "score": 92
    }
}

print(students)
```

Output

```text
{'student1': {'name': 'John', 'score': 92}}
```

---

# ✅ Summary

In Day 3, you learned:

- Create Dictionary
- Access Dictionary Values
- get()
- Add Keys
- Update Keys
- Delete Keys
- keys()
- values()
- items()
- Dictionary Comprehension
- Nested Dictionary

These concepts are essential for storing and manipulating structured data in Python and form the foundation for working with JSON, APIs, and datasets in data analysis.
