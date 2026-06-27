# Day 15: Advanced Data Visualization

⬅️ Previous: [Day 14](../Day-14-Seaborn-Basics/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 16](../Day-16-Statistics-for-Data-Science/README.md)

---

# 📌 Overview

Advanced Data Visualization focuses on creating professional, informative, and visually appealing charts. It allows multiple charts in one figure, customizes chart appearance, and helps present insights more effectively.

These techniques are widely used in Data Science, Business Intelligence, and Dashboard Development.

---

# Why Advanced Visualization?

Advanced visualization helps to:

- Create professional reports
- Compare multiple datasets
- Improve readability
- Highlight important insights
- Build dashboards

---

# 1. Figure Size

## 📖 Definition

The `figure()` function creates a new figure and allows you to specify its size.

## 🎯 Purpose

Create charts with custom dimensions.

## 📝 Syntax

```python
plt.figure(figsize=(width, height))
```

## 💻 Example

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
```

---

# 2. Subplots

## 📖 Definition

Subplots allow multiple charts to be displayed within the same figure.

## 🎯 Purpose

Compare multiple visualizations.

## 📝 Syntax

```python
plt.subplot(rows, columns, position)
```

## 💻 Example

```python
plt.subplot(1,2,1)
plt.plot([1,2,3],[4,5,6])

plt.subplot(1,2,2)
plt.bar(["A","B"],[10,20])

plt.show()
```

---

# 3. Grid

## 📖 Definition

The `grid()` function adds grid lines to the graph.

## 🎯 Purpose

Improve chart readability.

## 📝 Syntax

```python
plt.grid(True)
```

## 💻 Example

```python
plt.plot([1,2,3],[4,5,6])

plt.grid(True)

plt.show()
```

---

# 4. Change Line Style

## 📖 Definition

Customize the appearance of plot lines.

## 🎯 Purpose

Differentiate multiple datasets.

## 📝 Syntax

```python
plt.plot(x, y, linestyle="--")
```

## 💻 Example

```python
plt.plot([1,2,3],[2,4,6], linestyle="--")
```

---

# 5. Change Marker

## 📖 Definition

Markers highlight each data point.

## 🎯 Purpose

Improve visibility of observations.

## 📝 Syntax

```python
plt.plot(x, y, marker="o")
```

## 💻 Example

```python
plt.plot([1,2,3],[5,6,7], marker="o")
```

---

# 6. Rotate X-axis Labels

## 📖 Definition

Rotates labels on the x-axis.

## 🎯 Purpose

Prevent overlapping labels.

## 📝 Syntax

```python
plt.xticks(rotation=45)
```

## 💻 Example

```python
plt.bar(["January","February","March"], [100,150,120])

plt.xticks(rotation=45)

plt.show()
```

---

# 7. Axis Limits

## 📖 Definition

Set the visible range of x-axis and y-axis.

## 🎯 Purpose

Focus on important data.

## 📝 Syntax

```python
plt.xlim(start, end)

plt.ylim(start, end)
```

## 💻 Example

```python
plt.plot([1,2,3,4],[5,8,9,10])

plt.xlim(1,4)

plt.ylim(4,11)

plt.show()
```

---

# 8. Annotation

## 📖 Definition

Annotations add explanatory text to specific points.

## 🎯 Purpose

Highlight important values.

## 📝 Syntax

```python
plt.annotate(text, (x, y))
```

## 💻 Example

```python
plt.plot([1,2,3],[4,8,6])

plt.annotate("Highest", (2,8))

plt.show()
```

---

# 9. Save Figure

## 📖 Definition

The `savefig()` function saves the graph as an image.

## 🎯 Purpose

Store charts for reports and GitHub.

## 📝 Syntax

```python
plt.savefig("filename.png")
```

## 💻 Example

```python
plt.plot([1,2,3],[4,5,6])

plt.savefig("graph.png")

plt.show()
```

---

# 10. Multiple Seaborn Charts

## 📖 Definition

Seaborn charts can also be placed inside subplots.

## 🎯 Purpose

Compare different statistical visualizations.

## 📝 Syntax

```python
plt.subplot()

sns.chart()
```

## 💻 Example

```python
import seaborn as sns

tips = sns.load_dataset("tips")

plt.subplot(1,2,1)

sns.boxplot(data=tips, x="day", y="total_bill")

plt.subplot(1,2,2)

sns.violinplot(data=tips, x="day", y="total_bill")

plt.show()
```

---

# 🌍 Real-World Use Case

A sales manager wants a monthly sales report.

Advanced visualization helps to:

- Compare sales across regions
- Display multiple charts together
- Highlight best-performing months
- Export charts for presentations

---

# ⚠️ Common Mistakes

### ❌ Saving after closing the figure

```python
plt.show()

plt.savefig("graph.png")
```

### ✅ Correct

```python
plt.savefig("graph.png")

plt.show()
```

---

# 💼 Interview Questions

## Q1. Why do we use subplots?

**Answer**

Subplots allow multiple graphs to be displayed within the same figure for easy comparison.

---

## Q2. What is the purpose of `savefig()`?

**Answer**

It saves charts as image files such as PNG, JPG, or PDF for reports and presentations.

---

## Q3. Why are annotations useful?

**Answer**

Annotations help explain important points, trends, and outliers in a graph.

---

# ✅ Summary

Today you learned:

- Figure Size
- Subplots
- Grid
- Line Style
- Marker
- Rotate Labels
- Axis Limits
- Annotation
- savefig()
- Multiple Seaborn Charts

These techniques help create professional-quality visualizations suitable for business reports, dashboards, and machine learning projects.
