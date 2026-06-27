# Day 20: Feature Scaling

⬅️ Previous: [Day 19](../Day-19-Feature-Engineering/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 21](../Day-21-Train-Test-Split/README.md)

---

# 📌 Overview

Feature Scaling is the process of transforming numerical features so that they have a similar range or distribution.

Many Machine Learning algorithms calculate distances between data points. If one feature has much larger values than another, it can dominate the learning process and reduce model performance.

---

# Why Feature Scaling?

Feature Scaling helps to:

- Improve model accuracy
- Speed up model training
- Prevent one feature from dominating others
- Improve convergence of optimization algorithms
- Make distance-based algorithms perform better

---

# Algorithms That Require Feature Scaling

Feature Scaling is important for:

- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Logistic Regression
- Linear Regression (Gradient Descent)
- K-Means Clustering
- Principal Component Analysis (PCA)
- Neural Networks

Algorithms like Decision Trees and Random Forest generally do not require feature scaling.

---

# 1. Normalization (Min-Max Scaling)

## 📖 Definition

Normalization rescales data to a fixed range, usually between **0 and 1**.

## 🎯 Purpose

Ensure all features contribute equally when their original ranges differ significantly.

## 📝 Formula

```text
X' = (X - Xmin) / (Xmax - Xmin)
```

## 📝 Syntax

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)
```

## 💻 Example

```python
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = pd.DataFrame({
    "Salary":[25000,50000,75000,100000]
})

scaler = MinMaxScaler()

print(scaler.fit_transform(data))
```

---

# 2. Standardization (Z-Score Scaling)

## 📖 Definition

Standardization transforms data so that it has:

- Mean = 0
- Standard Deviation = 1

## 🎯 Purpose

Reduce the effect of different feature scales while preserving outliers.

## 📝 Formula

```text
Z = (X - Mean) / Standard Deviation
```

## 📝 Syntax

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)
```

## 💻 Example

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

print(scaler.fit_transform(data))
```

---

# 3. Difference Between Normalization and Standardization

| Normalization | Standardization |
|--------------|-----------------|
| Scales data between 0 and 1 | Mean becomes 0 |
| Sensitive to outliers | Less sensitive to outliers |
| Uses Min and Max values | Uses Mean and Standard Deviation |
| Best for bounded data | Best for normally distributed data |

---

# 4. MinMaxScaler

## 📖 Definition

A Scikit-learn class that performs Min-Max Normalization.

## 🎯 Purpose

Convert values into the range [0,1].

## 📝 Syntax

```python
MinMaxScaler()
```

## 💻 Example

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaled = scaler.fit_transform(df)
```

---

# 5. StandardScaler

## 📖 Definition

A Scikit-learn class that performs Standardization.

## 🎯 Purpose

Transform data to mean 0 and standard deviation 1.

## 📝 Syntax

```python
StandardScaler()
```

## 💻 Example

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaled = scaler.fit_transform(df)
```

---

# 6. When to Use Normalization?

## 📖 Definition

Normalization is preferred when data does not follow a normal distribution and values have different ranges.

## 🎯 Use Cases

- Image Processing
- Deep Learning
- KNN
- Neural Networks

---

# 7. When to Use Standardization?

## 📖 Definition

Standardization is preferred when data approximately follows a normal distribution.

## 🎯 Use Cases

- Linear Regression
- Logistic Regression
- Support Vector Machine
- Principal Component Analysis (PCA)

---

# 🌍 Real-World Use Case

A bank wants to predict whether customers will default on loans.

Features:

| Age | Salary |
|-----|---------|
| 25 | 30,000 |
| 45 | 900,000 |

Without scaling, the Salary feature dominates because its values are much larger than Age.

Feature Scaling ensures that both features contribute fairly to the model.

---

# ⚠️ Common Mistakes

### ❌ Training the scaler separately on training and testing data

```python
train_scaler.fit(train)

test_scaler.fit(test)
```

This produces inconsistent scaling.

### ✅ Correct

```python
scaler.fit(train)

train_scaled = scaler.transform(train)

test_scaled = scaler.transform(test)
```

---

### ❌ Applying scaling before splitting the dataset

Always split the dataset first, then fit the scaler only on the training data.

---

# 💻 Python Example

```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = pd.DataFrame({
    "Age":[20,30,40,50],
    "Salary":[30000,50000,70000,90000]
})

print("Original Data")
print(data)

# Normalization
minmax = MinMaxScaler()
normalized = minmax.fit_transform(data)

print("\nNormalized Data")
print(normalized)

# Standardization
standard = StandardScaler()
standardized = standard.fit_transform(data)

print("\nStandardized Data")
print(standardized)
```

---

# 💼 Interview Questions

## Q1. What is Feature Scaling?

**Answer**

Feature Scaling is the process of transforming numerical features to a common scale so that all features contribute equally during model training.

---

## Q2. Difference between Normalization and Standardization?

| Normalization | Standardization |
|--------------|-----------------|
| Range is 0–1 | Mean = 0, Standard Deviation = 1 |
| Uses Min and Max | Uses Mean and Standard Deviation |
| Sensitive to outliers | Less sensitive to outliers |

---

## Q3. Which algorithms require Feature Scaling?

**Answer**

- KNN
- SVM
- Logistic Regression
- K-Means
- PCA
- Neural Networks

---

## Q4. Do Decision Trees require Feature Scaling?

**Answer**

No. Decision Trees and Random Forests split data based on feature values rather than distances, so they generally do not require feature scaling.

---

# ✅ Summary

Today you learned:

- Feature Scaling
- Normalization
- Standardization
- MinMaxScaler
- StandardScaler
- Difference between Normalization and Standardization
- When to use each scaling technique
- Algorithms that require feature scaling

Feature Scaling is an essential preprocessing step that improves the performance and stability of many machine learning algorithms.
