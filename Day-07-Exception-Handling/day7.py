# Basic Exception
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# ValueError
try:
    number = int("Python")
except ValueError:
    print("Invalid number.")

# Multiple Exceptions
try:
    number = int(input("Enter a number: "))
    print(100 / number)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

# else Block
try:
    result = 20 / 2

except ZeroDivisionError:
    print("Error")

else:
    print("Result:", result)

# finally Block
try:
    print("Opening File")

finally:
    print("Closing File")

# raise
age = -5

try:
    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as e:
    print(e)

# User-Defined Exception
class InvalidAgeError(Exception):
    pass

try:
    age = -1

    if age < 0:
        raise InvalidAgeError("Invalid Age")

except InvalidAgeError as e:
    print(e)
