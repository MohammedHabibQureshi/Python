import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [120, 180, 160, 210]

# Figure Size
plt.figure(figsize=(8, 5))

# Line Plot with Marker and Grid
plt.plot(months, sales, marker="o", linestyle="--", label="Sales")

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()

# Annotation
plt.annotate("Highest Sales", ("Apr", 210))

# Save Figure
plt.savefig("line_plot.png")

plt.show()

# -----------------------------

tips = sns.load_dataset("tips")

plt.figure(figsize=(10, 5))

# Subplot 1
plt.subplot(1, 2, 1)

sns.boxplot(data=tips, x="day", y="total_bill")

plt.title("Box Plot")

# Subplot 2
plt.subplot(1, 2, 2)

sns.violinplot(data=tips, x="day", y="total_bill")

plt.title("Violin Plot")

plt.tight_layout()

plt.savefig("subplot.png")

plt.show()
