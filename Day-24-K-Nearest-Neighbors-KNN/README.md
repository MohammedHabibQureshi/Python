# Day 24: K-Nearest Neighbors (KNN)

⬅️ Previous: [Day 23](../Day-23-Logistic-Regression/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 25](../Day-25-Decision-Tree/README.md)

---

# 📌 Overview

K-Nearest Neighbors (KNN) is a supervised machine learning algorithm that classifies a new data point based on the majority class of its nearest neighbors.

Unlike many algorithms, KNN does not build a mathematical model during training. Instead, it stores the training data and makes predictions when new data is provided.

---

# Why KNN?

KNN is useful because it:

- Is simple and easy to understand
- Works well for small datasets
- Can solve both classification and regression problems
- Requires no assumptions about data distribution

Applications include:

- Handwritten Digit Recognition
- Recommendation Systems
- Medical Diagnosis
- Face Recognition
- Credit Risk Analysis

---

# 1. K-Nearest Neighbors (KNN)

## 📖 Definition

KNN is a supervised learning algorithm that predicts the class of a new data point by looking at the K closest training examples.

## 🎯 Purpose

Classify or predict new data based on similarity.

## 📝 Syntax

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)
```

---

# 2. K Value

## 📖 Definition

K represents the number of nearest neighbors considered while making a prediction.

## 🎯 Purpose

Control how many nearby data points influence the prediction.

## 💻 Example

```text
K = 3

Nearest Neighbors:

Class A
Class A
Class B

Prediction = Class A
```

---

# 3. Distance Metric

## 📖 Definition

Distance metrics measure how close two data points are.

## 🎯 Purpose

Find the nearest neighbors.

Common distance metrics:

- Euclidean Distance
- Manhattan Distance
- Minkowski Distance

---

# 4. Euclidean Distance

## 📖 Definition

The straight-line distance between two points.

## 🎯 Purpose

Measure similarity between observations.

## Formula

```text
Distance = √((x₂-x₁)² + (y₂-y₁)²)
```

---

# 5. Manhattan Distance

## 📖 Definition

Measures distance by moving horizontally and vertically.

## 🎯 Purpose

Useful when movement follows grid-like paths.

## Formula

```text
Distance = |x₂-x₁| + |y₂-y₁|
```

---

# 6. Lazy Learning

## 📖 Definition

KNN is called a Lazy Learning algorithm because it does not learn a model during training.

## 🎯 Purpose

Store training data and perform computations only during prediction.

---

# 7. Feature Scaling in KNN

## 📖 Definition

Feature Scaling ensures all features contribute equally when calculating distances.

## 🎯 Purpose

Prevent large-valued features from dominating distance calculations.

## 💻 Example

```text
Age = 30

Salary = 900000

Without scaling, Salary dominates the distance calculation.
```

---

# 8. Choosing the Best K

## 📖 Definition

Selecting the optimal K value improves prediction accuracy.

## 🎯 Purpose

Balance bias and variance.

General guideline:

```text
Small K → Overfitting

Large K → Underfitting
```

---

# 9. Advantages of KNN

## 📖 Definition

Benefits of using KNN.

### Advantages

- Easy to implement
- No training phase
- Works for classification and regression
- Handles multi-class problems

---

# 10. Limitations of KNN

## 📖 Definition

Challenges when using KNN.

### Limitations

- Slow for large datasets
- Sensitive to irrelevant features
- Requires feature scaling
- High memory usage

---

# 🌍 Real-World Use Case

A hospital wants to classify whether a patient has diabetes.

Features:

- Age
- Blood Pressure
- Glucose Level

KNN compares the patient's information with similar patients and predicts whether the patient is diabetic.

---

# ⚠️ Common Mistakes

### ❌ Not scaling data

Distance-based algorithms require feature scaling.

---

### ❌ Choosing K = 1 without validation

A very small K may lead to overfitting.

---

### ❌ Choosing a very large K

A very large K may ignore important local patterns and lead to underfitting.

---

# 💻 Python Example

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print(prediction)
```

---

# 💼 Interview Questions

## Q1. What is KNN?

**Answer**

KNN is a supervised learning algorithm that predicts the class of a new data point based on the majority class of its K nearest neighbors.

---

## Q2. Why is KNN called Lazy Learning?

**Answer**

Because it does not build a model during training. It stores the training data and performs calculations only during prediction.

---

## Q3. Why is Feature Scaling important in KNN?

**Answer**

KNN relies on distance calculations. Without feature scaling, features with larger values dominate the distance and produce incorrect predictions.

---

## Q4. What happens if K is too small?

**Answer**

The model becomes sensitive to noise and may overfit the training data.

---

## Q5. What happens if K is too large?

**Answer**

The model may overlook important local patterns, resulting in underfitting.

---

# ✅ Summary

Today you learned:

- K-Nearest Neighbors (KNN)
- K Value
- Distance Metrics
- Euclidean Distance
- Manhattan Distance
- Lazy Learning
- Feature Scaling
- Choosing the Best K
- Advantages of KNN
- Limitations of KNN

KNN is one of the simplest machine learning algorithms and is widely used for classification problems based on similarity.
