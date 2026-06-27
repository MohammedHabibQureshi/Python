# if Statement
age = 20

if age >= 18:
    print("Eligible to vote")

# if...else Statement
marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# if...elif...else Statement
marks = 82

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# Nested if
age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")

# for Loop
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

# range()
for i in range(1, 6):
    print(i)

# while Loop
count = 1

while count <= 5:
    print(count)
    count += 1

# break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# pass
for i in range(5):
    if i == 3:
        pass
    print(i)
