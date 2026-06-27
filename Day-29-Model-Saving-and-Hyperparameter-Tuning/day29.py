import joblib
import pickle

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Create Model
model = RandomForestClassifier(random_state=42)

# Hyperparameter Grid
param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [2, 4, 6]
}

# Grid Search
grid = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5
)

# Train
grid.fit(X, y)

# Best Results
print("Best Parameters:", grid.best_params_)
print("Best Cross Validation Score:", grid.best_score_)

# Save using Joblib
joblib.dump(grid.best_estimator_, "random_forest_model.joblib")

# Save using Pickle
with open("random_forest_model.pkl", "wb") as file:
    pickle.dump(grid.best_estimator_, file)

print("\nModel saved successfully!")

# Load Model
loaded_model = joblib.load("random_forest_model.joblib")

prediction = loaded_model.predict([X[0]])

print("Prediction for first sample:", prediction)
