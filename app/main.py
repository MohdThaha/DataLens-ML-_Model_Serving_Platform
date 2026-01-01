from fastapi import FastAPI
from app.routes.predict import router as predict_router
from app.routes.anomaly import router as anomaly_router
from app.routes.evaluate import router as evaluate_router

app = FastAPI(
    title="DataLens ML Model Serving",
    description="Production-style ML inference API",
    version="1.0.0"
)

app.include_router(predict_router)
app.include_router(anomaly_router)
app.include_router(evaluate_router)

@app.get("/")
def health_check():
    return {"status": "ok"}
