import pandas as pd

# Read Dataset
df = pd.read_csv("students.csv")

# Select Column
print("Name Column")
print(df["Name"])

# Multiple Columns
print("\nMultiple Columns")
print(df[["Name", "Marks"]])

# loc
print("\nUsing loc[]")
print(df.loc[1])

# iloc
print("\nUsing iloc[]")
print(df.iloc[2])

# Filter
print("\nMarks Greater Than 85")
print(df[df["Marks"] > 85])

# Sort
print("\nSort by Marks")
print(df.sort_values(by="Marks"))

# Rename Column
df.rename(columns={"Marks": "Score"}, inplace=True)

print("\nRenamed Column")
print(df)

# Add New Column
df["Result"] = ["Pass", "Pass", "Pass"]

print("\nNew Column")
print(df)

# Delete Column
df.drop(columns=["Age"], inplace=True)

print("\nAfter Dropping Age")
print(df)

# Unique Values
print("\nUnique Names")
print(df["Name"].unique())
