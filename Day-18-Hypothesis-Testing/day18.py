from scipy.stats import ttest_ind, chi2_contingency
import numpy as np

# Sample Data
group1 = [70, 75, 80, 85, 90]
group2 = [65, 68, 72, 74, 78]

# Independent T-Test
t_stat, p_value = ttest_ind(group1, group2)

print("=== Independent T-Test ===")
print("T-Statistic:", round(t_stat, 4))
print("P-Value:", round(p_value, 4))

if p_value < 0.05:
    print("Result: Reject Null Hypothesis")
else:
    print("Result: Fail to Reject Null Hypothesis")

# Chi-Square Test
observed = np.array([
    [30, 20],
    [15, 35]
])

chi2, p, dof, expected = chi2_contingency(observed)

print("\n=== Chi-Square Test ===")
print("Chi-Square Statistic:", round(chi2, 4))
print("P-Value:", round(p, 4))
print("Degrees of Freedom:", dof)
print("Expected Frequencies:")
print(expected)

if p < 0.05:
    print("Result: Variables are associated.")
else:
    print("Result: Variables are independent.")
