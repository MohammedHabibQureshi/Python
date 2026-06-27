import pandas as pd

# Read Dataset
df = pd.read_csv("students.csv")

print("Original Dataset")
print(df)

# Check Missing Values
print("\nMissing Values")
print(df.isnull())

# Count Missing Values
print("\nMissing Values Count")
print(df.isnull().sum())

# Fill Missing Marks with Mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill Missing Age with Mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nAfter Filling Missing Values")
print(df)

# Check Duplicate Rows
print("\nDuplicate Rows")
print(df.duplicated())

# Remove Duplicates
df = df.drop_duplicates()

# Remove Extra Spaces
df["Name"] = df["Name"].str.strip()

# Rename Column
df.rename(columns={"Marks": "Score"}, inplace=True)

# Convert Age to Integer
df["Age"] = df["Age"].astype(int)

print("\nCleaned Dataset")
print(df)
