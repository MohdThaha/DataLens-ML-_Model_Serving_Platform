import pandas as pd
from fastapi import APIRouter

from app.schemas import TransactionInput, AnomalyInput
from app.model_loader import load_decision_model, load_anomaly_model

router = APIRouter()

decision_model = load_decision_model()
anomaly_model = load_anomaly_model()

CONFIDENCE_THRESHOLD = 0.7

@router.post("/evaluate-transaction")
def evaluate_transaction(
    transaction: TransactionInput,
    anomaly_data: AnomalyInput
):
    # --------------------
    # Decision Prediction
    # --------------------
    decision_df = pd.DataFrame([transaction.dict()])
    prediction = decision_model.predict(decision_df)[0]
    confidence = decision_model.predict_proba(decision_df)[0][int(prediction)]

    # --------------------
    # Anomaly Detection
    # --------------------
    anomaly_df = pd.DataFrame([anomaly_data.dict()])
    anomaly_flag = anomaly_model.predict(anomaly_df)[0]
    anomaly_score = anomaly_model.decision_function(anomaly_df)[0]

    is_anomaly = anomaly_flag == -1

    # --------------------
    # Risk Logic
    # --------------------
    if is_anomaly and confidence < CONFIDENCE_THRESHOLD:
        risk_level = "HIGH"
    elif is_anomaly or confidence < CONFIDENCE_THRESHOLD:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "high_profit": int(prediction),
        "confidence": round(float(confidence), 4),
        "is_anomaly": bool(is_anomaly),
        "anomaly_score": round(float(anomaly_score), 4),
        "risk_level": risk_level
    }
