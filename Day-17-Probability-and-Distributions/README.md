# Day 17: Probability & Probability Distributions

⬅️ Previous: [Day 16](../Day-16-Statistics-for-Data-Science/README.md) | 🏠 [Home](../README.md) | ➡️ Next: [Day 18](../Day-18-Hypothesis-Testing/README.md)

---

# 📌 Overview

Probability is the branch of mathematics that measures the likelihood of an event occurring. It ranges from **0 to 1**, where:

- **0** → Impossible Event
- **1** → Certain Event

Probability is widely used in:

- Machine Learning
- Data Science
- Artificial Intelligence
- Risk Analysis
- Weather Forecasting
- Medical Diagnosis

---

# Why Probability?

Probability helps answer questions like:

- What is the chance of rain tomorrow?
- What is the probability that a customer will buy a product?
- What is the likelihood of a machine failing?
- What is the probability that an email is spam?

---

# 1. Experiment

## 📖 Definition

An experiment is an action or process that produces one or more outcomes.

## 🎯 Purpose

Generate possible outcomes for analysis.

## 📝 Example

```text
Rolling a dice

Possible Outcomes:
1, 2, 3, 4, 5, 6
```

---

# 2. Sample Space

## 📖 Definition

The sample space is the set of all possible outcomes of an experiment.

## 🎯 Purpose

Represent every possible result.

## 📝 Syntax

```python
S = {possible outcomes}
```

## 💻 Example

```python
S = {1,2,3,4,5,6}

print(S)
```

Output

```text
{1,2,3,4,5,6}
```

---

# 3. Event

## 📖 Definition

An event is one or more outcomes from the sample space.

## 🎯 Purpose

Represent a condition of interest.

## 📝 Example

```text
Event = Getting an even number

E = {2,4,6}
```

---

# 4. Probability Formula

## 📖 Definition

Probability is calculated by dividing the number of favorable outcomes by the total number of possible outcomes.

## 🎯 Purpose

Measure the likelihood of an event.

## 📝 Formula

```text
P(E) = Favorable Outcomes / Total Outcomes
```

## 💻 Example

Probability of getting an even number on a dice:

```text
P(E) = 3 / 6

= 0.5
```

---

# 5. Random Variable

## 📖 Definition

A random variable is a variable whose value depends on the outcome of a random experiment.

## 🎯 Purpose

Represent numerical outcomes.

## 📝 Example

```text
X = Number shown after rolling a dice
```

Possible values:

```text
1,2,3,4,5,6
```

---

# 6. Uniform Distribution

## 📖 Definition

A probability distribution where every outcome has an equal probability.

## 🎯 Purpose

Model equally likely events.

## 📝 Example

Rolling a fair dice.

Every number has probability:

```text
1/6
```

---

# 7. Normal Distribution

## 📖 Definition

A continuous probability distribution where data is symmetrically distributed around the mean.

It is also known as the **Bell Curve**.

## 🎯 Purpose

Model naturally occurring data.

Examples:

- Height
- Weight
- IQ Scores
- Exam Marks

---

# 8. Binomial Distribution

## 📖 Definition

A probability distribution that describes the number of successes in a fixed number of independent trials.

## 🎯 Purpose

Model events with only two outcomes.

Possible outcomes:

- Success
- Failure

## 💻 Example

Tossing a coin 10 times and counting the number of heads.

---

# 9. Poisson Distribution

## 📖 Definition

Models the number of events occurring in a fixed interval of time or space.

## 🎯 Purpose

Predict rare events.

## 💻 Example

- Calls received in one hour.
- Customers entering a store.
- Accidents per day.

---

# 10. Generate Random Numbers

## 📖 Definition

NumPy provides functions to generate random values.

## 🎯 Purpose

Simulate random experiments.

## 📝 Syntax

```python
np.random.randint(start, end, size)
```

## 💻 Example

```python
import numpy as np

dice = np.random.randint(1,7,10)

print(dice)
```

Possible Output

```text
[2 5 1 6 3 4 2 5 1 6]
```

---

# 🌍 Real-World Use Case

An online shopping company wants to predict customer purchases.

Using probability they can:

- Predict customer buying behavior.
- Estimate product demand.
- Detect fraudulent transactions.
- Improve recommendation systems.

Machine Learning algorithms use probability to make predictions based on historical data.

---

# ⚠️ Common Mistakes

### ❌ Confusing Probability with Possibility

Probability is a numerical measure.

Example:

```text
Probability of getting Head

= 1/2

= 0.5
```

Possibility only tells whether something can happen.

---

# 💼 Interview Questions

## Q1. What is Probability?

**Answer**

Probability is the numerical measure of the likelihood that an event will occur.

---

## Q2. What is Sample Space?

**Answer**

The sample space is the complete set of all possible outcomes of a random experiment.

---

## Q3. Difference between Binomial and Poisson Distribution?

| Binomial Distribution | Poisson Distribution |
|-----------------------|----------------------|
| Fixed number of trials | Fixed time or interval |
| Success or Failure | Counts number of events |
| Example: Coin Toss | Example: Calls per Hour |

---

## Q4. Why is Normal Distribution important?

**Answer**

Many real-world datasets such as heights, weights, IQ scores, and exam marks approximately follow a normal distribution, making it essential for statistical analysis and machine learning.

---

# ✅ Summary

Today you learned:

- Experiment
- Sample Space
- Event
- Probability Formula
- Random Variable
- Uniform Distribution
- Normal Distribution
- Binomial Distribution
- Poisson Distribution
- Random Number Generation

These concepts form the mathematical foundation for statistics, machine learning, and predictive analytics.
