import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


STUDENT_ID = "l232610"

print(f"Loading dataset for student {STUDENT_ID}...")

# Load dataset
data = pd.read_csv("data/dataset.csv")

# Separate features and target
X = data.drop("price", axis=1)
y = data["price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

print(f"Mean Squared Error: {mse:.2f}")

# Save trained model
joblib.dump(model, "model/model.pkl")

print("Model trained successfully.")
print("Model saved to model/model.pkl")