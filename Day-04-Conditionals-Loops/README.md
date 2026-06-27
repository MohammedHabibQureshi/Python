# Day 4: Conditional Statements & Loops

⬅️ Previous: [Day 3](../Day-03-Dictionaries/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 5](../Day-05-Functions/README.md)

---

# 📌 Overview

Conditional statements allow a program to make decisions based on specific conditions, while loops enable the repeated execution of code. These concepts are fundamental for automating tasks, processing data, and building intelligent programs.

---

# 1. if Statement

## 📖 Definition

The `if` statement executes a block of code only if a specified condition is **True**.

## 🎯 Purpose

- Make decisions
- Execute code conditionally
- Control program flow

## 📝 Syntax

```python
if condition:
    statement
```

## 💻 Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

Output

```text
Eligible to vote
```

---

# 2. if...else Statement

## 📖 Definition

The `if...else` statement executes one block of code if the condition is true and another block if the condition is false.

## 🎯 Purpose

Handle two possible outcomes.

## 📝 Syntax

```python
if condition:
    statement
else:
    statement
```

## 💻 Example

```python
marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Output

```text
Fail
```

---

# 3. if...elif...else Statement

## 📖 Definition

The `elif` keyword allows multiple conditions to be checked one after another.

## 🎯 Purpose

Handle multiple decision paths.

## 📝 Syntax

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

## 💻 Example

```python
marks = 82

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

Output

```text
Grade A
```

---

# 4. Nested if

## 📖 Definition

A Nested `if` is an `if` statement placed inside another `if` statement.

## 🎯 Purpose

Check multiple dependent conditions.

## 📝 Syntax

```python
if condition1:
    if condition2:
        statement
```

## 💻 Example

```python
age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
```

Output

```text
Eligible to vote
```

---

# 5. for Loop

## 📖 Definition

A `for` loop iterates over a sequence such as a list, tuple, string, or range.

## 🎯 Purpose

Repeat a block of code for every element in a sequence.

## 📝 Syntax

```python
for variable in sequence:
    statement
```

## 💻 Example

```python
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)
```

Output

```text
Apple
Banana
Orange
```

---

# 6. range()

## 📖 Definition

The `range()` function generates a sequence of numbers.

## 🎯 Purpose

Control loop iterations.

## 📝 Syntax

```python
range(start, stop, step)
```

## 💻 Example

```python
for i in range(1, 6):
    print(i)
```

Output

```text
1
2
3
4
5
```

---

# 7. while Loop

## 📖 Definition

The `while` loop repeatedly executes a block of code as long as the condition remains True.

## 🎯 Purpose

Repeat tasks when the number of iterations is unknown.

## 📝 Syntax

```python
while condition:
    statement
```

## 💻 Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```text
1
2
3
4
5
```

---

# 8. break Statement

## 📖 Definition

The `break` statement immediately terminates the loop.

## 🎯 Purpose

Exit a loop before it completes all iterations.

## 📝 Syntax

```python
break
```

## 💻 Example

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

Output

```text
1
2
3
4
```

---

# 9. continue Statement

## 📖 Definition

The `continue` statement skips the current iteration and moves to the next iteration.

## 🎯 Purpose

Ignore specific values during looping.

## 📝 Syntax

```python
continue
```

## 💻 Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output

```text
1
2
4
5
```

---

# 10. pass Statement

## 📖 Definition

The `pass` statement is a placeholder that performs no action.

## 🎯 Purpose

Create empty code blocks without causing errors.

## 📝 Syntax

```python
pass
```

## 💻 Example

```python
for i in range(5):
    if i == 3:
        pass
    print(i)
```

Output

```text
0
1
2
3
4
```

---

# ✅ Summary

In Day 4, you learned:

- if Statement
- if...else Statement
- if...elif...else Statement
- Nested if
- for Loop
- range()
- while Loop
- break Statement
- continue Statement
- pass Statement

These concepts enable Python programs to make decisions, repeat tasks efficiently, and control program execution. They are essential for solving real-world programming and data analysis problems.
