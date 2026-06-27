# Day 5: Functions

⬅️ Previous: [Day 4](../Day-04-Conditionals-Loops/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 6](../Day-06-Modules-File-Handling/README.md)

---

# 📌 Overview

Functions are reusable blocks of code designed to perform a specific task. Instead of writing the same code multiple times, you can define it once and call it whenever needed.

Functions improve code readability, reduce duplication, and make programs easier to maintain.

---

# 1. Function

## 📖 Definition

A function is a block of reusable code that performs a specific task. It executes only when it is called.

## 🎯 Purpose

- Avoid code repetition
- Improve code organization
- Increase readability
- Make debugging easier

## 📝 Syntax

```python
def function_name():
    statements
```

## 💻 Example

```python
def greet():
    print("Welcome to Python!")

greet()
```

Output

```text
Welcome to Python!
```

---

# 2. Function with Parameters

## 📖 Definition

Parameters are variables passed into a function during its definition.

## 🎯 Purpose

Allow functions to accept different input values.

## 📝 Syntax

```python
def function_name(parameter):
    statements
```

## 💻 Example

```python
def greet(name):
    print("Hello", name)

greet("Habib")
```

Output

```text
Hello Habib
```

---

# 3. Function with Multiple Parameters

## 📖 Definition

A function can accept multiple parameters separated by commas.

## 🎯 Purpose

Pass multiple values to a function.

## 📝 Syntax

```python
def function_name(param1, param2):
    statements
```

## 💻 Example

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output

```text
30
```

---

# 4. Return Statement

## 📖 Definition

The `return` statement sends a value back to the function caller.

## 🎯 Purpose

Return results for further use.

## 📝 Syntax

```python
return value
```

## 💻 Example

```python
def square(num):
    return num ** 2

result = square(5)

print(result)
```

Output

```text
25
```

---

# 5. Default Parameters

## 📖 Definition

Default parameters assign a default value if no argument is provided.

## 🎯 Purpose

Make function arguments optional.

## 📝 Syntax

```python
def function_name(parameter=value):
```

## 💻 Example

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Habib")
```

Output

```text
Hello Guest
Hello Habib
```

---

# 6. Keyword Arguments

## 📖 Definition

Keyword arguments specify the parameter name while calling the function.

## 🎯 Purpose

Improve readability and allow arguments in any order.

## 📝 Syntax

```python
function(parameter=value)
```

## 💻 Example

```python
def student(name, age):
    print(name, age)

student(age=22, name="Habib")
```

Output

```text
Habib 22
```

---

# 7. Variable-Length Arguments (*args)

## 📖 Definition

`*args` allows a function to accept any number of positional arguments.

## 🎯 Purpose

Handle an unknown number of inputs.

## 📝 Syntax

```python
def function_name(*args):
```

## 💻 Example

```python
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30, 40)
```

Output

```text
100
```

---

# 8. Keyword Variable-Length Arguments (**kwargs)

## 📖 Definition

`**kwargs` allows a function to accept any number of keyword arguments.

## 🎯 Purpose

Handle dynamic named inputs.

## 📝 Syntax

```python
def function_name(**kwargs):
```

## 💻 Example

```python
def employee(**details):
    print(details)

employee(name="Habib", age=22, city="Mumbai")
```

Output

```text
{'name': 'Habib', 'age': 22, 'city': 'Mumbai'}
```

---

# 9. Lambda Function

## 📖 Definition

A Lambda Function is a small anonymous function written in a single line.

## 🎯 Purpose

Create simple functions without using `def`.

## 📝 Syntax

```python
lambda arguments: expression
```

## 💻 Example

```python
square = lambda x: x ** 2

print(square(6))
```

Output

```text
36
```

---

# 10. Recursive Function

## 📖 Definition

A Recursive Function is a function that calls itself until a stopping condition is met.

## 🎯 Purpose

Solve problems that can be divided into smaller subproblems.

## 📝 Syntax

```python
def function():
    function()
```

## 💻 Example

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

Output

```text
120
```

---

# 💼 Interview Question

### Q1. What is the difference between `print()` and `return`?

**Answer**

| print() | return |
|----------|---------|
| Displays output on the screen | Sends a value back to the caller |
| Cannot be reused | Can be stored in a variable |
| Mainly for debugging | Used in real applications |

---

### Q2. What is the difference between Parameters and Arguments?

**Parameters**
- Variables defined in the function declaration.

**Arguments**
- Actual values passed while calling the function.

Example

```python
def greet(name):      # name is a parameter
    print(name)

greet("Habib")        # "Habib" is an argument
```

---

# ✅ Summary

Today you learned:

- Functions
- Parameters
- Multiple Parameters
- Return Statement
- Default Parameters
- Keyword Arguments
- *args
- **kwargs
- Lambda Functions
- Recursive Functions

Functions are one of the most important concepts in Python and are heavily used in Data Analysis, Machine Learning, Web Development, Automation, and Software Development.
