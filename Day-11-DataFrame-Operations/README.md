# Day 11: DataFrame Operations

⬅️ Previous: [Day 10](../Day-10-Pandas-Basics/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 12](../Day-12-Data-Cleaning/README.md)

---

# 📌 Overview

A DataFrame is the primary data structure in Pandas. DataFrame operations allow you to access, filter, modify, sort, and manipulate data efficiently. These operations are essential for data analysis, machine learning, and business intelligence.

---

# 1. Select a Column

## 📖 Definition

Selecting a column retrieves a single column from a DataFrame.

## 🎯 Purpose

- Access specific data
- Perform calculations
- Analyze individual columns

## 📝 Syntax

```python
df["column_name"]
```

## 💻 Example

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df["Name"])
```

Output

```text
0    Habib
1      Ali
2     Sara
Name: Name, dtype: object
```

---

# 2. Select Multiple Columns

## 📖 Definition

Retrieve more than one column from a DataFrame.

## 🎯 Purpose

Analyze only required columns.

## 📝 Syntax

```python
df[["column1","column2"]]
```

## 💻 Example

```python
print(df[["Name","Marks"]])
```

---

# 3. Select Rows using loc[]

## 📖 Definition

`loc[]` selects rows and columns using labels.

## 🎯 Purpose

Access data by row labels.

## 📝 Syntax

```python
df.loc[row_index]
```

## 💻 Example

```python
print(df.loc[1])
```

Output

```text
Name     Ali
Age       23
Marks     85
```

---

# 4. Select Rows using iloc[]

## 📖 Definition

`iloc[]` selects rows and columns using integer positions.

## 🎯 Purpose

Retrieve data using row and column numbers.

## 📝 Syntax

```python
df.iloc[row_index]
```

## 💻 Example

```python
print(df.iloc[2])
```

---

# 5. Filter Data

## 📖 Definition

Filtering returns rows that satisfy a given condition.

## 🎯 Purpose

Extract meaningful information.

## 📝 Syntax

```python
df[df["column"] > value]
```

## 💻 Example

```python
print(df[df["Marks"] > 85])
```

Output

```text
    Name  Age  Marks
0  Habib   22     90
2   Sara   21     95
```

---

# 6. Sort Data

## 📖 Definition

The `sort_values()` method sorts rows based on one or more columns.

## 🎯 Purpose

Arrange data in ascending or descending order.

## 📝 Syntax

```python
df.sort_values(by="column")
```

## 💻 Example

```python
print(df.sort_values(by="Marks"))
```

---

# 7. Rename Columns

## 📖 Definition

The `rename()` method changes column names.

## 🎯 Purpose

Improve readability.

## 📝 Syntax

```python
df.rename(columns={"old":"new"})
```

## 💻 Example

```python
df.rename(columns={"Marks":"Score"}, inplace=True)

print(df)
```

---

# 8. Add New Column

## 📖 Definition

Create a new column by assigning values.

## 🎯 Purpose

Store calculated or additional information.

## 📝 Syntax

```python
df["new_column"] = values
```

## 💻 Example

```python
df["Result"] = ["Pass","Pass","Pass"]

print(df)
```

---

# 9. Delete Column

## 📖 Definition

The `drop()` method removes columns or rows.

## 🎯 Purpose

Remove unnecessary data.

## 📝 Syntax

```python
df.drop(columns=["column"])
```

## 💻 Example

```python
df.drop(columns=["Age"], inplace=True)

print(df)
```

---

# 10. Unique Values

## 📖 Definition

The `unique()` method returns all unique values from a column.

## 🎯 Purpose

Identify distinct values.

## 📝 Syntax

```python
df["column"].unique()
```

## 💻 Example

```python
print(df["Name"].unique())
```

Output

```text
['Habib' 'Ali' 'Sara']
```

---

# 🌍 Real-World Use Case

Suppose a school has thousands of student records.

Using DataFrame operations, you can:

- View only student names
- Find students scoring above 90
- Sort students by marks
- Rename columns for reports
- Add a grade column
- Remove unnecessary information

These operations are commonly used in reporting dashboards and data analysis.

---

# ⚠️ Common Mistakes

### ❌ Incorrect Column Selection

```python
df[Name]
```

### ✅ Correct

```python
df["Name"]
```

---

# 💼 Interview Questions

## Q1. Difference between `loc[]` and `iloc[]`?

| loc[] | iloc[] |
|--------|---------|
| Uses labels | Uses integer positions |
| Label-based indexing | Position-based indexing |

---

## Q2. Difference between selecting one column and multiple columns?

```python
df["Marks"]
```

Returns a **Series**.

```python
df[["Marks"]]
```

Returns a **DataFrame**.

---

## Q3. Why do we use `sort_values()`?

**Answer**

It arranges data based on one or more columns, making analysis and reporting easier.

---

# ✅ Summary

Today you learned:

- Select Column
- Select Multiple Columns
- loc[]
- iloc[]
- Filter Data
- sort_values()
- rename()
- Add Column
- drop()
- unique()

These operations are fundamental for manipulating and analyzing tabular data using Pandas.
