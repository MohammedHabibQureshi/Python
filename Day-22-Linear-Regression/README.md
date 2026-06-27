# Day 22: Linear Regression

⬅️ Previous: [Day 21](../Day-21-Train-Test-Split-and-Model-Evaluation/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 23](../Day-23-Logistic-Regression/README.md)

---

# 📌 Overview

Linear Regression is a supervised Machine Learning algorithm used to predict continuous numerical values by finding the best-fit line between the independent variable(s) and the dependent variable.

It assumes a linear relationship between the input features and the output.

---

# Why Linear Regression?

Linear Regression helps us:

- Predict future values
- Analyze relationships between variables
- Identify trends
- Support business decisions

Applications include:

- House Price Prediction
- Sales Forecasting
- Salary Prediction
- Stock Price Analysis
- Demand Forecasting

---

# 1. Supervised Learning

## 📖 Definition

Supervised Learning is a type of Machine Learning where the model learns using labeled data.

## 🎯 Purpose

Train the model to predict known outputs.

## 💻 Example

Input:

```text
Years of Experience
```

Output:

```text
Salary
```

---

# 2. Linear Regression

## 📖 Definition

Linear Regression finds the best straight line that represents the relationship between independent and dependent variables.

## 🎯 Purpose

Predict continuous numerical values.

## 📝 Syntax

```python
from sklearn.linear_model import LinearRegression
```

---

# 3. Independent Variable (X)

## 📖 Definition

The feature(s) used to predict the target.

## 🎯 Purpose

Provide input to the model.

## 💻 Example

```python
X = df[["Experience"]]
```

---

# 4. Dependent Variable (y)

## 📖 Definition

The value that the model predicts.

## 🎯 Purpose

Represent the expected output.

## 💻 Example

```python
y = df["Salary"]
```

---

# 5. Best Fit Line

## 📖 Definition

The line that minimizes prediction errors.

## 🎯 Purpose

Represent the relationship between variables.

## Formula

```text
y = mx + c
```

Where:

- y → Predicted value
- m → Slope
- x → Input feature
- c → Intercept

---

# 6. Model Training

## 📖 Definition

Training means teaching the model using historical data.

## 🎯 Purpose

Allow the model to learn patterns.

## 📝 Syntax

```python
model.fit(X_train, y_train)
```

---

# 7. Prediction

## 📖 Definition

Use the trained model to predict new values.

## 🎯 Purpose

Estimate unknown outputs.

## 📝 Syntax

```python
model.predict(X_test)
```

---

# 8. Mean Squared Error (MSE)

## 📖 Definition

Mean Squared Error measures the average squared difference between actual and predicted values.

## 🎯 Purpose

Measure prediction error.

## Formula

```text
MSE = Σ(Actual − Predicted)² / n
```

## 📝 Syntax

```python
from sklearn.metrics import mean_squared_error
```

---

# 9. R² Score (Coefficient of Determination)

## 📖 Definition

R² Score measures how well the regression model explains the variation in the target variable.

## 🎯 Purpose

Evaluate regression performance.

## Range

```text
0 → Poor Model

1 → Perfect Model
```

## 📝 Syntax

```python
from sklearn.metrics import r2_score
```

---

# 10. Regression Line Visualization

## 📖 Definition

A regression line visually represents the relationship between input and output variables.

## 🎯 Purpose

Understand how predictions are made.

## 💻 Example

```python
plt.scatter(X, y)

plt.plot(X, prediction)

plt.show()
```

---

# 🌍 Real-World Use Case

A company wants to predict employee salaries.

Dataset:

| Experience | Salary |
|------------|---------|
| 1 | 30000 |
| 2 | 35000 |
| 3 | 45000 |
| 5 | 65000 |

The model learns the relationship and predicts the salary of a person with 6 years of experience.

---

# ⚠️ Common Mistakes

### ❌ Using classification metrics

Do NOT use:

```python
accuracy_score()
```

Regression problems require:

- Mean Squared Error
- Mean Absolute Error
- R² Score

---

### ❌ Forgetting to reshape X

```python
X = df["Experience"]
```

Correct:

```python
X = df[["Experience"]]
```

---

# 💻 Python Example

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Experience":[1,2,3,4,5],
    "Salary":[30000,35000,45000,55000,65000]
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()

model.fit(X,y)

prediction = model.predict([[6]])

print("Predicted Salary:", prediction)
```

---

# 💼 Interview Questions

## Q1. What is Linear Regression?

**Answer**

Linear Regression is a supervised learning algorithm used to predict continuous numerical values by fitting a straight line to the data.

---

## Q2. What is the equation of Linear Regression?

**Answer**

```text
y = mx + c
```

Where:

- m = slope
- c = intercept

---

## Q3. What is the difference between Regression and Classification?

| Regression | Classification |
|------------|----------------|
| Predicts continuous values | Predicts categories |
| Example: Salary | Example: Spam Detection |

---

## Q4. What is R² Score?

**Answer**

R² Score measures how well the regression model explains the variation in the dependent variable.

---

## Q5. What is Mean Squared Error?

**Answer**

MSE measures the average squared difference between actual and predicted values. Lower MSE indicates better model performance.

---

# ✅ Summary

Today you learned:

- Supervised Learning
- Linear Regression
- Independent Variable
- Dependent Variable
- Best Fit Line
- Model Training
- Prediction
- Mean Squared Error (MSE)
- R² Score
- Regression Line Visualization

Linear Regression is the foundation of regression-based machine learning models and is widely used for predicting numerical values.
