# Day 16: Statistics for Data Science

⬅️ Previous: [Day 15](../Day-15-Advanced-Data-Visualization/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 17](../Day-17-Probability-and-Distributions/README.md)

---

# 📌 Overview

Statistics is the science of collecting, organizing, analyzing, interpreting, and presenting data.

In Data Science, statistics helps us:

- Understand datasets
- Find hidden patterns
- Make predictions
- Support business decisions
- Build Machine Learning models

---

# Why Statistics?

Statistics helps answer questions like:

- What is the average salary?
- Which product sells the most?
- How much variation exists in sales?
- Which customers spend more than average?

Without statistics, data has very little meaning.

---

# 1. Mean (Average)

## 📖 Definition

The mean is the average of all values in a dataset.

## 🎯 Purpose

Measure the central value of data.

## 📝 Syntax

```python
np.mean(data)
```

## 💻 Example

```python
import numpy as np

marks = [80,85,90,95]

print(np.mean(marks))
```

Output

```text
87.5
```

---

# 2. Median

## 📖 Definition

The median is the middle value after arranging the data in ascending order.

## 🎯 Purpose

Find the center of skewed data.

## 📝 Syntax

```python
np.median(data)
```

## 💻 Example

```python
marks = [70,80,90,100,95]

print(np.median(marks))
```

Output

```text
90.0
```

---

# 3. Mode

## 📖 Definition

The mode is the value that appears most frequently in a dataset.

## 🎯 Purpose

Identify the most common value.

## 📝 Syntax

```python
statistics.mode(data)
```

## 💻 Example

```python
from statistics import mode

numbers = [1,2,2,3,4]

print(mode(numbers))
```

Output

```text
2
```

---

# 4. Range

## 📖 Definition

The range is the difference between the maximum and minimum values.

## 🎯 Purpose

Measure the spread of data.

## 📝 Syntax

```python
max(data) - min(data)
```

## 💻 Example

```python
marks = [70,80,90,100]

print(max(marks)-min(marks))
```

Output

```text
30
```

---

# 5. Variance

## 📖 Definition

Variance measures how far each value is from the mean.

## 🎯 Purpose

Understand data dispersion.

## 📝 Syntax

```python
np.var(data)
```

## 💻 Example

```python
import numpy as np

marks = [80,85,90,95]

print(np.var(marks))
```

---

# 6. Standard Deviation

## 📖 Definition

Standard deviation measures the average spread of values around the mean.

## 🎯 Purpose

Measure consistency of data.

## 📝 Syntax

```python
np.std(data)
```

## 💻 Example

```python
print(np.std(marks))
```

---

# 7. Minimum Value

## 📖 Definition

Returns the smallest value in the dataset.

## 🎯 Purpose

Identify the lowest observation.

## 📝 Syntax

```python
np.min(data)
```

## 💻 Example

```python
print(np.min(marks))
```

---

# 8. Maximum Value

## 📖 Definition

Returns the largest value in the dataset.

## 🎯 Purpose

Identify the highest observation.

## 📝 Syntax

```python
np.max(data)
```

## 💻 Example

```python
print(np.max(marks))
```

---

# 9. Percentile

## 📖 Definition

A percentile indicates the value below which a given percentage of observations fall.

## 🎯 Purpose

Understand the distribution of data.

## 📝 Syntax

```python
np.percentile(data, percentile)
```

## 💻 Example

```python
print(np.percentile(marks, 75))
```

---

# 10. Correlation

## 📖 Definition

Correlation measures the strength and direction of the relationship between two variables.

## 🎯 Purpose

Determine whether two variables are related.

## 📝 Syntax

```python
df.corr()
```

## 💻 Example

```python
import pandas as pd

data = {
    "Hours":[1,2,3,4,5],
    "Marks":[40,50,65,80,95]
}

df = pd.DataFrame(data)

print(df.corr())
```

---

# 🌍 Real-World Use Case

A school wants to analyze student performance.

Using statistics, they can:

- Find average marks.
- Identify the highest and lowest scores.
- Measure score consistency.
- Determine whether study hours affect marks.

These insights help improve academic performance.

---

# ⚠️ Common Mistakes

### ❌ Confusing Mean and Median

Mean is affected by extreme values (outliers).

Example:

```text
10, 20, 30, 500
```

Mean = 140

Median = 25

The median better represents the center when outliers are present.

---

# 💼 Interview Questions

## Q1. Difference between Mean and Median?

| Mean | Median |
|------|---------|
| Average of all values | Middle value |
| Affected by outliers | Less affected by outliers |

---

## Q2. Difference between Variance and Standard Deviation?

| Variance | Standard Deviation |
|-----------|--------------------|
| Square of deviations | Square root of variance |
| Unit is squared | Same unit as the data |

---

## Q3. What is Correlation?

**Answer**

Correlation measures how strongly two variables are related.

- Positive Correlation → Both increase together.
- Negative Correlation → One increases while the other decreases.
- Zero Correlation → No relationship.

---

# ✅ Summary

Today you learned:

- Mean
- Median
- Mode
- Range
- Variance
- Standard Deviation
- Minimum
- Maximum
- Percentile
- Correlation

These statistical measures form the foundation of data analysis and machine learning.
