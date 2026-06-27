# Day 18: Hypothesis Testing

⬅️ Previous: [Day 17](../Day-17-Probability-and-Distributions/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 19](../Day-19-Feature-Engineering/README.md)

---

# 📌 Overview

Hypothesis Testing is a statistical method used to determine whether there is enough evidence in a sample to support a claim about a population.

It helps answer questions such as:

- Does a new medicine work better?
- Does a marketing campaign increase sales?
- Is a machine producing defective products?
- Is there a significant difference between two groups?

---

# Why Hypothesis Testing?

It helps us make data-driven decisions instead of relying on assumptions.

Applications include:

- Medical Research
- Business Analytics
- Machine Learning
- Quality Control
- Finance
- Marketing

---

# 1. Hypothesis

## 📖 Definition

A hypothesis is an assumption or statement that can be tested using statistical methods.

## 🎯 Purpose

Provide a claim that can be accepted or rejected.

## 💻 Example

"The average salary of employees is ₹50,000."

---

# 2. Null Hypothesis (H₀)

## 📖 Definition

The Null Hypothesis states that there is **no significant difference** or **no relationship** between variables.

## 🎯 Purpose

Acts as the default assumption.

## 💻 Example

```text
H₀: The new teaching method does not improve student marks.
```

---

# 3. Alternative Hypothesis (H₁)

## 📖 Definition

The Alternative Hypothesis states that a significant difference or relationship exists.

## 🎯 Purpose

Represents the claim we want to prove.

## 💻 Example

```text
H₁: The new teaching method improves student marks.
```

---

# 4. Significance Level (α)

## 📖 Definition

The significance level is the maximum probability of rejecting a true Null Hypothesis.

Common values are:

- 0.05
- 0.01

## 🎯 Purpose

Determine the threshold for decision-making.

## 💻 Example

```text
α = 0.05
```

Meaning there is a 5% risk of making a wrong decision.

---

# 5. P-value

## 📖 Definition

The p-value measures the probability of obtaining the observed result if the Null Hypothesis is true.

## 🎯 Purpose

Help decide whether to reject or accept the Null Hypothesis.

## Decision Rule

If

```text
p-value < α
```

Reject H₀

If

```text
p-value ≥ α
```

Fail to reject H₀

---

# 6. Type I Error

## 📖 Definition

Rejecting a true Null Hypothesis.

## 🎯 Purpose

Understand false positives.

## 💻 Example

A medical test says a healthy person has a disease.

---

# 7. Type II Error

## 📖 Definition

Failing to reject a false Null Hypothesis.

## 🎯 Purpose

Understand false negatives.

## 💻 Example

A medical test reports that a sick person is healthy.

---

# 8. Z-Test

## 📖 Definition

A Z-Test compares sample and population means when:

- Sample size is large (n ≥ 30)
- Population variance is known

## 🎯 Purpose

Determine whether a sample differs significantly from the population.

## 💻 Example

Testing whether the average salary differs from ₹50,000.

---

# 9. T-Test

## 📖 Definition

A T-Test compares means when:

- Sample size is small
- Population variance is unknown

## 🎯 Purpose

Compare two groups.

## Types

- One Sample T-Test
- Independent T-Test
- Paired T-Test

---

# 10. Chi-Square Test

## 📖 Definition

The Chi-Square Test determines whether two categorical variables are related.

## 🎯 Purpose

Test independence between categories.

## 💻 Example

Relationship between:

- Gender
- Product Preference

---

# 🌍 Real-World Use Case

A company launches a new website.

Old conversion rate:

```text
10%
```

New conversion rate:

```text
13%
```

Hypothesis Testing determines whether the increase is statistically significant or happened by chance.

---

# ⚠️ Common Mistakes

### ❌ Assuming a small p-value proves the alternative hypothesis.

A small p-value only provides evidence against the Null Hypothesis.

---

### ❌ Confusing Type I and Type II Errors.

Remember:

- Type I → False Positive
- Type II → False Negative

---

# 💻 Python Example

```python
from scipy.stats import ttest_ind

group1 = [70,75,80,85,90]
group2 = [65,68,72,74,78]

t_stat, p_value = ttest_ind(group1, group2)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")
```

---

# 💼 Interview Questions

## Q1. What is Hypothesis Testing?

**Answer**

Hypothesis Testing is a statistical method used to determine whether there is enough evidence to support a claim about a population.

---

## Q2. What is the difference between Null and Alternative Hypothesis?

| Null Hypothesis | Alternative Hypothesis |
|-----------------|------------------------|
| No difference | Significant difference |
| Default assumption | Research claim |

---

## Q3. What is a p-value?

**Answer**

The p-value is the probability of observing the obtained results assuming the Null Hypothesis is true.

---

## Q4. Difference between Z-Test and T-Test?

| Z-Test | T-Test |
|---------|---------|
| Large sample | Small sample |
| Population variance known | Population variance unknown |
| Uses Normal Distribution | Uses T Distribution |

---

## Q5. What are Type I and Type II Errors?

| Type I Error | Type II Error |
|---------------|---------------|
| False Positive | False Negative |
| Reject true H₀ | Accept false H₀ |

---

# ✅ Summary

Today you learned:

- Hypothesis
- Null Hypothesis
- Alternative Hypothesis
- Significance Level
- P-value
- Type I Error
- Type II Error
- Z-Test
- T-Test
- Chi-Square Test

These concepts are fundamental in statistical analysis, A/B testing, machine learning, business analytics, and scientific research.
