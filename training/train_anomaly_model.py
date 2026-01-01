import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest

# Load data
df = pd.read_csv("data/sales.csv")

# Cleaning
df["price"] = df["price"].fillna(df["price"].mean())
df["quantity"] = df["quantity"].fillna(df["quantity"].median())
df["discount_pct"] = df["discount_pct"].fillna(0)

# Features for anomaly detection
features = [
    "price",
    "quantity",
    "discount_pct",
    "profit",
    "is_weekend",
]

X = df[features]

# Train Isolation Forest
model = IsolationForest(
    n_estimators=200,
    contamination=0.02,
    random_state=42
)

model.fit(X)

# Save model
joblib.dump(model, "models/anomaly_model.pkl")

print("✅ Anomaly model trained and saved to models/anomaly_model.pkl")
