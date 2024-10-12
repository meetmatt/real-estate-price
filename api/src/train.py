import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
data = pd.read_csv('data/data.csv')

# Separate features and target
X = data[['surfaces.max', 'bedrooms.max']]
y = data['prices.max']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Gradient Boosting Regressor model
model = GradientBoostingRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'model/model.pkl')

# Evaluate the model
mae = np.mean(np.abs(model.predict(X_test) - y_test))
mse = np.mean((model.predict(X_test) - y_test)**2)
r2 = model.score(X_test, y_test)

print(f"Model evaluation metrics: MAE={mae}, MSE={mse}, R^2={r2}")
