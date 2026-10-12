from pathlib import Path
import json
import sqlite3
from datetime import datetime, timezone

import joblib
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename

from train_model import train_model, FEATURES

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
INSTANCE_DIR = BASE_DIR / "instance"
DB_PATH = INSTANCE_DIR / "agriculture.db"
DATA_PATH = DATA_DIR / "crop_recommendation.csv"
MODEL_PATH = MODEL_DIR / "crop_model.joblib"
METRICS_PATH = MODEL_DIR / "metrics.json"

app = Flask(__name__)
app.config["SECRET_KEY"] = "replace-this-with-a-random-secret"
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
app.config["UPLOAD_FOLDER"] = DATA_DIR

CROP_INFO = {
    "rice": "Suitable where water availability and growing conditions support rice.",
    "maize": "Consider soil fertility, rainfall, and seasonal temperature.",
    "cotton": "Check local growing-season length and soil drainage.",
    "chickpea": "Often grown in cooler, relatively dry conditions.",
    "banana": "Requires suitable warmth, water, drainage, and nutrients.",
    "mungbean": "A short-duration legume; verify the local growing season.",
}
RANGES = {
    "N": (0, 200), "P": (0, 200), "K": (0, 250),
    "temperature": (-5, 60), "humidity": (0, 100),
    "ph": (0, 14), "rainfall": (0, 1000),
}


