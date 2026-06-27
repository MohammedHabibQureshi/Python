import numpy as np
import pandas as pd
from statistics import mode

# Sample Data
marks = [80, 85, 90, 95, 100]

# Mean
print("Mean:", np.mean(marks))

# Median
print("Median:", np.median(marks))

# Mode
numbers = [1, 2, 2, 3, 4]
print("Mode:", mode(numbers))

# Range
print("Range:", max(marks) - min(marks))

# Variance
print("Variance:", np.var(marks))

# Standard Deviation
print("Standard Deviation:", np.std(marks))

# Minimum
print("Minimum:", np.min(marks))

# Maximum
print("Maximum:", np.max(marks))

# Percentile
print("75th Percentile:", np.percentile(marks, 75))

# Correlation
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 65, 80, 95]
}

df = pd.DataFrame(data)

print("\nCorrelation Matrix:")
print(df.corr())
