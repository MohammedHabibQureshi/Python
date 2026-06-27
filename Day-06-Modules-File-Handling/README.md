# Day 6: Modules & File Handling

⬅️ Previous: [Day 5](../Day-05-Functions/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 7](../Day-07-Exception-Handling/README.md)

---

# 📌 Overview

As Python programs grow larger, organizing code becomes essential. Modules allow you to divide code into separate files, making it reusable and easier to maintain. File handling enables Python to create, read, update, and delete files, making it useful for storing and processing data.

---

# 1. Modules

## 📖 Definition

A Module is a Python file (`.py`) that contains functions, classes, and variables which can be imported into another Python program.

## 🎯 Purpose

- Organize code
- Reuse code
- Improve readability
- Reduce duplication

## 📝 Syntax

```python
import module_name
```

## 💻 Example

```python
import math

print(math.sqrt(25))
```

Output

```text
5.0
```

---

# 2. Import Specific Functions

## 📖 Definition

Instead of importing an entire module, you can import only the required functions.

## 🎯 Purpose

Reduce unnecessary code and improve readability.

## 📝 Syntax

```python
from module_name import function_name
```

## 💻 Example

```python
from math import sqrt

print(sqrt(49))
```

Output

```text
7.0
```

---

# 3. Import with Alias

## 📖 Definition

An alias gives a module or function a shorter name.

## 🎯 Purpose

Make code shorter and easier to read.

## 📝 Syntax

```python
import module_name as alias
```

## 💻 Example

```python
import numpy as np

numbers = np.array([1,2,3])

print(numbers)
```

Output

```text
[1 2 3]
```

---

# 4. Create Your Own Module

## 📖 Definition

You can create your own module by saving Python code in a `.py` file.

## 🎯 Purpose

Reuse your own functions across multiple projects.

## 📝 Syntax

```python
# module.py

def function_name():
    pass
```

```python
# main.py

import module
```

## 💻 Example

**calculator.py**

```python
def add(a, b):
    return a + b
```

**main.py**

```python
import calculator

print(calculator.add(10, 20))
```

Output

```text
30
```

---

# 5. File Handling

## 📖 Definition

File Handling is the process of creating, reading, writing, and modifying files using Python.

## 🎯 Purpose

- Store data permanently
- Read existing data
- Update files
- Process datasets

## 📝 Syntax

```python
open(filename, mode)
```

---

# 6. Open a File

## 📖 Definition

The `open()` function opens a file for different operations.

## 🎯 Purpose

Access a file before reading or writing.

## 📝 Syntax

```python
open("file.txt", "mode")
```

## 💻 Example

```python
file = open("sample.txt", "r")
```

---

# 7. Read a File

## 📖 Definition

The `read()` method reads the entire file.

## 🎯 Purpose

Retrieve file contents.

## 📝 Syntax

```python
file.read()
```

## 💻 Example

```python
file = open("sample.txt", "r")

print(file.read())

file.close()
```

---

# 8. Write to a File

## 📖 Definition

The `write()` method writes data to a file. If the file does not exist, Python creates it.

## 🎯 Purpose

Save new information into a file.

## 📝 Syntax

```python
file.write(data)
```

## 💻 Example

```python
file = open("sample.txt", "w")

file.write("Welcome to Python")

file.close()
```

---

# 9. Append to a File

## 📖 Definition

Append mode adds new content at the end of an existing file without removing previous data.

## 🎯 Purpose

Update existing files.

## 📝 Syntax

```python
open("file.txt", "a")
```

## 💻 Example

```python
file = open("sample.txt", "a")

file.write("\nLearning File Handling")

file.close()
```

---

# 10. Close a File

## 📖 Definition

The `close()` method releases the file from memory after use.

## 🎯 Purpose

Prevent data corruption and free system resources.

## 📝 Syntax

```python
file.close()
```

## 💻 Example

```python
file = open("sample.txt", "r")

print(file.read())

file.close()
```

---

# 11. Using with Statement

## 📖 Definition

The `with` statement automatically closes the file after completing the operation.

## 🎯 Purpose

Write cleaner and safer code.

## 📝 Syntax

```python
with open(filename, mode) as file:
```

## 💻 Example

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

---

# 💼 Interview Questions

### Q1. What is the difference between `write()` and `append()`?

| write() | append() |
|----------|----------|
| Overwrites existing content | Adds content to the end |
| Creates file if not present | Creates file if not present |

---

### Q2. Why should we use the `with` statement?

**Answer**

- Automatically closes the file.
- Prevents memory leaks.
- Handles exceptions more safely.
- Produces cleaner and more readable code.

---

# ⚠️ Common Mistakes

❌ Forgetting to close a file.

```python
file = open("sample.txt", "r")
print(file.read())
```

✔ Correct

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

---

# ✅ Summary

Today you learned:

- Modules
- Import Module
- Import Specific Functions
- Import with Alias
- Create Your Own Module
- File Handling
- Open File
- Read File
- Write File
- Append File
- Close File
- with Statement

These concepts help you organize large Python programs and work efficiently with files, making them essential for data analysis, automation, and software development.
