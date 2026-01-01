import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

# --------------------
# Load data
# --------------------
df = pd.read_csv("data/sales.csv")

# --------------------
# Cleaning
# --------------------
df["price"] = df["price"].fillna(df["price"].mean())
df["quantity"] = df["quantity"].fillna(df["quantity"].median())
df["discount_pct"] = df["discount_pct"].fillna(0)

# --------------------
# Create label
# --------------------
profit_threshold = df["profit"].median()
df["high_profit"] = (df["profit"] > profit_threshold).astype(int)

# --------------------
# Features / Target
# --------------------
X = df[
    [
        "price",
        "quantity",
        "discount_pct",
        "category",
        "region",
        "sales_channel",
        "customer_type",
        "is_weekend",
    ]
]
y = df["high_profit"]

categorical_features = [
    "category",
    "region",
    "sales_channel",
    "customer_type",
]

numeric_features = [
    "price",
    "quantity",
    "discount_pct",
    "is_weekend",
]

# --------------------
# Pipeline
# --------------------
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numeric_features),
    ]
)

model = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("classifier", RandomForestClassifier(
            n_estimators=200,
            random_state=42,
            n_jobs=-1
        )),
    ]
)

# --------------------
# Train
# --------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model.fit(X_train, y_train)

# --------------------
# Save model
# --------------------
joblib.dump(model, "models/decision_model.pkl")

print("✅ Decision model trained and saved to models/decision_model.pkl")
