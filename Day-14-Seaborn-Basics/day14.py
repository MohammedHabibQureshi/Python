import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
tips = sns.load_dataset("tips")

# Scatter Plot
plt.figure(figsize=(6,4))
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Total Bill vs Tip")
plt.show()

# Line Plot
plt.figure(figsize=(6,4))
sns.lineplot(data=tips, x="size", y="tip")
plt.title("Party Size vs Tip")
plt.show()

# Bar Plot
plt.figure(figsize=(6,4))
sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Average Bill by Day")
plt.show()

# Count Plot
plt.figure(figsize=(6,4))
sns.countplot(data=tips, x="day")
plt.title("Number of Customers by Day")
plt.show()

# Histogram
plt.figure(figsize=(6,4))
sns.histplot(data=tips, x="total_bill")
plt.title("Distribution of Total Bill")
plt.show()

# Box Plot
plt.figure(figsize=(6,4))
sns.boxplot(data=tips, x="total_bill")
plt.title("Box Plot of Total Bill")
plt.show()

# Heatmap
plt.figure(figsize=(6,4))
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()
