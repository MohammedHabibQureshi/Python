# Day 7: Exception Handling

⬅️ Previous: [Day 6](../Day-06-Modules-File-Handling/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 8](../Day-08-NumPy-Basics/README.md)

---

# 📌 Overview

Exception Handling is a mechanism used to handle runtime errors gracefully without stopping the execution of the program. Instead of crashing, Python allows us to catch and handle errors using special keywords.

It is commonly used in file handling, user input validation, databases, APIs, and machine learning applications.

---

# 1. Exception

## 📖 Definition

An Exception is an error that occurs during the execution of a program, interrupting the normal flow of execution.

## 🎯 Purpose

- Detect runtime errors
- Prevent program crashes
- Improve program reliability

## 💻 Example

```python
num = 10
print(num / 0)
```

Output

```text
ZeroDivisionError: division by zero
```

---

# 2. try Block

## 📖 Definition

The `try` block contains code that may raise an exception.

## 🎯 Purpose

Monitor code that might produce an error.

## 📝 Syntax

```python
try:
    statements
```

## 💻 Example

```python
try:
    print(10 / 0)
```

---

# 3. except Block

## 📖 Definition

The `except` block executes when an exception occurs inside the `try` block.

## 🎯 Purpose

Handle errors without terminating the program.

## 📝 Syntax

```python
try:
    statements
except:
    statements
```

## 💻 Example

```python
try:
    print(10 / 0)
except:
    print("Cannot divide by zero.")
```

Output

```text
Cannot divide by zero.
```

---

# 4. Handling Specific Exceptions

## 📖 Definition

Specific exceptions allow you to catch only particular types of errors.

## 🎯 Purpose

Provide customized error handling.

## 📝 Syntax

```python
except ExceptionName:
```

## 💻 Example

```python
try:
    number = int("Python")
except ValueError:
    print("Invalid number.")
```

Output

```text
Invalid number.
```

---

# 5. Multiple Exceptions

## 📖 Definition

A program can handle different types of exceptions using multiple `except` blocks.

## 🎯 Purpose

Handle different errors separately.

## 📝 Syntax

```python
try:
    statements
except Exception1:
    statements
except Exception2:
    statements
```

## 💻 Example

```python
try:
    number = int(input("Enter number: "))
    print(10 / number)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 6. else Block

## 📖 Definition

The `else` block executes only if no exception occurs.

## 🎯 Purpose

Run code when the program executes successfully.

## 📝 Syntax

```python
try:
    statements
except:
    statements
else:
    statements
```

## 💻 Example

```python
try:
    num = 10
    print(num / 2)

except ZeroDivisionError:
    print("Error")

else:
    print("Division Successful")
```

Output

```text
5.0
Division Successful
```

---

# 7. finally Block

## 📖 Definition

The `finally` block always executes whether an exception occurs or not.

## 🎯 Purpose

Release resources such as files and database connections.

## 📝 Syntax

```python
try:
    statements
except:
    statements
finally:
    statements
```

## 💻 Example

```python
try:
    print(10 / 2)

finally:
    print("Execution Completed")
```

Output

```text
5.0
Execution Completed
```

---

# 8. Raise Exception

## 📖 Definition

The `raise` keyword allows programmers to generate exceptions manually.

## 🎯 Purpose

Validate data and stop execution when invalid conditions occur.

## 📝 Syntax

```python
raise ExceptionName("Message")
```

## 💻 Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Output

```text
ValueError: Age cannot be negative.
```

---

# 9. User-Defined Exception

## 📖 Definition

Python allows programmers to create their own exception classes.

## 🎯 Purpose

Handle application-specific errors.

## 📝 Syntax

```python
class ExceptionName(Exception):
    pass
```

## 💻 Example

```python
class InvalidAgeError(Exception):
    pass

age = -1

if age < 0:
    raise InvalidAgeError("Invalid Age")
```

---

# 🌍 Real-World Use Case

Imagine a banking application.

A customer enters the amount to withdraw.

Instead of crashing when invalid input is entered, Exception Handling displays a meaningful message.

```python
try:
    amount = int(input("Enter amount: "))

    if amount < 0:
        raise ValueError

    print("Transaction Successful")

except ValueError:
    print("Invalid Amount")
```

---

# ⚠️ Common Mistakes

### ❌ Using a bare except

```python
try:
    print(10 / 0)
except:
    print("Error")
```

### ✅ Better Practice

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 💼 Interview Questions

## Q1. What is Exception Handling?

**Answer**

Exception Handling is a mechanism that allows a program to detect and handle runtime errors without terminating unexpectedly.

---

## Q2. Difference between Error and Exception?

| Error | Exception |
|--------|-----------|
| Usually unrecoverable | Can be handled |
| Stops the program | Program can continue |

---

## Q3. Difference between `else` and `finally`?

| else | finally |
|------|----------|
| Executes only if no exception occurs | Always executes |
| Used for success code | Used for cleanup |

---

# ✅ Summary

Today you learned:

- Exception
- try
- except
- Specific Exceptions
- Multiple Exceptions
- else
- finally
- raise
- User-Defined Exception

These concepts are essential for writing robust Python applications that can gracefully handle unexpected situations and continue running without crashing.
