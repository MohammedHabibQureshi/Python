# Day 29: Model Saving & Hyperparameter Tuning

⬅️ Previous: [Day 28](../Day-28-Principal-Component-Analysis-PCA/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 30](../Day-30-Machine-Learning-Pipeline/README.md)

---

# 📌 Overview

After building a Machine Learning model, we usually don't want to train it every time we use it.

Instead, we save the trained model to a file and load it whenever needed.

We also improve model performance by finding the best hyperparameters using Hyperparameter Tuning.

---

# Why Learn This?

Model Saving helps us:

- Deploy ML models
- Avoid retraining
- Save computation time
- Reuse trained models

Hyperparameter Tuning helps us:

- Improve model accuracy
- Find optimal settings
- Reduce overfitting
- Build better ML models

---

# 1. Model Saving

## 📖 Definition

Model Saving stores a trained machine learning model so it can be reused later without retraining.

## 🎯 Purpose

Save training time and deploy models.

---

# 2. Pickle

## 📖 Definition

Pickle is a Python module used to serialize and deserialize Python objects.

## 🎯 Purpose

Save and load trained models.

## 📝 Syntax

```python
import pickle

pickle.dump(model, open("model.pkl", "wb"))
```

Load model:

```python
model = pickle.load(open("model.pkl", "rb"))
```

---

# 3. Joblib

## 📖 Definition

Joblib is a library designed for efficiently saving and loading large Python objects.

## 🎯 Purpose

Store machine learning models efficiently.

## 📝 Syntax

```python
import joblib

joblib.dump(model, "model.joblib")
```

Load model:

```python
model = joblib.load("model.joblib")
```

---

# 4. Hyperparameters

## 📖 Definition

Hyperparameters are configuration values set before training a machine learning model.

## 🎯 Purpose

Control how the learning algorithm works.

## Examples

```text
n_estimators

max_depth

learning_rate

n_neighbors
```

---

# 5. Hyperparameter Tuning

## 📖 Definition

Hyperparameter Tuning is the process of finding the best hyperparameter values for a model.

## 🎯 Purpose

Improve model performance.

---

# 6. GridSearchCV

## 📖 Definition

GridSearchCV tests every possible combination of specified hyperparameters.

## 🎯 Purpose

Find the best parameter combination.

## 📝 Syntax

```python
from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(
    model,
    param_grid,
    cv=5
)
```

---

# 7. RandomizedSearchCV

## 📖 Definition

RandomizedSearchCV tests a random subset of hyperparameter combinations.

## 🎯 Purpose

Reduce computation time.

## 📝 Syntax

```python
from sklearn.model_selection import RandomizedSearchCV
```

---

# 8. Cross Validation (CV)

## 📖 Definition

Cross Validation evaluates a model by dividing the dataset into multiple folds.

## 🎯 Purpose

Measure model performance more reliably.

Example:

```text
5-Fold Cross Validation

Fold 1 → Test

Fold 2 → Test

Fold 3 → Test

Fold 4 → Test

Fold 5 → Test
```

---

# 9. Best Parameters

## 📖 Definition

Best Parameters are the hyperparameter values that produce the highest model performance.

## 🎯 Purpose

Use the optimal model configuration.

## 📝 Syntax

```python
grid.best_params_
```

---

# 10. Best Score

## 📖 Definition

The highest validation score achieved during hyperparameter tuning.

## 🎯 Purpose

Evaluate the best-performing model.

## 📝 Syntax

```python
grid.best_score_
```

---

# 🌍 Real-World Use Case

An online shopping company builds a customer purchase prediction model.

Instead of training the model every day:

- The trained model is saved using Joblib.
- Hyperparameter tuning is performed using GridSearchCV.
- The optimized model is deployed to production.

---

# ⚠️ Common Mistakes

### ❌ Saving an untrained model

Always train the model before saving.

---

### ❌ Using too many GridSearch combinations

A large parameter grid can significantly increase training time.

---

### ❌ Ignoring Cross Validation

Cross Validation provides a more reliable estimate of model performance than a single train-test split.

---

# 💻 Python Example

```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

iris = load_iris()

X = iris.data
y = iris.target

model = RandomForestClassifier(random_state=42)

param_grid = {
    "n_estimators": [50,100],
    "max_depth": [2,4,6]
}

grid = GridSearchCV(
    model,
    param_grid,
    cv=5
)

grid.fit(X,y)

print(grid.best_params_)
print(grid.best_score_)
```

---

# 💼 Interview Questions

## Q1. Why do we save machine learning models?

**Answer**

To reuse trained models without retraining, making deployment faster and more efficient.

---

## Q2. Difference between Pickle and Joblib?

| Pickle | Joblib |
|---------|---------|
| General Python serialization | Optimized for large NumPy arrays and ML models |
| Slower for large models | Faster for large models |
| Built into Python | External library |

---

## Q3. What are Hyperparameters?

**Answer**

Hyperparameters are settings defined before training that control how a machine learning algorithm learns.

---

## Q4. What is GridSearchCV?

**Answer**

GridSearchCV searches through every possible combination of specified hyperparameters to find the best-performing model.

---

## Q5. Difference between GridSearchCV and RandomizedSearchCV?

| GridSearchCV | RandomizedSearchCV |
|---------------|-------------------|
| Tests all combinations | Tests random combinations |
| More accurate | Faster |
| Computationally expensive | Computationally efficient |

---

# ✅ Summary

Today you learned:

- Model Saving
- Pickle
- Joblib
- Hyperparameters
- Hyperparameter Tuning
- GridSearchCV
- RandomizedSearchCV
- Cross Validation
- Best Parameters
- Best Score

These concepts are essential for optimizing and deploying machine learning models in real-world applications.
