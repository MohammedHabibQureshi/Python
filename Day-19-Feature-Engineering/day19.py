import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Sample Dataset
data = {
    "Name": ["Ali", "Sara", "Habib"],
    "Math": [80, 90, 85],
    "Science": [85, 95, 80],
    "Gender": ["Male", "Female", "Male"],
    "Date": ["2025-01-10", "2025-02-15", "2025-03-20"]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# Create New Feature
df["Total"] = df["Math"] + df["Science"]

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Extract Year and Month
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# Label Encoding
encoder = LabelEncoder()
df["Gender_Label"] = encoder.fit_transform(df["Gender"])

# One-Hot Encoding
df = pd.get_dummies(df, columns=["Gender"])

# Feature Selection
selected_features = df[["Math", "Science", "Total"]]

# Drop Unnecessary Column
df.drop(columns=["Name"], inplace=True)

print("\nProcessed Dataset:\n")
print(df)

print("\nSelected Features:\n")
print(selected_features)
