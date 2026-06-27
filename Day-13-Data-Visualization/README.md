# Day 13: Data Visualization (Matplotlib Basics)

⬅️ Previous: [Day 12](../Day-12-Data-Cleaning/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 14](../Day-14-Seaborn-Basics/README.md)

---

# 📌 Overview

Data Visualization is the graphical representation of data using charts and graphs. It helps identify trends, patterns, relationships, and outliers that are difficult to understand from raw data alone.

Matplotlib is one of the most popular Python libraries for creating static, animated, and interactive visualizations.

---

# Why Matplotlib?

Matplotlib is used to:

- Visualize large datasets
- Identify trends and patterns
- Compare different categories
- Present data professionally
- Support data-driven decision making

---

# 1. Import Matplotlib

## 📖 Definition

Before using Matplotlib, import the `pyplot` module.

## 🎯 Purpose

Access plotting functions.

## 📝 Syntax

```python
import matplotlib.pyplot as plt
```

## 💻 Example

```python
import matplotlib.pyplot as plt
```

---

# 2. Line Plot

## 📖 Definition

A Line Plot displays data points connected by straight lines.

## 🎯 Purpose

Show trends over time.

## 📝 Syntax

```python
plt.plot(x, y)
```

## 💻 Example

```python
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]
sales = [120,150,180,170]

plt.plot(months, sales)

plt.show()
```

---

# 3. Bar Chart

## 📖 Definition

A Bar Chart compares values across different categories.

## 🎯 Purpose

Compare categorical data.

## 📝 Syntax

```python
plt.bar(x, y)
```

## 💻 Example

```python
students = ["Ali","Sara","Habib"]

marks = [80,90,95]

plt.bar(students, marks)

plt.show()
```

---

# 4. Histogram

## 📖 Definition

A Histogram displays the frequency distribution of numerical data.

## 🎯 Purpose

Understand data distribution.

## 📝 Syntax

```python
plt.hist(data)
```

## 💻 Example

```python
ages = [18,19,20,20,21,22,22,23,24]

plt.hist(ages)

plt.show()
```

---

# 5. Scatter Plot

## 📖 Definition

A Scatter Plot shows the relationship between two numerical variables.

## 🎯 Purpose

Identify correlations and outliers.

## 📝 Syntax

```python
plt.scatter(x, y)
```

## 💻 Example

```python
hours = [1,2,3,4,5]

marks = [40,55,65,80,95]

plt.scatter(hours, marks)

plt.show()
```

---

# 6. Pie Chart

## 📖 Definition

A Pie Chart represents data as slices of a circle.

## 🎯 Purpose

Show percentage distribution.

## 📝 Syntax

```python
plt.pie(data, labels=labels)
```

## 💻 Example

```python
subjects = ["Math","Science","English"]

students = [40,35,25]

plt.pie(students, labels=subjects)

plt.show()
```

---

# 7. Title

## 📖 Definition

Adds a title to the graph.

## 🎯 Purpose

Describe the chart.

## 📝 Syntax

```python
plt.title("Title")
```

## 💻 Example

```python
plt.title("Monthly Sales")
```

---

# 8. X-axis Label

## 📖 Definition

Adds a label to the x-axis.

## 🎯 Purpose

Describe x-axis values.

## 📝 Syntax

```python
plt.xlabel("Label")
```

## 💻 Example

```python
plt.xlabel("Months")
```

---

# 9. Y-axis Label

## 📖 Definition

Adds a label to the y-axis.

## 🎯 Purpose

Describe y-axis values.

## 📝 Syntax

```python
plt.ylabel("Label")
```

## 💻 Example

```python
plt.ylabel("Sales")
```

---

# 10. Legend

## 📖 Definition

Displays labels for plotted data.

## 🎯 Purpose

Differentiate multiple datasets.

## 📝 Syntax

```python
plt.legend()
```

## 💻 Example

```python
months = ["Jan","Feb","Mar"]

sales = [120,140,160]

plt.plot(months, sales, label="Sales")

plt.legend()

plt.show()
```

---

# 🌍 Real-World Use Case

A retail company tracks monthly sales.

Using Matplotlib, they can:

- Visualize sales growth
- Compare department performance
- Analyze customer purchases
- Present reports to management

Visualization makes complex data easy to understand.

---

# ⚠️ Common Mistakes

### ❌ Forgetting `plt.show()`

```python
plt.plot(x, y)
```

The graph may not display.

### ✅ Correct

```python
plt.plot(x, y)
plt.show()
```

---

# 💼 Interview Questions

## Q1. What is Matplotlib?

**Answer**

Matplotlib is a Python library used for creating data visualizations such as line charts, bar charts, histograms, scatter plots, and pie charts.

---

## Q2. Difference between Line Plot and Scatter Plot?

| Line Plot | Scatter Plot |
|------------|--------------|
| Shows trends | Shows relationships |
| Points connected | Points are separate |

---

## Q3. Why is Data Visualization important?

**Answer**

- Simplifies complex data
- Identifies trends
- Detects outliers
- Supports business decisions
- Improves presentations

---

# ✅ Summary

Today you learned:

- Import Matplotlib
- Line Plot
- Bar Chart
- Histogram
- Scatter Plot
- Pie Chart
- Title
- X-axis Label
- Y-axis Label
- Legend

These are the fundamental visualization techniques used in Data Analysis and Machine Learning projects.