def connect_db():
    INSTANCE_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with connect_db() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL, module TEXT NOT NULL,
            inputs TEXT NOT NULL, result TEXT NOT NULL)""")
        conn.commit()


def log_prediction(module, inputs, result):
    with connect_db() as conn:
        conn.execute(
            "INSERT INTO predictions (created_at, module, inputs, result) VALUES (?, ?, ?, ?)",
            (datetime.now(timezone.utc).isoformat(timespec="seconds"),
             module, json.dumps(inputs), json.dumps(result)),
        )
        conn.commit()


def load_model():
    if not MODEL_PATH.exists():
        train_model()
    return joblib.load(MODEL_PATH)["model"]


def get_metrics():
    if METRICS_PATH.exists():
        return json.loads(METRICS_PATH.read_text(encoding="utf-8"))
    return {}


def numeric_form_values(fields):
    values = {}
    for field in fields:
        raw = request.form.get(field, "").strip()
        if not raw:
            raise ValueError(f"Please enter {field}.")
        try:
            value = float(raw)
        except ValueError:
            raise ValueError(f"{field} must be a number.")
        if not np.isfinite(value):
            raise ValueError(f"{field} must be finite.")
        low, high = RANGES[field]
        if not low <= value <= high:
            raise ValueError(f"{field} must be between {low} and {high}.")
        values[field] = value
    return values


def recommend_irrigation(moisture, temperature, humidity, rainfall, crop_stage, area_acres):
    if not 0 <= moisture <= 100:
        raise ValueError("Moisture must be between 0 and 100.")
    if not 0 <= humidity <= 100:
        raise ValueError("Humidity must be between 0 and 100.")
    if not 0 <= rainfall <= 1000:
        raise ValueError("Rainfall must be between 0 and 1000 mm.")
    if not 0 < area_acres <= 100000:
        raise ValueError("Area must be greater than 0.")
    if not -5 <= temperature <= 60:
        raise ValueError("Temperature must be between -5 and 60 C.")

    stage_factor = {"seedling": 0.85, "vegetative": 1.0,
                    "flowering": 1.15, "maturity": 0.75}.get(crop_stage, 1.0)
    deficit = max(0, 60 - moisture) * 0.35
    weather_factor = max(0.25, 1 + max(0, temperature - 25) * 0.025
                         - max(0, humidity - 60) * 0.008)
    effective_rain = min(rainfall, 25) * 0.4
    depth_mm = max(0, deficit * stage_factor * weather_factor - effective_rain)
    litres = depth_mm * area_acres * 4046.8564224

    if depth_mm < 2:
        status, advice = "Low immediate need", "Check the sensor again and avoid unnecessary watering."
    elif depth_mm < 10:
        status, advice = "Moderate irrigation need", "Consider a measured irrigation cycle and recheck moisture."
    else:
        status, advice = "Higher irrigation need", "Inspect root-zone moisture and local forecasts before watering."
    return {"status": status, "depth_mm": round(depth_mm, 2),
            "water_litres": round(litres, 0), "advice": advice,
            "method": "Illustrative rule-based estimate"}


def fertilizer_advisory(n, p, k, ph, crop):
    deficiencies = []
    if n < 40: deficiencies.append("Nitrogen may be low")
    if p < 25: deficiencies.append("Phosphorus may be low")
    if k < 25: deficiencies.append("Potassium may be low")
    if ph < 5.5:
        ph_advice = "Soil is acidic; confirm with a soil test before amendments."
    elif ph > 7.5:
        ph_advice = "Soil is alkaline; confirm pH and nutrient availability with a soil test."
    else:
        ph_advice = "pH is within a broad general range; crop-specific targets may differ."
    if not deficiencies:
        deficiencies.append("No low N/P/K flags from the demo thresholds")
    return {"crop": crop, "nutrient_flags": deficiencies, "ph_advice": ph_advice,
            "recommendation": "Use a laboratory soil test and local crop guidance to determine fertilizer type, dose, and timing.",
            "method": "Illustrative nutrient thresholds"}


def recent_predictions(limit=8):
    with connect_db() as conn:
        rows = conn.execute(
            "SELECT id, created_at, module, inputs, result FROM predictions ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [dict(row) for row in rows]


@app.route("/")
def index():
    with connect_db() as conn:
        total = conn.execute("SELECT COUNT(*) FROM predictions").fetchone()[0]
        crops = conn.execute("SELECT COUNT(*) FROM predictions WHERE module='crop'").fetchone()[0]
        irrigation = conn.execute("SELECT COUNT(*) FROM predictions WHERE module='irrigation'").fetchone()[0]
    return render_template("index.html", total=total, crops=crops, irrigation=irrigation,
                           metrics=get_metrics(), recent=recent_predictions())


@app.route("/crop", methods=["GET", "POST"])
def crop():
    result, values = None, {}
    if request.method == "POST":
        try:
            values = numeric_form_values(FEATURES)
            model = load_model()
            row = pd.DataFrame([values], columns=FEATURES)
            prediction = str(model.predict(row)[0])
            confidence = None
            if hasattr(model, "predict_proba"):
                confidence = round(float(max(model.predict_proba(row)[0])) * 100, 1)
            result = {"crop": prediction, "confidence": confidence,
                      "note": CROP_INFO.get(prediction.lower(), "Verify this suggestion against local agronomic guidance."),
                      "disclaimer": "Model confidence is not the probability that this crop will succeed on your farm."}
            log_prediction("crop", values, result)
        except (ValueError, FileNotFoundError) as exc:
            flash(str(exc), "error")
        except Exception:
            app.logger.exception("Crop prediction failed")
            flash("Prediction failed. Check the dataset and model files.", "error")
    return render_template("crop.html", result=result, values=values)


@app.route("/irrigation", methods=["GET", "POST"])
def irrigation():
    result, values = None, {}
    if request.method == "POST":
        try:
            fields = ["moisture", "temperature", "humidity", "rainfall", "area_acres"]
            for field in fields:
                raw = request.form.get(field, "").strip()
                if not raw: raise ValueError(f"Please enter {field}.")
                values[field] = float(raw)
            if not all(np.isfinite(v) for v in values.values()):
                raise ValueError("All values must be finite numbers.")
            stage = request.form.get("crop_stage", "vegetative")
            if stage not in {"seedling", "vegetative", "flowering", "maturity"}:
                raise ValueError("Invalid crop stage.")
            result = recommend_irrigation(values["moisture"], values["temperature"],
                values["humidity"], values["rainfall"], stage, values["area_acres"])
            result["crop_stage"] = stage
            log_prediction("irrigation", values | {"crop_stage": stage}, result)
        except (ValueError, TypeError) as exc:
            flash(str(exc), "error")
    return render_template("irrigation.html", result=result, values=values)


@app.route("/fertilizer", methods=["GET", "POST"])
def fertilizer():
    result, values = None, {}
    if request.method == "POST":
        try:
            values = numeric_form_values(["N", "P", "K", "ph"])
            crop_name = request.form.get("crop", "").strip()
            if not crop_name or len(crop_name) > 60:
                raise ValueError("Enter a valid crop name.")
            result = fertilizer_advisory(values["N"], values["P"], values["K"], values["ph"], crop_name)
            log_prediction("fertilizer", values | {"crop": crop_name}, result)
        except ValueError as exc:
            flash(str(exc), "error")
    return render_template("fertilizer.html", result=result, values=values)


@app.route("/analytics")
def analytics():
    metrics, dataset_summary = get_metrics(), {}
    if DATA_PATH.exists():
        df = pd.read_csv(DATA_PATH)
        dataset_summary = {"rows": int(len(df)), "columns": int(len(df.columns)),
            "crops": int(df["label"].nunique()) if "label" in df.columns else 0,
            "distribution": df["label"].value_counts().to_dict() if "label" in df.columns else {}}
    return render_template("analytics.html", metrics=metrics, dataset=dataset_summary,
                           history=recent_predictions(100))


@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "model_exists": MODEL_PATH.exists(),
                    "dataset_exists": DATA_PATH.exists()})


@app.route("/api/crop-predict", methods=["POST"])
def crop_predict_api():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Send a JSON object."}), 400
    values = {}
    try:
        for field in FEATURES:
            value = float(payload[field])
            if not np.isfinite(value): raise ValueError(f"{field} must be finite.")
            low, high = RANGES[field]
            if not low <= value <= high: raise ValueError(f"{field} must be between {low} and {high}.")
            values[field] = value
        model = load_model()
        row = pd.DataFrame([values], columns=FEATURES)
        predicted = str(model.predict(row)[0])
        probabilities = model.predict_proba(row)[0] if hasattr(model, "predict_proba") else None
        result = {"crop": predicted,
            "confidence": round(float(np.max(probabilities)) * 100, 1) if probabilities is not None else None,
            "note": CROP_INFO.get(predicted.lower(), "Verify locally before making a planting decision.")}
        log_prediction("crop", values, result)
        return jsonify(result)
    except (KeyError, TypeError, ValueError) as exc:
        return jsonify({"error": str(exc)}), 400
    except Exception:
        app.logger.exception("Crop API error")
        return jsonify({"error": "Model prediction failed."}), 500


@app.route("/upload", methods=["POST"])
def upload_dataset():
    file = request.files.get("dataset")
    if not file or not file.filename:
        flash("Choose a CSV file first.", "error")
        return redirect(url_for("analytics"))
    filename = secure_filename(file.filename)
    if not filename.lower().endswith(".csv"):
        flash("Only CSV files are accepted.", "error")
        return redirect(url_for("analytics"))
    try:
        df = pd.read_csv(file, nrows=100000)
        required = FEATURES + ["label"]
        missing = set(required) - set(df.columns)
        if missing: raise ValueError(f"CSV is missing columns: {', '.join(sorted(missing))}")
        if len(df) < 10: raise ValueError("Upload at least 10 rows.")
        for column in FEATURES: df[column] = pd.to_numeric(df[column], errors="raise")
        df = df[required].dropna()
        if df["label"].nunique() < 2: raise ValueError("Dataset needs at least two crop classes.")
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        df.to_csv(DATA_PATH, index=False)
        train_model()
        flash(f"Dataset imported and model retrained ({len(df)} rows).", "success")
    except Exception as exc:
        app.logger.exception("Dataset upload failed")
        flash(f"Could not import dataset: {exc}", "error")
    return redirect(url_for("analytics"))


@app.route("/api/history")
def history_api():
    rows = recent_predictions(100)
    for row in rows:
        row["inputs"], row["result"] = json.loads(row["inputs"]), json.loads(row["result"])
    return jsonify(rows)


init_db()
if not DATA_PATH.exists():
    raise RuntimeError(f"Place crop_recommendation.csv at {DATA_PATH}")
if not MODEL_PATH.exists():
    train_model()

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
