# Day 26: Random Forest

⬅️ Previous: [Day 25](../Day-25-Decision-Tree/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 27](../Day-27-K-Means-Clustering/README.md)

---

# 📌 Overview

Random Forest is a supervised Machine Learning algorithm that combines multiple Decision Trees to improve prediction accuracy and reduce overfitting.

Instead of relying on one Decision Tree, Random Forest builds many trees and combines their predictions.

It can solve both:

- Classification Problems
- Regression Problems

---

# Why Random Forest?

Random Forest helps us:

- Improve prediction accuracy
- Reduce overfitting
- Handle missing values
- Work with large datasets
- Measure feature importance

Applications include:

- Fraud Detection
- Disease Prediction
- Stock Market Prediction
- Customer Churn Prediction
- Credit Risk Analysis

---

# 1. Random Forest

## 📖 Definition

Random Forest is an ensemble learning algorithm that builds multiple Decision Trees and combines their predictions.

## 🎯 Purpose

Increase accuracy and improve model generalization.

## 📝 Syntax

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
```

---

# 2. Ensemble Learning

## 📖 Definition

Ensemble Learning combines multiple machine learning models to produce a stronger overall model.

## 🎯 Purpose

Improve prediction performance.

## Example

```text
Tree 1 → Yes

Tree 2 → Yes

Tree 3 → No

Final Prediction → Yes
```

---

# 3. Bagging (Bootstrap Aggregating)

## 📖 Definition

Bagging creates multiple datasets by randomly sampling the training data with replacement.

Each dataset trains a different Decision Tree.

## 🎯 Purpose

Reduce variance and improve stability.

---

# 4. Bootstrap Sampling

## 📖 Definition

Bootstrap Sampling randomly selects samples from the original dataset **with replacement**.

## 🎯 Purpose

Generate different training datasets for each tree.

## Example

Original Dataset:

```text
A B C D E
```

Bootstrap Sample:

```text
A C C D E
```

Notice that **C** appears twice because sampling is done with replacement.

---

# 5. Voting Mechanism

## 📖 Definition

For classification, every Decision Tree votes for a class.

The class with the highest number of votes becomes the final prediction.

## 🎯 Purpose

Produce a reliable prediction.

## Example

```text
Tree 1 → Cat

Tree 2 → Dog

Tree 3 → Dog

Final Prediction → Dog
```

---

# 6. Feature Importance

## 📖 Definition

Feature Importance indicates how much each feature contributes to the model's predictions.

## 🎯 Purpose

Identify the most influential features.

## Example

```text
Income        → 45%

Credit Score  → 35%

Age           → 20%
```

---

# 7. Number of Trees (n_estimators)

## 📖 Definition

The number of Decision Trees built in the Random Forest.

## 🎯 Purpose

Control model performance.

## Syntax

```python
RandomForestClassifier(n_estimators=100)
```

More trees generally improve stability but increase training time.

---

# 8. Out-of-Bag (OOB) Error

## 📖 Definition

Some training samples are not selected during bootstrap sampling.

These unused samples are called **Out-of-Bag samples**.

## 🎯 Purpose

Estimate model performance without needing a separate validation dataset.

---

# 9. Advantages of Random Forest

## 📖 Definition

Benefits of using Random Forest.

### Advantages

- High accuracy
- Reduces overfitting
- Handles missing values
- Supports classification and regression
- Provides feature importance
- Works well with large datasets

---

# 10. Limitations of Random Forest

## 📖 Definition

Challenges when using Random Forest.

### Limitations

- Slower than a single Decision Tree
- Requires more memory
- Harder to interpret
- Large models may take longer to train

---

# 🌍 Real-World Use Case

A bank wants to predict whether a customer will default on a loan.

Features:

- Age
- Income
- Credit Score
- Loan Amount

Instead of using one Decision Tree, Random Forest trains hundreds of Decision Trees.

Each tree votes:

```text
Tree 1 → Default

Tree 2 → No Default

Tree 3 → No Default

Tree 4 → Default

Tree 5 → No Default

Final Prediction → No Default
```

---

# ⚠️ Common Mistakes

### ❌ Using very few trees

Too few trees may reduce accuracy.

---

### ❌ Believing Random Forest never overfits

Although Random Forest reduces overfitting, it is still possible if parameters are poorly chosen.

---

### ❌ Ignoring Hyperparameter Tuning

Parameters such as:

- n_estimators
- max_depth
- min_samples_split

can significantly affect performance.

---

# 💻 Python Example

```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print(prediction)
```

---

# 💼 Interview Questions

## Q1. What is Random Forest?

**Answer**

Random Forest is an ensemble learning algorithm that combines multiple Decision Trees to improve prediction accuracy and reduce overfitting.

---

## Q2. What is Bagging?

**Answer**

Bagging (Bootstrap Aggregating) creates multiple bootstrap samples from the training data and trains a separate Decision Tree on each sample.

---

## Q3. What is Bootstrap Sampling?

**Answer**

Bootstrap Sampling randomly selects observations from the dataset with replacement to create different training datasets.

---

## Q4. Why is Random Forest better than a Decision Tree?

| Decision Tree | Random Forest |
|---------------|---------------|
| One tree | Many trees |
| More prone to overfitting | Less prone to overfitting |
| Lower accuracy | Higher accuracy |
| Easy to interpret | Harder to interpret |

---

## Q5. What is Feature Importance?

**Answer**

Feature Importance measures how much each feature contributes to the model's predictions, helping identify the most influential variables.

---

# ✅ Summary

Today you learned:

- Random Forest
- Ensemble Learning
- Bagging
- Bootstrap Sampling
- Voting Mechanism
- Feature Importance
- Number of Trees
- Out-of-Bag Error
- Advantages of Random Forest
- Limitations of Random Forest

Random Forest is one of the most reliable machine learning algorithms and is widely used in real-world applications due to its high accuracy and robustness.
