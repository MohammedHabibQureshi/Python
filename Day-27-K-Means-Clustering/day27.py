from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Load Dataset
iris = load_iris()
X = iris.data

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train K-Means Model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

model.fit(X_scaled)

# Cluster Labels
labels = model.labels_

# Evaluation
print("Cluster Labels:")
print(labels)

print("\nCluster Centers:")
print(model.cluster_centers_)

print("\nInertia (WCSS):", model.inertia_)

print("Silhouette Score:", silhouette_score(X_scaled, labels))

# Elbow Method
wcss = []

for k in range(1, 11):
    km = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    km.fit(X_scaled)
    wcss.append(km.inertia_)

plt.figure(figsize=(8,5))
plt.plot(range(1,11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.grid(True)
plt.savefig("elbow_method.png")
plt.show()
