
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained Random Forest model
model = joblib.load("random_forest_final_model.pkl")

# List of features in the same order as during training
FEATURES = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Scaled_Amount'
]

app = FastAPI()

class Transaction(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Scaled_Amount: float

@app.post("/predict")
def predict(transaction: Transaction):
    input_data = np.array([[getattr(transaction, feature) for feature in FEATURES]])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return {
        "prediction": int(prediction),
        "fraud_probability": round(float(probability), 4)
    }
