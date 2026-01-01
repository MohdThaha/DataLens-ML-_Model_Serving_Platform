# DataLens — ML Model Serving Platform

DataLens is a hands-on AI project series focused on building
production-ready machine learning systems from data to deployment.

This project is the **capstone** — a complete ML serving platform that
combines prediction, anomaly detection, and business risk logic behind
a real API.

---

## 🎯 Objective

Build a **standalone, production-style ML inference service** that:
- Trains models locally
- Serves them via API
- Returns decisions with confidence and risk signals

---

## 🧠 What This System Does

For a given transaction, the system:
1. Predicts whether it is **High Profit**
2. Estimates **model confidence**
3. Detects **anomalous behavior**
4. Assigns a **risk level**
5. Returns a business-ready response

---

## 📊 Models Used

### Decision Intelligence
- Model: Random Forest Classifier
- Task: Binary classification (High Profit vs Low Profit)
- Output: Prediction + Confidence

### Anomaly Detection
- Model: Isolation Forest
- Task: Unsupervised anomaly detection
- Output: Anomaly flag + score

---

## 🧪 API Endpoints

### `POST /predict`
Predicts profitability.

**Sample Response**
{
  "high_profit": 1,
  "confidence": 0.95
}

### `POST /detect-anomaly`
Detects unusual behavior.

**Sample Response**
{
  "is_anomaly": true,
  "anomaly_score": -0.02
}


### `POST /evaluate-transaction`
Unified decision + risk endpoint.

**Sample Response**
{
  "high_profit": 1,
  "confidence": 0.98,
  "is_anomaly": true,
  "anomaly_score": -0.01,
  "risk_level": "MEDIUM"
}

---
### ⚠️ Risk Logic

Condition                -	Risk Level
Anomaly + Low confidence - HIGH
Anomaly only             - MEDIUM
Low confidence only      - MEDIUM
Normal + High confidence - LOW

---
### 🛠 Tech Stack

Python
FastAPI
scikit-learn
Pandas
Joblib
Uvicorn

---

### 📌 Part of DataLens Series

✅ DataLens — Exploratory Intelligence

✅ DataLens — Predictive Modeling

✅ DataLens — Decision Intelligence

✅ DataLens — Anomaly Detection Engine

✅ DataLens — ML Model Serving Platform