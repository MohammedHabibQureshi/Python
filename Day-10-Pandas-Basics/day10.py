import pandas as pd

# Create Series
marks = pd.Series([80, 85, 90, 95])
print("Series")
print(marks)

# Create DataFrame
student = {
    "Name": ["Habib", "Ali", "Sara"],
    "Age": [22, 23, 21],
    "Marks": [90, 85, 95]
}

df = pd.DataFrame(student)

print("\nDataFrame")
print(df)

# Save DataFrame to CSV
df.to_csv("students.csv", index=False)

# Read CSV
df = pd.read_csv("students.csv")

print("\nFirst Five Rows")
print(df.head())

print("\nLast Five Rows")
print(df.tail())

print("\nInformation")
df.info()

print("\nStatistical Summary")
print(df.describe())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)
