# Create Dictionary
employee = {
    "name": "John",
    "age": 30,
    "department": "Sales"
}

print("Original Dictionary")
print(employee)

# Access Value
print("\nAccess Value")
print(employee["name"])

# Safe Access
print("\nSafe Access")
print(employee.get("salary", 0))

# Add Key
employee["salary"] = 75000

print("\nAfter Adding Salary")
print(employee)

# Update Key
employee["age"] = 31

print("\nAfter Updating Age")
print(employee)

# Delete Key
del employee["department"]

print("\nAfter Deleting Department")
print(employee)

# Keys
print("\nKeys")
print(employee.keys())

# Values
print("\nValues")
print(employee.values())

# Items
print("\nItems")
print(employee.items())

# Dictionary Comprehension
prices = {
    "Apple": 100,
    "Orange": 80,
    "Banana": 50
}

discount = {k: v * 0.9 for k, v in prices.items()}

print("\nDictionary Comprehension")
print(discount)

# Nested Dictionary
students = {
    "student1": {
        "name": "John",
        "score": 92
    },
    "student2": {
        "name": "Alice",
        "score": 95
    }
}

print("\nNested Dictionary")
print(students)
