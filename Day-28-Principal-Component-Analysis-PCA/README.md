# Day 28: Principal Component Analysis (PCA)

⬅️ Previous: [Day 27](../Day-27-K-Means-Clustering/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 29](../Day-29-Model-Saving-and-Hyperparameter-Tuning/README.md)

---

# 📌 Overview

Principal Component Analysis (PCA) is an unsupervised machine learning technique used for dimensionality reduction.

It transforms a dataset with many features into a smaller set of new features called Principal Components while preserving most of the original information.

PCA is widely used for:

- Data Compression
- Feature Extraction
- Data Visualization
- Noise Reduction
- Improving Machine Learning Performance

---

# Why PCA?

PCA helps us:

- Reduce the number of features
- Speed up model training
- Remove redundant information
- Reduce overfitting
- Visualize high-dimensional datasets

Applications include:

- Face Recognition
- Image Compression
- Bioinformatics
- Financial Analysis
- Recommendation Systems

---

# 1. Principal Component Analysis (PCA)

## 📖 Definition

PCA is a statistical technique that transforms correlated variables into a smaller number of uncorrelated variables called Principal Components.

## 🎯 Purpose

Reduce dimensionality while preserving maximum information.

## 📝 Syntax

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
```

---

# 2. Dimensionality Reduction

## 📖 Definition

Dimensionality Reduction reduces the number of input features while retaining important information.

## 🎯 Purpose

Simplify datasets and improve model efficiency.

## 💻 Example

```text
Original Features:

Age
Salary
Experience
Education
City

↓

Reduced Features:

PC1
PC2
```

---

# 3. Principal Components

## 📖 Definition

Principal Components are new features created by combining the original features.

## 🎯 Purpose

Capture the maximum variance in the dataset.

Example:

```text
Original Features

↓

Principal Component 1

↓

Principal Component 2
```

---

# 4. Explained Variance

## 📖 Definition

Explained Variance measures how much information each Principal Component preserves.

## 🎯 Purpose

Select the most informative components.

## 📝 Syntax

```python
pca.explained_variance_ratio_
```

---

# 5. Eigenvectors

## 📖 Definition

Eigenvectors determine the direction of the Principal Components.

## 🎯 Purpose

Define the new feature axes.

---

# 6. Eigenvalues

## 📖 Definition

Eigenvalues represent the amount of variance captured by each Principal Component.

## 🎯 Purpose

Measure the importance of each Principal Component.

Higher Eigenvalue → More Information

---

# 7. Feature Extraction

## 📖 Definition

Feature Extraction creates new features from the existing features.

## 🎯 Purpose

Reduce redundancy and improve learning.

PCA is a Feature Extraction technique.

---

# 8. Feature Scaling Before PCA

## 📖 Definition

Feature Scaling standardizes features before applying PCA.

## 🎯 Purpose

Ensure all features contribute equally.

## 📝 Syntax

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

---

# 9. Choosing the Number of Components

## 📖 Definition

The number of Principal Components determines how much information is retained.

## 🎯 Purpose

Balance dimensionality reduction and information preservation.

Example:

```text
95% Explained Variance

↓

Choose enough Principal Components to retain at least 95% of the variance.
```

---

# 10. Advantages and Limitations

## ✅ Advantages

- Reduces dimensionality
- Faster model training
- Removes correlated features
- Reduces overfitting
- Improves visualization

## ❌ Limitations

- Reduced interpretability
- Information loss
- Sensitive to feature scaling
- Assumes linear relationships

---

# 🌍 Real-World Use Case

A facial recognition system processes images with thousands of pixel values.

Using PCA:

- Thousands of pixel features are reduced to a few hundred Principal Components.
- The model trains faster.
- Storage requirements decrease.
- Recognition accuracy remains high.

---

# ⚠️ Common Mistakes

### ❌ Applying PCA without Feature Scaling

Features with larger values dominate the Principal Components.

---

### ❌ Choosing too few components

Too much information may be lost.

---

### ❌ Assuming PCA selects original features

PCA creates **new features**, not a subset of existing ones.

---

# 💻 Python Example

```python
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()

X = iris.data

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

print(X_pca)

print(pca.explained_variance_ratio_)
```

---

# 💼 Interview Questions

## Q1. What is PCA?

**Answer**

PCA is an unsupervised learning technique used to reduce the number of features while preserving maximum variance.

---

## Q2. Why do we use PCA?

**Answer**

To reduce dimensionality, improve model performance, remove correlated features, and visualize high-dimensional data.

---

## Q3. What are Principal Components?

**Answer**

Principal Components are new uncorrelated features that capture the maximum variance from the original dataset.

---

## Q4. Why is Feature Scaling important before PCA?

**Answer**

PCA depends on variance. Without feature scaling, features with larger values dominate the Principal Components.

---

## Q5. What is Explained Variance?

**Answer**

Explained Variance indicates how much information each Principal Component retains from the original dataset.

---

# ✅ Summary

Today you learned:

- Principal Component Analysis (PCA)
- Dimensionality Reduction
- Principal Components
- Explained Variance
- Eigenvectors
- Eigenvalues
- Feature Extraction
- Feature Scaling
- Choosing the Number of Components
- Advantages and Limitations

PCA is one of the most important dimensionality reduction techniques and is widely used to improve machine learning performance and visualize high-dimensional data.
