import matplotlib.pyplot as plt

# Line Plot
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [120, 150, 180, 170]

plt.figure(figsize=(6,4))
plt.plot(months, sales, label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()

# Bar Chart
students = ["Ali", "Sara", "Habib"]
marks = [80, 90, 95]

plt.figure(figsize=(6,4))
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Histogram
ages = [18,19,20,20,21,22,22,23,24]

plt.figure(figsize=(6,4))
plt.hist(ages)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
hours = [1,2,3,4,5]
marks = [40,55,65,80,95]

plt.figure(figsize=(6,4))
plt.scatter(hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# Pie Chart
subjects = ["Math","Science","English"]
students = [40,35,25]

plt.figure(figsize=(6,6))
plt.pie(students, labels=subjects, autopct="%1.1f%%")
plt.title("Students by Subject")
plt.show()
