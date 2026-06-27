# Day 27: K-Means Clustering

⬅️ Previous: [Day 26](../Day-26-Random-Forest/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 28](../Day-28-PCA/README.md)

---

# 📌 Overview

K-Means Clustering is an unsupervised machine learning algorithm used to divide a dataset into K distinct groups (clusters).

Unlike supervised learning, K-Means does not require labeled data. It groups similar data points based on their distance from cluster centers (centroids).

---

# Why K-Means Clustering?

K-Means helps us:

- Discover hidden patterns
- Group similar customers or products
- Perform market segmentation
- Reduce data complexity
- Detect anomalies

Applications include:

- Customer Segmentation
- Image Compression
- Document Clustering
- Recommendation Systems
- Fraud Detection

---

# 1. Unsupervised Learning

## 📖 Definition

Unsupervised Learning is a type of machine learning where the model learns patterns from unlabeled data.

## 🎯 Purpose

Discover hidden structures or relationships within the data.

## 💻 Example

Customer data without labels is grouped based on purchasing behavior.

---

# 2. K-Means Clustering

## 📖 Definition

K-Means is an algorithm that partitions data into K clusters by minimizing the distance between data points and their assigned cluster centroid.

## 🎯 Purpose

Group similar observations into clusters.

## 📝 Syntax

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3, random_state=42)
```

---

# 3. Cluster

## 📖 Definition

A cluster is a group of similar data points.

## 🎯 Purpose

Organize similar observations together.

## 💻 Example

```text
Cluster 1 → Students

Cluster 2 → Working Professionals

Cluster 3 → Senior Citizens
```

---

# 4. Centroid

## 📖 Definition

A centroid is the center point of a cluster.

## 🎯 Purpose

Represent the average position of all points in a cluster.

## 📝 Syntax

```python
model.cluster_centers_
```

---

# 5. Number of Clusters (K)

## 📖 Definition

K specifies the number of clusters to create.

## 🎯 Purpose

Control how the data is grouped.

## Example

```text
K = 3

Cluster 1

Cluster 2

Cluster 3
```

---

# 6. Euclidean Distance

## 📖 Definition

Euclidean Distance measures the straight-line distance between two points.

## 🎯 Purpose

Assign data points to the nearest centroid.

## Formula

```text
Distance = √((x₂-x₁)² + (y₂-y₁)²)
```

---

# 7. Inertia (WCSS)

## 📖 Definition

Inertia, also called Within-Cluster Sum of Squares (WCSS), measures the total squared distance between data points and their cluster centroids.

## 🎯 Purpose

Evaluate clustering quality.

Lower Inertia indicates better clustering.

## 📝 Syntax

```python
model.inertia_
```

---

# 8. Elbow Method

## 📖 Definition

The Elbow Method helps determine the optimal number of clusters.

## 🎯 Purpose

Select the best K value.

### Steps

1. Train K-Means for different values of K.
2. Calculate Inertia (WCSS).
3. Plot K vs Inertia.
4. Choose the point where the graph forms an "elbow."

---

# 9. Silhouette Score

## 📖 Definition

Silhouette Score measures how well each data point fits within its assigned cluster.

## 🎯 Purpose

Evaluate clustering quality.

### Range

```text
-1 → Poor Clustering

0 → Overlapping Clusters

1 → Excellent Clustering
```

---

# 10. Advantages and Limitations

## ✅ Advantages

- Simple and fast
- Easy to implement
- Works well with large datasets
- Efficient for spherical clusters

## ❌ Limitations

- Must choose K beforehand
- Sensitive to outliers
- Sensitive to centroid initialization
- Performs poorly with irregular cluster shapes

---

# 🌍 Real-World Use Case

An e-commerce company wants to group customers based on:

- Annual Income
- Spending Score

K-Means identifies customer segments such as:

- Premium Customers
- Regular Customers
- Budget Customers

The marketing team can then create personalized campaigns for each group.

---

# ⚠️ Common Mistakes

### ❌ Choosing the wrong K value

Always use the Elbow Method or Silhouette Score to determine an appropriate number of clusters.

---

### ❌ Ignoring Feature Scaling

Distance-based algorithms require standardized data.

---

### ❌ Assuming K-Means works for every dataset

K-Means performs best when clusters are roughly spherical and similar in size.

---

# 💻 Python Example

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()

X = iris.data

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

model.fit(X)

print(model.labels_)
print(model.cluster_centers_)
```

---

# 💼 Interview Questions

## Q1. What is K-Means Clustering?

**Answer**

K-Means is an unsupervised machine learning algorithm that groups similar data points into K clusters based on distance.

---

## Q2. What is a Centroid?

**Answer**

A centroid is the center of a cluster and represents the average position of all points assigned to that cluster.

---

## Q3. What is Inertia (WCSS)?

**Answer**

Inertia measures the total squared distance between data points and their assigned centroid. Lower values indicate tighter clusters.

---

## Q4. What is the Elbow Method?

**Answer**

The Elbow Method helps determine the optimal number of clusters by plotting Inertia against different values of K.

---

## Q5. Why is Feature Scaling important in K-Means?

**Answer**

K-Means uses distance calculations. Without feature scaling, features with larger values dominate the clustering process.

---

# ✅ Summary

Today you learned:

- Unsupervised Learning
- K-Means Clustering
- Cluster
- Centroid
- Number of Clusters (K)
- Euclidean Distance
- Inertia (WCSS)
- Elbow Method
- Silhouette Score
- Advantages and Limitations

K-Means is one of the most widely used clustering algorithms for discovering hidden patterns in unlabeled data.
