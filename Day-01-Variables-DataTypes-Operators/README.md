# Day 1: Variables, Data Types & Operators

## 📌 Overview

Day 1 introduces the fundamental building blocks of Python programming. You will learn how to store data using variables, understand different data types, perform type checking and conversion, and use various operators to manipulate data.

---

# 1. Variables

## 📖 Definition

A variable is a named memory location used to store data. Instead of repeatedly writing a value, you assign it to a variable and use the variable name whenever needed.

## 🎯 Purpose

- Store data in memory
- Reuse values throughout the program
- Make code more readable and maintainable
- Allow values to change during execution

## 📝 Syntax

```python
variable_name = value
```

## 💻 Example

```python
name = "Mohammed Habib"
age = 22
salary = 45000

print(name)
print(age)
print(salary)
```

---

# 2. Integer (int)

## 📖 Definition

An Integer is a whole number without a decimal point.

## 🎯 Purpose

Used for counting, indexing, calculations, and storing whole numbers.

## 📝 Syntax

```python
variable = 25
```

## 💻 Example

```python
age = 25

print(age)
```

---

# 3. Float (float)

## 📖 Definition

A Float is a number containing decimal values.

## 🎯 Purpose

Used for precise numerical calculations involving decimal values.

## 📝 Syntax

```python
variable = 25.5
```

## 💻 Example

```python
salary = 55000.75

print(salary)
```

---

# 4. String (str)

## 📖 Definition

A String is a sequence of characters enclosed within single or double quotation marks.

## 🎯 Purpose

Used to store textual information.

## 📝 Syntax

```python
variable = "Text"
```

## 💻 Example

```python
name = "Habib"

print(name)
```

---

# 5. Boolean (bool)

## 📖 Definition

A Boolean data type stores only one of two values: True or False.

## 🎯 Purpose

Used in decision-making and conditional statements.

## 📝 Syntax

```python
variable = True
```

## 💻 Example

```python
is_student = True

print(is_student)
```

---

# 6. Type Checking

## 📖 Definition

Python provides the `type()` function to determine the data type of a variable.

## 🎯 Purpose

- Verify variable types
- Debug programs
- Validate input

## 📝 Syntax

```python
type(variable_name)
```

## 💻 Example

```python
age = 25

print(type(age))
```

Output

```python
<class 'int'>
```

---

# 7. Type Conversion

## 📖 Definition

Type conversion changes one data type into another.

## 🎯 Purpose

Allows different data types to work together during calculations and input processing.

## 📝 Syntax

```python
int(value)
float(value)
str(value)
bool(value)
```

## 💻 Example

```python
age = "25"

print(int(age))

price = "99.5"

print(float(price))
```

---

# 8. Arithmetic Operators

## 📖 Definition

Arithmetic operators perform mathematical calculations.

## 🎯 Purpose

Used for numerical computations.

## 📝 Syntax

```python
+
-
*
/
%
//
**
```

## 💻 Example

```python
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
```

---

# 9. Comparison Operators

## 📖 Definition

Comparison operators compare two values and return either True or False.

## 🎯 Purpose

Used in decision-making and conditional statements.

## 📝 Syntax

```python
==
!=
>
<
>=
<=
```

## 💻 Example

```python
x = 20
y = 15

print(x > y)
print(x == y)
print(x != y)
```

---

# 10. Logical Operators

## 📖 Definition

Logical operators combine multiple conditions.

## 🎯 Purpose

Used when checking multiple conditions simultaneously.

## 📝 Syntax

```python
and
or
not
```

## 💻 Example

```python
age = 22

print(age > 18 and age < 30)

print(age > 30 or age < 25)

print(not(age > 18))
```

---

# 11. String Concatenation

## 📖 Definition

String concatenation combines two or more strings into a single string.

## 🎯 Purpose

Creates complete messages from multiple strings.

## 📝 Syntax

```python
string1 + string2
```

## 💻 Example

```python
first_name = "Mohammed"
last_name = "Habib"

print(first_name + " " + last_name)
```

---

# 12. f-Strings

## 📖 Definition

An f-string is a formatted string literal that allows variables and expressions to be embedded directly inside a string.

## 🎯 Purpose

Creates readable and efficient formatted output.

## 📝 Syntax

```python
f"Text {variable}"
```

## 💻 Example

```python
name = "Habib"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

---

# ✅ Summary

In Day 1, you learned:

- Variables
- Integer
- Float
- String
- Boolean
- Type Checking
- Type Conversion
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- String Concatenation
- f-Strings

These concepts form the foundation of Python programming and are essential before moving on to data structures and data analysis libraries.
