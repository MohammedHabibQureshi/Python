# Day 23: Logistic Regression

⬅️ Previous: [Day 22](../Day-22-Linear-Regression/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 24](../Day-24-K-Nearest-Neighbors-KNN/README.md)

---

# 📌 Overview

Logistic Regression is a supervised Machine Learning algorithm used for **classification problems**. Instead of predicting continuous values like Linear Regression, it predicts the probability that an input belongs to a particular class.

It is mainly used for **binary classification**, where the output has only two possible classes.

Examples:

- Spam or Not Spam
- Disease or Healthy
- Fraud or Not Fraud
- Pass or Fail
- Purchased or Not Purchased

---

# Why Logistic Regression?

Logistic Regression helps us:

- Predict categories
- Estimate probabilities
- Solve binary classification problems
- Build simple and interpretable models

Applications include:

- Email Spam Detection
- Customer Churn Prediction
- Disease Prediction
- Credit Card Fraud Detection
- Loan Approval Prediction

---

# 1. Classification

## 📖 Definition

Classification is a supervised learning task where the output belongs to predefined categories.

## 🎯 Purpose

Predict class labels instead of numerical values.

## 💻 Example

Input:

```text
Age = 35
Income = ₹50,000
```

Output:

```text
Purchased = Yes
```

---

# 2. Logistic Regression

## 📖 Definition

Logistic Regression predicts the probability of an observation belonging to a class using the Sigmoid Function.

## 🎯 Purpose

Perform binary classification.

## 📝 Syntax

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
```

---

# 3. Binary Classification

## 📖 Definition

Binary Classification means there are only two possible output classes.

## 🎯 Purpose

Classify observations into one of two groups.

## 💻 Example

```text
0 → No

1 → Yes
```

---

# 4. Sigmoid Function

## 📖 Definition

The Sigmoid Function converts any real number into a probability between 0 and 1.

## 🎯 Purpose

Generate probability values for classification.

## Formula

```text
P = 1 / (1 + e^(-z))
```

Range:

```text
0 ≤ P ≤ 1
```

---

# 5. Decision Boundary

## 📖 Definition

The Decision Boundary separates one class from another.

## 🎯 Purpose

Convert predicted probabilities into class labels.

Common Threshold:

```text
Probability ≥ 0.5 → Class 1

Probability < 0.5 → Class 0
```

---

# 6. Odds

## 📖 Definition

Odds represent the ratio of the probability that an event occurs to the probability that it does not occur.

## 🎯 Purpose

Express probabilities in ratio form.

## Formula

```text
Odds = P / (1 − P)
```

---

# 7. Log Odds (Logit)

## 📖 Definition

Log Odds is the logarithm of the odds.

## 🎯 Purpose

Transform probabilities into values that range from negative infinity to positive infinity.

## Formula

```text
Logit = ln(P / (1 − P))
```

---

# 8. Model Training

## 📖 Definition

The process of learning from historical labeled data.

## 🎯 Purpose

Allow the algorithm to identify patterns.

## 📝 Syntax

```python
model.fit(X_train, y_train)
```

---

# 9. Prediction

## 📖 Definition

Predict the class of unseen data.

## 🎯 Purpose

Classify new observations.

## 📝 Syntax

```python
model.predict(X_test)
```

Predict probabilities:

```python
model.predict_proba(X_test)
```

---

# 10. Log Loss

## 📖 Definition

Log Loss measures how well the predicted probabilities match the actual class labels.

## 🎯 Purpose

Evaluate classification models.

Lower Log Loss indicates a better model.

---

# 🌍 Real-World Use Case

A bank wants to predict whether a customer will default on a loan.

Features:

- Age
- Income
- Credit Score

Target:

```text
1 → Default

0 → No Default
```

The Logistic Regression model predicts the probability of loan default, helping banks make informed lending decisions.

---

# ⚠️ Common Mistakes

### ❌ Using Logistic Regression for predicting continuous values

Wrong Example:

```text
Predict House Price
```

Correct:

Use Linear Regression.

---

### ❌ Using Linear Regression for binary classification

Wrong Example:

```text
Predict Pass or Fail
```

Correct:

Use Logistic Regression.

---

# 💻 Python Example

```python
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = load_breast_cancer()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=10000)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print(prediction[:10])
```

---

# 💼 Interview Questions

## Q1. What is Logistic Regression?

**Answer**

Logistic Regression is a supervised machine learning algorithm used for classification problems by predicting the probability of class membership.

---

## Q2. Why is Logistic Regression called Regression?

**Answer**

It uses a regression equation internally to estimate probabilities, but its final output is used for classification.

---

## Q3. What is the Sigmoid Function?

**Answer**

The Sigmoid Function converts any real-valued number into a probability between 0 and 1.

---

## Q4. Difference between Linear Regression and Logistic Regression?

| Linear Regression | Logistic Regression |
|------------------|---------------------|
| Predicts numerical values | Predicts categories |
| Continuous output | Binary/Categorical output |
| Straight line | Sigmoid curve |
| Uses MSE | Uses Log Loss |

---

## Q5. What is Log Loss?

**Answer**

Log Loss measures the performance of a classification model by comparing predicted probabilities with actual class labels. Lower values indicate better performance.

---

# ✅ Summary

Today you learned:

- Classification
- Logistic Regression
- Binary Classification
- Sigmoid Function
- Decision Boundary
- Odds
- Log Odds
- Model Training
- Prediction
- Log Loss

Logistic Regression is one of the simplest and most effective algorithms for solving binary classification problems.
