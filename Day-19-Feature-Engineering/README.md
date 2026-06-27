# Day 19: Feature Engineering

⬅️ Previous: [Day 18](../Day-18-Hypothesis-Testing/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 20](../Day-20-Feature-Scaling/README.md)

---

# 📌 Overview

Feature Engineering is the process of creating, modifying, selecting, or transforming variables (features) to improve the performance of machine learning models.

Good features help models learn patterns more accurately and improve prediction accuracy.

---

# Why Feature Engineering?

Real-world datasets often contain:

- Irrelevant columns
- Missing information
- Categorical values
- Date and time data
- Text data
- Duplicate features

Feature Engineering converts raw data into useful features for Machine Learning.

---

# 1. What is a Feature?

## 📖 Definition

A feature is an individual measurable property or characteristic of a dataset.

## 🎯 Purpose

Provide input to a machine learning model.

## 💻 Example

| Name | Age | Salary |
|------|-----|--------|
| Ali | 25 | 50000 |

Features:

- Age
- Salary

Target:

- Salary Prediction

---

# 2. Feature Selection

## 📖 Definition

Feature Selection is the process of selecting only the most important features from a dataset.

## 🎯 Purpose

- Reduce complexity
- Improve accuracy
- Reduce training time

## 📝 Syntax

```python
df[["Age", "Salary"]]
```

## 💻 Example

```python
selected = df[["Age", "Salary"]]

print(selected.head())
```

---

# 3. Feature Extraction

## 📖 Definition

Feature Extraction creates new features from existing data.

## 🎯 Purpose

Generate more meaningful information.

## 💻 Example

Date:

```text
2025-07-15
```

Extract:

- Year
- Month
- Day

---

# 4. Creating New Features

## 📖 Definition

A new feature can be created by combining existing features.

## 🎯 Purpose

Provide better information to the model.

## 📝 Syntax

```python
df["NewColumn"] = expression
```

## 💻 Example

```python
df["Total"] = df["Math"] + df["Science"]
```

---

# 5. Encoding Categorical Data

## 📖 Definition

Machine Learning models cannot understand text values directly.

Encoding converts categories into numerical values.

## 🎯 Purpose

Prepare categorical variables for machine learning.

## 📝 Syntax

```python
pd.get_dummies(df["Gender"])
```

## 💻 Example

```python
gender = pd.get_dummies(df["Gender"])

print(gender)
```

---

# 6. Label Encoding

## 📖 Definition

Assigns a unique integer to each category.

## 🎯 Purpose

Convert labels into numbers.

## 📝 Syntax

```python
from sklearn.preprocessing import LabelEncoder
```

## 💻 Example

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

df["Gender"] = encoder.fit_transform(df["Gender"])
```

---

# 7. One-Hot Encoding

## 📖 Definition

Creates separate binary columns for every category.

## 🎯 Purpose

Avoid assigning numerical order to categories.

## 📝 Syntax

```python
pd.get_dummies()
```

## 💻 Example

```python
encoded = pd.get_dummies(df, columns=["City"])
```

---

# 8. Date Feature Engineering

## 📖 Definition

Extract useful information from date columns.

## 🎯 Purpose

Generate additional features.

## 📝 Syntax

```python
df["Date"] = pd.to_datetime(df["Date"])
```

## 💻 Example

```python
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
```

---

# 9. Dropping Unnecessary Features

## 📖 Definition

Remove columns that are not useful for prediction.

## 🎯 Purpose

Reduce noise.

## 📝 Syntax

```python
df.drop(columns=["Name"])
```

## 💻 Example

```python
df.drop(columns=["Student_ID"], inplace=True)
```

---

# 10. Feature Importance

## 📖 Definition

Feature Importance measures how much each feature contributes to a machine learning model.

## 🎯 Purpose

Identify the most useful features.

## 💻 Example

Tree-based models such as Random Forest provide feature importance scores after training.

---

# 🌍 Real-World Use Case

A bank wants to predict whether a customer will default on a loan.

Raw Data:

- Name
- Age
- Income
- Gender
- City
- Loan Amount
- Joining Date

Feature Engineering can:

- Remove Name
- Encode Gender
- Encode City
- Extract Joining Year
- Create Income-to-Loan Ratio

This improves the performance of the prediction model.

---

# ⚠️ Common Mistakes

### ❌ Keeping unnecessary columns

```python
Name
Customer_ID
Phone_Number
```

These usually don't help prediction.

---

### ❌ Using Label Encoding for unordered categories

Example:

```text
Red
Blue
Green
```

Better choice:

```text
One-Hot Encoding
```

---

# 💻 Python Example

```python
import pandas as pd

data = {
    "Name":["Ali","Sara","Habib"],
    "Math":[80,90,85],
    "Science":[85,95,80],
    "Gender":["Male","Female","Male"]
}

df = pd.DataFrame(data)

# Create New Feature
df["Total"] = df["Math"] + df["Science"]

# One-Hot Encoding
df = pd.get_dummies(df, columns=["Gender"])

# Drop Unnecessary Column
df.drop(columns=["Name"], inplace=True)

print(df)
```

---

# 💼 Interview Questions

## Q1. What is Feature Engineering?

**Answer**

Feature Engineering is the process of creating, selecting, and transforming features to improve machine learning model performance.

---

## Q2. Difference between Feature Selection and Feature Extraction?

| Feature Selection | Feature Extraction |
|-------------------|-------------------|
| Select existing features | Create new features |
| Reduces dimensions | Generates new information |

---

## Q3. Difference between Label Encoding and One-Hot Encoding?

| Label Encoding | One-Hot Encoding |
|---------------|------------------|
| Assigns numbers | Creates binary columns |
| Suitable for ordinal data | Suitable for nominal data |

---

## Q4. Why do we remove unnecessary features?

**Answer**

Removing irrelevant features reduces noise, improves model accuracy, decreases training time, and lowers the risk of overfitting.

---

# ✅ Summary

Today you learned:

- Feature
- Feature Selection
- Feature Extraction
- Creating New Features
- Encoding Categorical Data
- Label Encoding
- One-Hot Encoding
- Date Feature Engineering
- Dropping Features
- Feature Importance

Feature Engineering is one of the most critical steps in building accurate and efficient machine learning models.
