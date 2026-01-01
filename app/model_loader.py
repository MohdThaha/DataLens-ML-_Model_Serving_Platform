import joblib

MODEL_PATH = "models/decision_model.pkl"

def load_decision_model():
    model = joblib.load(MODEL_PATH)
    return model
