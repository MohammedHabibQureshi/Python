# Day 10: Pandas Basics

⬅️ Previous: [Day 9](../Day-09-NumPy-Operations/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 11](../Day-11-DataFrame-Operations/README.md)

---

# 📌 Overview

Pandas is an open-source Python library used for data manipulation and analysis. It provides powerful data structures like **Series** and **DataFrame**, making it easy to work with structured data.

Pandas is widely used in:

- Data Analysis
- Machine Learning
- Data Cleaning
- Data Visualization
- Business Analytics

---

# Why Pandas?

Without Pandas, handling large datasets using Python lists and dictionaries becomes difficult.

Pandas provides:

- Fast data processing
- Easy data cleaning
- Built-in statistical functions
- Reading and writing multiple file formats
- Powerful indexing and filtering

---

# 1. Import Pandas

## 📖 Definition

Before using Pandas, you must import the library.

## 🎯 Purpose

Access Pandas functions using the alias **pd**.

## 📝 Syntax

```python
import pandas as pd
```

## 💻 Example

```python
import pandas as pd

print(pd.__version__)
```

---

# 2. Series

## 📖 Definition

A Series is a one-dimensional labeled array capable of storing different data types.

## 🎯 Purpose

Store a single column of data.

## 📝 Syntax

```python
pd.Series(data)
```

## 💻 Example

```python
import pandas as pd

marks = pd.Series([80,85,90,95])

print(marks)
```

Output

```text
0    80
1    85
2    90
3    95
dtype: int64
```

---

# 3. DataFrame

## 📖 Definition

A DataFrame is a two-dimensional table consisting of rows and columns.

## 🎯 Purpose

Store and analyze tabular data.

## 📝 Syntax

```python
pd.DataFrame(data)
```

## 💻 Example

```python
student = {
    "Name":["Habib","Ali","Sara"],
    "Age":[22,23,21],
    "Marks":[90,85,95]
}

df = pd.DataFrame(student)

print(df)
```

Output

```text
    Name  Age  Marks
0  Habib   22     90
1    Ali   23     85
2   Sara   21     95
```

---

# 4. Read CSV File

## 📖 Definition

The `read_csv()` function loads data from a CSV file into a DataFrame.

## 🎯 Purpose

Read datasets for analysis.

## 📝 Syntax

```python
pd.read_csv("filename.csv")
```

## 💻 Example

```python
df = pd.read_csv("students.csv")

print(df)
```

---

# 5. View First Rows

## 📖 Definition

The `head()` function displays the first rows of a DataFrame.

## 🎯 Purpose

Quickly inspect data.

## 📝 Syntax

```python
df.head()
```

## 💻 Example

```python
print(df.head())
```

---

# 6. View Last Rows

## 📖 Definition

The `tail()` function displays the last rows of a DataFrame.

## 🎯 Purpose

Inspect the end of a dataset.

## 📝 Syntax

```python
df.tail()
```

## 💻 Example

```python
print(df.tail())
```

---

# 7. Data Information

## 📖 Definition

The `info()` function displays information about the DataFrame.

## 🎯 Purpose

Understand columns, data types, and missing values.

## 📝 Syntax

```python
df.info()
```

## 💻 Example

```python
df.info()
```

---

# 8. Statistical Summary

## 📖 Definition

The `describe()` function generates descriptive statistics.

## 🎯 Purpose

Understand numerical data.

## 📝 Syntax

```python
df.describe()
```

## 💻 Example

```python
print(df.describe())
```

---

# 9. Shape

## 📖 Definition

The `shape` attribute returns the number of rows and columns.

## 🎯 Purpose

Know the size of the dataset.

## 📝 Syntax

```python
df.shape
```

## 💻 Example

```python
print(df.shape)
```

Output

```text
(3,3)
```

---

# 10. Columns

## 📖 Definition

Returns the names of all columns in a DataFrame.

## 🎯 Purpose

Identify available features.

## 📝 Syntax

```python
df.columns
```

## 💻 Example

```python
print(df.columns)
```

Output

```text
Index(['Name','Age','Marks'], dtype='object')
```

---

# 🌍 Real-World Use Case

Suppose a company stores employee information in a CSV file.

```text
Name,Department,Salary
Habib,IT,50000
Ali,HR,45000
Sara,Finance,60000
```

Using Pandas you can:

- Read the CSV file.
- Analyze salaries.
- Filter employees.
- Generate reports.
- Prepare data for Machine Learning.

---

# ⚠️ Common Mistakes

### ❌ Forgetting to import Pandas

```python
df = pd.read_csv("students.csv")
```

### ✅ Correct

```python
import pandas as pd

df = pd.read_csv("students.csv")
```

---

# 💼 Interview Questions

## Q1. What is Pandas?

**Answer**

Pandas is an open-source Python library used for data manipulation and analysis.

---

## Q2. Difference between Series and DataFrame?

| Series | DataFrame |
|---------|-----------|
| One-dimensional | Two-dimensional |
| Single column | Multiple columns |
| Homogeneous or mixed data | Tabular data |

---

## Q3. Why is Pandas important?

**Answer**

- Fast data processing
- Easy data cleaning
- Supports CSV, Excel, SQL, JSON
- Integrates with NumPy and Scikit-learn

---

# ✅ Summary

Today you learned:

- Import Pandas
- Series
- DataFrame
- Read CSV
- head()
- tail()
- info()
- describe()
- shape
- columns

These concepts form the foundation of working with structured data in Python using Pandas.
