from fastapi import FastAPI
from app.model_loader import load_decision_model

app = FastAPI(
    title="DataLens ML Model Serving",
    description="Production-style ML inference API",
    version="1.0.0"
)

# Load model at startup
decision_model = load_decision_model()

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "DataLens ML API is running"
    }
