# Day 21: Train-Test Split & Model Evaluation

⬅️ Previous: [Day 20](../Day-20-Feature-Scaling/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 22](../Day-22-Linear-Regression/README.md)

---

# 📌 Overview

Machine Learning models should not be evaluated on the same data used for training.

To measure how well a model performs on unseen data, the dataset is divided into:

- Training Data
- Testing Data

This process is called **Train-Test Split**.

---

# Why Train-Test Split?

It helps to:

- Measure model performance
- Prevent overfitting
- Test on unseen data
- Estimate real-world accuracy

---

# 1. Training Data

## 📖 Definition

Training Data is the portion of the dataset used to train the machine learning model.

## 🎯 Purpose

Help the model learn patterns from the data.

## 💻 Example

```text
Dataset = 1000 records

Training Data = 800 records (80%)
```

---

# 2. Testing Data

## 📖 Definition

Testing Data is the unseen data used to evaluate the trained model.

## 🎯 Purpose

Measure how well the model performs on new data.

## 💻 Example

```text
Testing Data = 200 records (20%)
```

---

# 3. Train-Test Split

## 📖 Definition

Train-Test Split divides a dataset into training and testing datasets.

## 🎯 Purpose

Evaluate the model fairly.

## 📝 Syntax

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

---

# 4. Features (X)

## 📖 Definition

Features are the input variables used to make predictions.

## 🎯 Purpose

Provide information to the model.

## 💻 Example

```python
X = df[["Age", "Salary"]]
```

---

# 5. Target (y)

## 📖 Definition

Target is the output variable that the model predicts.

## 🎯 Purpose

Provide the expected result.

## 💻 Example

```python
y = df["Purchased"]
```

---

# 6. Accuracy

## 📖 Definition

Accuracy measures the percentage of correct predictions.

## 🎯 Purpose

Evaluate classification models.

## 📝 Formula

```text
Accuracy =
Correct Predictions / Total Predictions
```

## 📝 Syntax

```python
from sklearn.metrics import accuracy_score
```

## 💻 Example

```python
accuracy_score(y_test, y_pred)
```

---

# 7. Confusion Matrix

## 📖 Definition

A Confusion Matrix compares predicted values with actual values.

## 🎯 Purpose

Understand model errors.

## 📝 Syntax

```python
from sklearn.metrics import confusion_matrix
```

## 💻 Example

```python
confusion_matrix(y_test, y_pred)
```

---

# 8. Precision

## 📖 Definition

Precision measures how many predicted positive values are actually positive.

## 🎯 Purpose

Reduce False Positives.

## 📝 Formula

```text
Precision = TP / (TP + FP)
```

---

# 9. Recall

## 📖 Definition

Recall measures how many actual positive values were correctly identified.

## 🎯 Purpose

Reduce False Negatives.

## 📝 Formula

```text
Recall = TP / (TP + FN)
```

---

# 10. F1-Score

## 📖 Definition

F1-Score is the harmonic mean of Precision and Recall.

## 🎯 Purpose

Provide a balanced evaluation when classes are imbalanced.

## 📝 Formula

```text
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

---

# 11. Overfitting

## 📖 Definition

Overfitting occurs when a model learns the training data too well, including noise.

## 🎯 Purpose

Understand why models may fail on unseen data.

## Characteristics

- Very high training accuracy
- Low testing accuracy

---

# 12. Underfitting

## 📖 Definition

Underfitting occurs when the model is too simple to learn the underlying patterns.

## 🎯 Purpose

Recognize when a model has not learned enough.

## Characteristics

- Low training accuracy
- Low testing accuracy

---

# 🌍 Real-World Use Case

A bank wants to predict whether a customer will default on a loan.

Dataset:

- Age
- Income
- Credit Score

Target:

- Default (Yes/No)

The model is trained using 80% of the data and tested on the remaining 20% to estimate how well it performs on new customers.

---

# ⚠️ Common Mistakes

### ❌ Evaluating on training data

This gives misleadingly high accuracy.

### ✅ Correct

Always evaluate using the testing dataset.

---

### ❌ Forgetting random_state

Without `random_state`, the split changes every time you run the program.

---

# 💻 Python Example

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

# 💼 Interview Questions

## Q1. Why do we split the dataset?

**Answer**

To evaluate the model on unseen data and estimate its real-world performance.

---

## Q2. What is the difference between training and testing data?

| Training Data | Testing Data |
|--------------|--------------|
| Used to train the model | Used to evaluate the model |
| Usually 70–80% | Usually 20–30% |

---

## Q3. What is Overfitting?

**Answer**

Overfitting occurs when a model memorizes the training data instead of learning general patterns, leading to poor performance on new data.

---

## Q4. What is Underfitting?

**Answer**

Underfitting occurs when a model is too simple and fails to capture the underlying patterns in the data.

---

## Q5. Why is F1-Score important?

**Answer**

F1-Score balances Precision and Recall, making it useful for datasets with imbalanced classes.

---

# ✅ Summary

Today you learned:

- Training Data
- Testing Data
- Train-Test Split
- Features (X)
- Target (y)
- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-Score
- Overfitting
- Underfitting

These concepts are essential before building and evaluating machine learning models.
