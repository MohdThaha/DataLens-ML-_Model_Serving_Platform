import pandas as pd
from fastapi import APIRouter

from app.schemas import TransactionInput
from app.model_loader import load_decision_model

router = APIRouter()

model = load_decision_model()

@router.post("/predict")
def predict_transaction(data: TransactionInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Predict class
    prediction = model.predict(input_df)[0]

    # Predict probability
    probability = model.predict_proba(input_df)[0][int(prediction)]

    return {
        "high_profit": int(prediction),
        "confidence": round(float(probability), 4)
    }
