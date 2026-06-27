import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Sample Dataset
data = pd.DataFrame({
    "Age": [20, 30, 40, 50],
    "Salary": [30000, 50000, 70000, 90000]
})

print("=== Original Data ===")
print(data)

# -----------------------------
# Min-Max Normalization
# -----------------------------
minmax_scaler = MinMaxScaler()

normalized_data = minmax_scaler.fit_transform(data)

normalized_df = pd.DataFrame(
    normalized_data,
    columns=data.columns
)

print("\n=== Normalized Data ===")
print(normalized_df)

# -----------------------------
# Standardization
# -----------------------------
standard_scaler = StandardScaler()

standardized_data = standard_scaler.fit_transform(data)

standardized_df = pd.DataFrame(
    standardized_data,
    columns=data.columns
)

print("\n=== Standardized Data ===")
print(standardized_df)
