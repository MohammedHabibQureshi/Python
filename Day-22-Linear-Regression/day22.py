import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample Dataset
data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [30000, 35000, 45000, 55000, 65000]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Experience"]]
y = df["Salary"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Predict Salary for 6 Years Experience
prediction = model.predict([[6]])

print("Predicted Salary for 6 Years Experience: ₹", prediction[0])

# Evaluation
print("Mean Squared Error:", mean_squared_error(y, y_pred))
print("R² Score:", r2_score(y, y_pred))

# Visualization
plt.figure(figsize=(8,5))
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, y_pred, color="red", label="Regression Line")

plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)

plt.savefig("regression_plot.png")
plt.show()
