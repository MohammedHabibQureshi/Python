# Day 12: Data Cleaning

⬅️ Previous: [Day 11](../Day-11-DataFrame-Operations/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 13](../Day-13-Data-Visualization/README.md)

---

# 📌 Overview

Data Cleaning is the process of identifying and correcting inaccurate, incomplete, duplicate, or inconsistent data. Since real-world datasets are rarely perfect, data cleaning is one of the most important steps in Data Analysis and Machine Learning.

A clean dataset improves analysis accuracy and model performance.

---

# Why Data Cleaning?

Real-world datasets often contain:

- Missing values
- Duplicate records
- Incorrect data
- Extra spaces
- Wrong data types
- Outliers

Cleaning data ensures reliable and accurate analysis.

---

# 1. Check Missing Values

## 📖 Definition

The `isnull()` function identifies missing (null) values in a DataFrame.

## 🎯 Purpose

Find incomplete data before analysis.

## 📝 Syntax

```python
df.isnull()
```

## 💻 Example

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df.isnull())
```

---

# 2. Count Missing Values

## 📖 Definition

The `isnull().sum()` method counts missing values in each column.

## 🎯 Purpose

Identify columns with missing data.

## 📝 Syntax

```python
df.isnull().sum()
```

## 💻 Example

```python
print(df.isnull().sum())
```

Output

```text
Name     0
Age      1
Marks    2
dtype: int64
```

---

# 3. Drop Missing Values

## 📖 Definition

The `dropna()` method removes rows containing missing values.

## 🎯 Purpose

Remove incomplete records.

## 📝 Syntax

```python
df.dropna()
```

## 💻 Example

```python
clean_df = df.dropna()

print(clean_df)
```

---

# 4. Fill Missing Values

## 📖 Definition

The `fillna()` method replaces missing values with a specified value.

## 🎯 Purpose

Keep all records while handling missing data.

## 📝 Syntax

```python
df.fillna(value)
```

## 💻 Example

```python
df["Marks"].fillna(0, inplace=True)

print(df)
```

---

# 5. Fill Missing Values using Mean

## 📖 Definition

Replace missing numerical values with the average of the column.

## 🎯 Purpose

Maintain the dataset without removing rows.

## 📝 Syntax

```python
df["column"].fillna(df["column"].mean())
```

## 💻 Example

```python
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
```

---

# 6. Check Duplicate Rows

## 📖 Definition

The `duplicated()` method identifies duplicate rows.

## 🎯 Purpose

Detect repeated records.

## 📝 Syntax

```python
df.duplicated()
```

## 💻 Example

```python
print(df.duplicated())
```

---

# 7. Remove Duplicate Rows

## 📖 Definition

The `drop_duplicates()` method removes duplicate records.

## 🎯 Purpose

Keep only unique records.

## 📝 Syntax

```python
df.drop_duplicates()
```

## 💻 Example

```python
df = df.drop_duplicates()
```

---

# 8. Rename Columns

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
```

---

# 9. Change Data Type

## 📖 Definition

The `astype()` method converts one data type into another.

## 🎯 Purpose

Ensure correct data formats.

## 📝 Syntax

```python
df["column"].astype(type)
```

## 💻 Example

```python
df["Age"] = df["Age"].astype(int)
```

---

# 10. Remove Extra Spaces

## 📖 Definition

The `str.strip()` method removes leading and trailing spaces from text.

## 🎯 Purpose

Standardize string values.

## 📝 Syntax

```python
df["column"].str.strip()
```

## 💻 Example

```python
df["Name"] = df["Name"].str.strip()
```

---

# 🌍 Real-World Use Case

Suppose an online shopping company has customer data.

Problems in the dataset:

- Missing phone numbers
- Duplicate customer records
- Extra spaces in names
- Missing order amounts

Using Pandas, you can:

- Remove duplicates
- Fill missing values
- Correct data types
- Clean text data
- Prepare the dataset for reporting or machine learning

---

# ⚠️ Common Mistakes

### ❌ Ignoring Missing Values

```python
print(df["Marks"].mean())
```

This may produce misleading results if many values are missing.

### ✅ Correct

```python
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
```

---

# 💼 Interview Questions

## Q1. Why is Data Cleaning important?

**Answer**

Data cleaning improves data quality, removes inconsistencies, and ensures accurate analysis and better machine learning performance.

---

## Q2. Difference between `dropna()` and `fillna()`?

| dropna() | fillna() |
|-----------|-----------|
| Removes rows with missing values | Replaces missing values |
| Reduces dataset size | Keeps all rows |

---

## Q3. What does `drop_duplicates()` do?

**Answer**

It removes duplicate rows from a DataFrame while keeping the first occurrence by default.

---

# ✅ Summary

Today you learned:

- isnull()
- isnull().sum()
- dropna()
- fillna()
- Fill using Mean
- duplicated()
- drop_duplicates()
- rename()
- astype()
- str.strip()

These techniques are essential for preparing clean and reliable datasets before performing analysis or building machine learning models.
