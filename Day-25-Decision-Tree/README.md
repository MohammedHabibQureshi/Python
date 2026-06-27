# Day 25: Decision Tree

⬅️ Previous: [Day 24](../Day-24-K-Nearest-Neighbors-KNN/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 26](../Day-26-Random-Forest/README.md)

---

# 📌 Overview

A Decision Tree is a supervised machine learning algorithm that predicts an outcome by splitting data into smaller subsets based on feature values.

It works like a flowchart where:

- Root Node → Starting point
- Internal Node → Decision point
- Branch → Outcome of a decision
- Leaf Node → Final prediction

Decision Trees are used for both Classification and Regression problems.

---

# Why Decision Trees?

Decision Trees help us:

- Make easy-to-understand decisions
- Handle numerical and categorical data
- Perform classification and regression
- Visualize decision-making

Applications include:

- Loan Approval
- Disease Diagnosis
- Fraud Detection
- Customer Churn Prediction
- Employee Performance Analysis

---

# 1. Decision Tree

## 📖 Definition

A Decision Tree is a tree-like model that makes predictions by asking a sequence of questions.

## 🎯 Purpose

Split data into smaller groups until a prediction can be made.

## 📝 Syntax

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
```

---

# 2. Root Node

## 📖 Definition

The Root Node is the topmost node of the tree where the first split occurs.

## 🎯 Purpose

Start the decision-making process.

## 💻 Example

```text
Age > 30?
```

---

# 3. Internal Node

## 📖 Definition

An Internal Node represents a decision based on a feature.

## 🎯 Purpose

Split data further.

## 💻 Example

```text
Income > ₹50,000?
```

---

# 4. Leaf Node

## 📖 Definition

A Leaf Node is the final node that gives the prediction.

## 🎯 Purpose

Provide the final class or value.

## 💻 Example

```text
Loan Approved
```

---

# 5. Entropy

## 📖 Definition

Entropy measures the amount of uncertainty or impurity in a dataset.

## 🎯 Purpose

Find the best feature for splitting data.

## Formula

```text
Entropy = -Σ P(x) log₂ P(x)
```

Entropy Range:

```text
0 → Pure Node

1 → Maximum Uncertainty
```

---

# 6. Information Gain

## 📖 Definition

Information Gain measures how much entropy decreases after a split.

## 🎯 Purpose

Choose the best feature for splitting.

## Formula

```text
Information Gain = Parent Entropy − Weighted Child Entropy
```

Higher Information Gain means a better split.

---

# 7. Gini Index

## 📖 Definition

The Gini Index measures the impurity of a dataset.

## 🎯 Purpose

Select the best feature for splitting.

## Formula

```text
Gini = 1 − Σ(P²)
```

Lower Gini means a better split.

---

# 8. Tree Depth

## 📖 Definition

Tree Depth is the maximum number of levels in a Decision Tree.

## 🎯 Purpose

Control model complexity.

Small Depth:

- Underfitting

Large Depth:

- Overfitting

---

# 9. Pruning

## 📖 Definition

Pruning removes unnecessary branches from the Decision Tree.

## 🎯 Purpose

Reduce overfitting and improve generalization.

Types:

- Pre-Pruning
- Post-Pruning

---

# 10. Feature Importance

## 📖 Definition

Feature Importance measures how much each feature contributes to predictions.

## 🎯 Purpose

Identify the most influential features.

## 💻 Example

A loan prediction model may find:

```text
Income → 60%

Credit Score → 30%

Age → 10%
```

---

# 🌍 Real-World Use Case

A bank wants to decide whether to approve a loan.

Features:

- Age
- Income
- Credit Score
- Employment Status

The Decision Tree asks questions such as:

```text
Credit Score > 700?

        Yes
         |
Income > ₹50,000?

      Yes → Loan Approved

      No → Loan Rejected
```

---

# ⚠️ Common Mistakes

### ❌ Allowing unlimited tree depth

This often leads to overfitting.

---

### ❌ Ignoring pruning

Pruning helps improve model performance on unseen data.

---

### ❌ Using noisy or irrelevant features

Irrelevant features can reduce prediction accuracy.

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

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, prediction))
```

---

# 💼 Interview Questions

## Q1. What is a Decision Tree?

**Answer**

A Decision Tree is a supervised machine learning algorithm that predicts outcomes by splitting data into smaller subsets using feature-based decisions.

---

## Q2. What is Entropy?

**Answer**

Entropy measures the impurity or uncertainty of a dataset. Lower entropy indicates purer data.

---

## Q3. What is Information Gain?

**Answer**

Information Gain measures how much uncertainty is reduced after splitting the dataset. The feature with the highest Information Gain is selected for splitting.

---

## Q4. Difference between Entropy and Gini Index?

| Entropy | Gini Index |
|----------|------------|
| Uses logarithms | Uses squared probabilities |
| Slightly slower | Faster to compute |
| Used in ID3 | Used in CART |

---

## Q5. Why is Pruning important?

**Answer**

Pruning removes unnecessary branches from the tree, reducing overfitting and improving performance on unseen data.

---

# ✅ Summary

Today you learned:

- Decision Tree
- Root Node
- Internal Node
- Leaf Node
- Entropy
- Information Gain
- Gini Index
- Tree Depth
- Pruning
- Feature Importance

Decision Trees are powerful, interpretable algorithms that form the foundation of many advanced ensemble methods such as Random Forest and Gradient Boosting.
