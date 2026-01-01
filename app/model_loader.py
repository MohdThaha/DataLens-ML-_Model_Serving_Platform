import joblib

DECISION_MODEL_PATH = "models/decision_model.pkl"
ANOMALY_MODEL_PATH = "models/anomaly_model.pkl"

def load_decision_model():
    return joblib.load(DECISION_MODEL_PATH)

def load_anomaly_model():
    return joblib.load(ANOMALY_MODEL_PATH)
