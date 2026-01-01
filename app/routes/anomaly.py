import pandas as pd
from fastapi import APIRouter

from app.schemas import AnomalyInput
from app.model_loader import load_anomaly_model

router = APIRouter()

model = load_anomaly_model()

@router.post("/detect-anomaly")
def detect_anomaly(data: AnomalyInput):
    input_df = pd.DataFrame([data.dict()])

    flag = model.predict(input_df)[0]      # -1 or 1
    score = model.decision_function(input_df)[0]

    return {
        "is_anomaly": bool(flag == -1),
        "anomaly_score": round(float(score), 4)
    }
