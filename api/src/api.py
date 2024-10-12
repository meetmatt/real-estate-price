from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# Load the model using joblib
model = joblib.load('model/model.pkl')

# Initialize FastAPI
api = FastAPI()

# Define the input schema
class PropertyData(BaseModel):
    area: float
    bedrooms: int

# Define the prediction endpoint
@api.post("/api/predict")
def predict_price(data: PropertyData):
    # Prepare the features for prediction
    features = np.array([[data.area, data.bedrooms]])

    # Make the prediction
    prediction = model.predict(features)

    # Return the prediction price
    return {"area": data.area, "bedrooms": data.bedrooms, "predicted_price": round(prediction[0])}