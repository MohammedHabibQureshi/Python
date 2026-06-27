# Function
def greet():
    print("Welcome to Python!")

greet()

# Function with Parameters
def greet_user(name):
    print("Hello", name)

greet_user("Habib")

# Multiple Parameters
def add(a, b):
    print(a + b)

add(10, 20)

# Return Statement
def square(num):
    return num ** 2

print(square(5))

# Default Parameter
def welcome(name="Guest"):
    print("Hello", name)

welcome()
welcome("Habib")

# Keyword Arguments
def student(name, age):
    print(name, age)

student(age=22, name="Habib")

# *args
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30, 40)

# **kwargs
def employee(**details):
    print(details)

employee(name="Habib", age=22, city="Mumbai")

# Lambda Function
square = lambda x: x ** 2
print(square(6))

# Recursive Function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
