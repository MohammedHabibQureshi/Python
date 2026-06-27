import numpy as np

# Sample Space
sample_space = {1, 2, 3, 4, 5, 6}
print("Sample Space:", sample_space)

# Event
event = {2, 4, 6}
print("Event (Even Numbers):", event)

# Probability
probability = len(event) / len(sample_space)
print("Probability of Even Number:", probability)

# Random Variable
X = np.random.randint(1, 7)
print("Random Variable (Dice Roll):", X)

# Generate Random Numbers
dice_rolls = np.random.randint(1, 7, 10)
print("10 Dice Rolls:", dice_rolls)

# Uniform Distribution
uniform_numbers = np.random.uniform(0, 1, 5)
print("Uniform Distribution:", uniform_numbers)

# Normal Distribution
normal_numbers = np.random.normal(loc=50, scale=10, size=5)
print("Normal Distribution:", normal_numbers)

# Binomial Distribution
binomial = np.random.binomial(n=10, p=0.5, size=5)
print("Binomial Distribution:", binomial)

# Poisson Distribution
poisson = np.random.poisson(lam=3, size=5)
print("Poisson Distribution:", poisson)
