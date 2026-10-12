from pathlib import Path
import json

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "crop_recommendation.csv"
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "crop_model.joblib"
METRICS_PATH = MODEL_DIR / "metrics.json"

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
TARGET = "label"


def train_model():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    data = pd.read_csv(DATA_PATH)
    required = FEATURES + [TARGET]
    missing = set(required) - set(data.columns)
    if missing:
        raise ValueError(f"Missing CSV columns: {sorted(missing)}")

    data = data[required].dropna(subset=[TARGET])
    data[TARGET] = data[TARGET].astype(str).str.strip()
    data = data[data[TARGET] != ""]
    for column in FEATURES:
        data[column] = pd.to_numeric(data[column], errors="coerce")
    data = data.dropna(subset=FEATURES)

    if data[TARGET].nunique() < 2:
        raise ValueError("At least two crop classes are required.")

    X, y = data[FEATURES], data[TARGET]
    counts = y.value_counts()
    can_stratify = counts.min() >= 2 and len(data) * 0.2 >= y.nunique()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42,
        stratify=y if can_stratify else None
    )

    model = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("classifier", RandomForestClassifier(
            n_estimators=250, max_depth=None, min_samples_leaf=1,
            class_weight="balanced", random_state=42, n_jobs=-1
        )),
    ])
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(
        y_test, predictions, output_dict=True, zero_division=0
    )

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump({
        "model": model, "features": FEATURES,
        "classes": sorted(y.unique().tolist())
    }, MODEL_PATH)

    metrics = {
        "accuracy": round(float(accuracy), 4),
        "train_rows": int(len(X_train)),
        "test_rows": int(len(X_test)),
        "total_rows": int(len(data)),
        "crop_classes": int(y.nunique()),
        "class_distribution": {str(k): int(v) for k, v in counts.items()},
        "classification_report": report,
    }
    METRICS_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(f"Model saved to: {MODEL_PATH}")
    print(f"Test accuracy: {accuracy:.2%}")
    print(f"Training records: {len(X_train)}")
    print(f"Testing records: {len(X_test)}")
    print(f"Crop classes: {y.nunique()}")
    return metrics


if __name__ == "__main__":
    train_model()
