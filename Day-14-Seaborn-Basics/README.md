# Day 14: Seaborn Basics

⬅️ Previous: [Day 13](../Day-13-Data-Visualization/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 15](../Day-15-Data-Visualization-Advanced/README.md)

---

# 📌 Overview

Seaborn is a Python data visualization library built on top of Matplotlib. It provides an easy interface for creating attractive and informative statistical graphics.

Seaborn integrates well with Pandas DataFrames and is widely used in Exploratory Data Analysis (EDA).

---

# Why Seaborn?

Compared to Matplotlib, Seaborn offers:

- Beautiful default themes
- Less code
- Statistical plots
- Better integration with Pandas
- Easy customization

---

# 1. Import Seaborn

## 📖 Definition

Import the Seaborn library before creating visualizations.

## 🎯 Purpose

Access Seaborn plotting functions.

## 📝 Syntax

```python
import seaborn as sns
```

## 💻 Example

```python
import seaborn as sns

print(sns.__version__)
```

---

# 2. Load Dataset

## 📖 Definition

Seaborn can load built-in datasets for visualization.

## 🎯 Purpose

Practice without creating datasets manually.

## 📝 Syntax

```python
sns.load_dataset("dataset_name")
```

## 💻 Example

```python
import seaborn as sns

tips = sns.load_dataset("tips")

print(tips.head())
```

---

# 3. Scatter Plot

## 📖 Definition

Displays the relationship between two numerical variables.

## 🎯 Purpose

Identify trends and correlations.

## 📝 Syntax

```python
sns.scatterplot(data=df, x="column1", y="column2")
```

## 💻 Example

```python
sns.scatterplot(data=tips, x="total_bill", y="tip")
```

---

# 4. Line Plot

## 📖 Definition

Shows trends using connected data points.

## 🎯 Purpose

Visualize changes over time.

## 📝 Syntax

```python
sns.lineplot(data=df, x="column1", y="column2")
```

## 💻 Example

```python
sns.lineplot(data=tips, x="size", y="tip")
```

---

# 5. Bar Plot

## 📖 Definition

Displays the average value of a numerical variable for different categories.

## 🎯 Purpose

Compare categories.

## 📝 Syntax

```python
sns.barplot(data=df, x="column1", y="column2")
```

## 💻 Example

```python
sns.barplot(data=tips, x="day", y="total_bill")
```

---

# 6. Count Plot

## 📖 Definition

Displays the frequency of each category.

## 🎯 Purpose

Count occurrences of categorical values.

## 📝 Syntax

```python
sns.countplot(data=df, x="column")
```

## 💻 Example

```python
sns.countplot(data=tips, x="day")
```

---

# 7. Histogram

## 📖 Definition

Displays the distribution of a numerical variable.

## 🎯 Purpose

Understand how data is distributed.

## 📝 Syntax

```python
sns.histplot(data=df, x="column")
```

## 💻 Example

```python
sns.histplot(data=tips, x="total_bill")
```

---

# 8. Box Plot

## 📖 Definition

Shows the distribution, median, quartiles, and outliers of data.

## 🎯 Purpose

Identify spread and detect outliers.

## 📝 Syntax

```python
sns.boxplot(data=df, x="column")
```

## 💻 Example

```python
sns.boxplot(data=tips, x="total_bill")
```

---

# 9. Heatmap

## 📖 Definition

Displays values as colors in a matrix.

## 🎯 Purpose

Visualize correlation and relationships.

## 📝 Syntax

```python
sns.heatmap(data)
```

## 💻 Example

```python
corr = tips.corr(numeric_only=True)

sns.heatmap(corr, annot=True)
```

---

# 10. Change Theme

## 📖 Definition

Seaborn themes improve the appearance of plots.

## 🎯 Purpose

Create professional-looking visualizations.

## 📝 Syntax

```python
sns.set_style("style")
```

## 💻 Example

```python
sns.set_style("darkgrid")
```

Available styles:

- darkgrid
- whitegrid
- dark
- white
- ticks

---

# 🌍 Real-World Use Case

A restaurant wants to analyze customer spending.

Using Seaborn, they can:

- Compare bills across different days.
- Analyze tip distribution.
- Detect unusual customer spending.
- Visualize relationships between bill amount and tips.

---

# ⚠️ Common Mistakes

### ❌ Forgetting to display the plot

```python
sns.barplot(data=tips, x="day", y="total_bill")
```

### ✅ Correct

```python
sns.barplot(data=tips, x="day", y="total_bill")

plt.show()
```

---

# 💼 Interview Questions

## Q1. What is Seaborn?

**Answer**

Seaborn is a Python visualization library built on top of Matplotlib that provides attractive statistical graphics.

---

## Q2. Difference between Matplotlib and Seaborn?

| Matplotlib | Seaborn |
|------------|----------|
| Basic plotting library | Built on Matplotlib |
| More customization required | Better default styling |
| More code | Less code |
| General-purpose plotting | Statistical visualization |

---

## Q3. What is a Heatmap?

**Answer**

A Heatmap is a graphical representation of data where values are represented by different colors. It is commonly used to visualize correlation matrices.

---

# ✅ Summary

Today you learned:

- Import Seaborn
- Load Dataset
- Scatter Plot
- Line Plot
- Bar Plot
- Count Plot
- Histogram
- Box Plot
- Heatmap
- Themes

Seaborn simplifies statistical data visualization and is widely used in Exploratory Data Analysis (EDA) and Machine Learning.
