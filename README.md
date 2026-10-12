# WEBPROJECT
WEBPROJECT DESCRIPTION
🌱 Smart Agriculture AI — Intelligent Farming Platform

Python · Flask · Scikit-learn · Pandas · NumPy · SQLite · Bootstrap 5 · Chart.js

Smart Agriculture AI is a responsive, machine-learning-powered web application designed to assist farmers and agriculture students with crop recommendation, irrigation planning, soil nutrient analysis, and farm data analytics.

The platform combines a trained Random Forest classifier with rule-based agricultural advisory modules, an interactive analytics dashboard, CSV dataset management, and SQLite-based prediction history. It runs locally on Windows without requiring paid APIs, cloud services, or physical IoT sensors.

Built as an advanced BCA Final-Year Machine Learning Project to demonstrate the practical application of AI and data analytics in agriculture.

📁 Project Structure
smart-agriculture-ai/
├── app.py                       # Flask application and API endpoints
├── train_model.py               # Model training and evaluation
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── .gitignore                   # Files excluded from Git
├── .env.example                 # Example environment configuration
├── LICENSE                      # Project license
│
├── data/
│   └── crop_recommendation.csv   # Crop training dataset
│
├── models/
│   ├── crop_model.joblib         # Trained Random Forest pipeline
│   └── metrics.json              # Model evaluation results
│
├── instance/
│   └── agriculture.db            # SQLite database (auto-created)
│
├── templates/
│   ├── base.html                 # Shared layout and navigation
│   ├── index.html                # Main dashboard
│   ├── crop.html                 # Crop recommendation interface
│   ├── irrigation.html            # Irrigation planner
│   ├── fertilizer.html            # Fertilizer advisory
│   └── analytics.html            # Analytics and prediction history
│
├── static/
│   ├── css/
│   │   └── style.css              # Responsive application styling
│   └── js/
│       └── app.js                 # Client-side enhancements
│
└── tests/
    ├── test_app.py                # Application tests
    └── test_models.py             # Model pipeline tests


Note: Model files, the SQLite database, and test files are generated or added during project setup. Their exact presence depends on your repository contents.

✨ Key Features
Feature	Description
🌾 Crop Recommendation	Predicts a candidate crop from soil nutrients and climate conditions using Random Forest classification.
💧 Smart Irrigation	Estimates illustrative irrigation requirements from soil moisture, temperature, humidity, rainfall, crop stage, and farm area.
🧪 Fertilizer Advisory	Flags potentially low nitrogen, phosphorus, and potassium values and provides general soil pH guidance.
📊 Farm Analytics	Displays dataset statistics, crop class distribution, model metrics, and recent prediction history.
📂 CSV Dataset Upload	Imports compatible crop datasets and retrains the model.
🧠 Model Evaluation	Reports held-out classification accuracy and additional classification metrics.
🗄️ Prediction History	Stores crop, irrigation, and fertilizer results in a local SQLite database.
🔌 JSON API	Provides crop prediction, application health, and prediction history endpoints.
📱 Responsive UI	Supports desktop, tablet, and mobile layouts.
🖥️ Local Execution	Runs locally without paid APIs, cloud accounts, or physical sensors.
⚙️ Installation
1. Prerequisites
Windows 10 or Windows 11
Python 3.11 or 3.12
pip package manager
Visual Studio Code (recommended)
Internet access for installing packages and loading CDN-hosted frontend assets

Verify Python installation:

py --version

2. Clone the Repository

Replace YOUR_USERNAME with your GitHub username.

git clone https://github.com/YOUR_USERNAME/smart-agriculture-ai.git
cd smart-agriculture-ai


Alternatively, download the repository ZIP from GitHub and extract it.

3. Create a Virtual Environment
py -3.12 -m venv .venv


Activate the environment in Command Prompt:

.venv\Scripts\activate

4. Install Dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

5. Prepare the Dataset

Ensure that the following file exists:

data/crop_recommendation.csv


The CSV must contain these columns:

N,P,K,temperature,humidity,ph,rainfall,label


The numeric columns represent soil nutrient measurements and climate inputs. The label column contains the target crop class.

Use the sample dataset included in the repository or replace it with a compatible, documented agricultural dataset.

6. Train the Machine Learning Model

Run the training script:

python train_model.py


The script validates the dataset, trains a Random Forest classifier, evaluates predictions on a held-out test set, and saves the trained pipeline and evaluation metrics.

Generated files:

models/
├── crop_model.joblib
└── metrics.json

7. Launch the Application
python app.py


Open the following address in your browser:

http://127.0.0.1:5000

Keep the terminal running while using the application.

🧠 Machine Learning — Crop Recommendation

The crop recommendation module uses a supervised machine learning classification pipeline built with Scikit-learn.

Input Features
Feature	Description
N	Nitrogen level
P	Phosphorus level
K	Potassium level
Temperature	Ambient temperature in °C
Humidity	Relative humidity in %
pH	Soil pH value
Rainfall	Rainfall measurement in mm
Model Architecture
Algorithm: Random Forest Classifier
Library: Scikit-learn
Preprocessing: Numeric validation and median imputation
Training strategy: Train/test split with a fixed random seed
Evaluation: Accuracy and classification report
Model persistence: Joblib
Training Workflow
Agricultural CSV Dataset
          ↓
Data Validation
          ↓
Feature Selection
          ↓
Missing-Value Handling
          ↓
Train/Test Split
          ↓
Random Forest Training
          ↓
Model Evaluation
          ↓
Save Model and Metrics
          ↓
Crop Recommendation


The predicted crop is a model-generated candidate, not a guarantee of successful cultivation.

💧 Smart Irrigation Planner

The irrigation module estimates a demonstration irrigation requirement using:

Soil moisture
Temperature
Relative humidity
Recent rainfall
Crop growth stage
Farm area in acres

The output includes an illustrative water depth in millimetres, an estimated water volume in litres, and general guidance.

Implementation: Rule-based calculation, not a separately trained machine learning model.

Actual irrigation requirements depend on soil properties, crop water demand, effective rainfall, evapotranspiration, irrigation efficiency, and local conditions. The demonstration formula must be validated before practical agricultural use.

🧪 Fertilizer and Soil Nutrient Advisory

The fertilizer module accepts:

Nitrogen (N)
Phosphorus (P)
Potassium (K)
Soil pH
Crop name

It identifies potentially low nutrient values using illustrative thresholds and provides general pH observations.

The system does not calculate a validated fertilizer dose. Fertilizer type, application rate, and timing should be determined using laboratory soil tests, crop-specific nutrient requirements, and local agricultural guidance.

📊 Analytics Dashboard

The analytics module provides an overview of the dataset and application activity.

Dashboard section	Information
Dataset overview	Number of records, columns, and crop classes
Crop distribution	Chart showing records per crop class
Model evaluation	Held-out test accuracy and training statistics
Dataset management	CSV upload and model retraining
Prediction history	Recent crop, irrigation, and fertilizer results
Application statistics	Total predictions and module usage

Chart.js is used for interactive data visualization, while SQLite stores prediction history locally.

🔌 API Endpoints
Method	Endpoint	Purpose
GET	/api/health	Checks application and model-file status
POST	/api/crop-predict	Returns a crop recommendation from JSON input
GET	/api/history	Returns recent prediction records
Example Crop Prediction Request

Endpoint:

POST /api/crop-predict
Content-Type: application/json


Request body:

{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 20.9,
  "humidity": 82,
  "ph": 6.5,
  "rainfall": 202.9
}


Example response structure:

{
  "crop": "rice",
  "confidence": 85.0,
  "note": "Verify the recommendation against local agronomic guidance."
}


The response above illustrates the format only. The predicted crop and confidence depend on the trained model and actual input values.

🗄️ Database

Smart Agriculture AI uses SQLite, so no separate database server is required.

The application automatically creates its database and prediction-history table.

instance/
└── agriculture.db


Prediction records contain:

Record ID
Timestamp
Module name
Input values
Prediction or advisory result

The database is intended for local demonstration and can be inspected using an SQLite database viewer.

🧪 Testing and Evaluation

Recommended checks before submission:

Verify that the application starts successfully.
Test crop predictions with valid and invalid inputs.
Confirm that malformed CSV uploads are rejected.
Verify that prediction history is saved correctly.
Test irrigation boundary values and fertilizer advisory inputs.
Confirm that model metrics match the latest training run.
Test the interface on desktop and mobile screen sizes.
Run automated tests before pushing changes to GitHub.

For a stronger academic evaluation, add stratified cross-validation, a confusion matrix, per-class precision and recall, and comparisons against Decision Tree and Gradient Boosting classifiers where the dataset supports them.

🛠️ Technology Stack
Component	Technology
Frontend	HTML5, CSS3, Bootstrap 5, JavaScript
Backend	Python, Flask
Machine Learning	Scikit-learn, Random Forest
Data Processing	Pandas, NumPy
Visualization	Chart.js
Database	SQLite
Model Persistence	Joblib
Dataset Format	CSV
Development Environment	Windows, VS Code
Version Control	Git and GitHub
🚀 Future Enhancements
Crop Yield Prediction: Estimate crop yield using documented historical yield, weather, and soil data.
Plant Disease Detection: Add an image-classification model trained on a suitable labeled leaf dataset.
Weather Integration: Incorporate weather forecasts into irrigation planning.
Explainable AI: Display feature importance and model explanations.
Model Comparison: Compare Random Forest, Decision Tree, and Gradient Boosting.
User Authentication: Add secure login and user-specific farm records.
IoT Integration: Connect validated soil moisture sensors and other agricultural devices.
Advanced Analytics: Add cross-validation, confusion matrices, and model monitoring.
Deployment: Prepare a production configuration with secure secrets and a production WSGI server.
⚠️ Disclaimer

Smart Agriculture AI is an educational project developed to demonstrate machine learning and data analytics in agriculture.

The included sample dataset is small and illustrative. Its evaluation metrics do not establish real-world agricultural accuracy. Irrigation estimates and fertilizer advisories use demonstration rules and have not been independently validated for farm management.

The application should not replace laboratory soil testing, verified weather data, crop-specific recommendations, or advice from qualified agricultural professionals.

Before using this platform for real farming decisions, validate the models and calculations using reliable local data and agronomic expertise.

👨‍🎓 Academic Project Information

Project Title: Smart Agriculture AI — All-in-One Intelligent Farming Platform

Project Type: BCA Final-Year Project

Domain: Artificial Intelligence, Machine Learning, Data Analytics, and Smart Agriculture

Primary Objective: To demonstrate how machine learning and web technologies can support crop selection, irrigation planning, soil nutrient assessment, and agricultural data exploration through a unified application.

📄 License

This project can be distributed under the MIT License if that matches your intended use. Add a LICENSE file before claiming that the repository is MIT-licensed.

⭐ Contributing

Contributions and educational improvements are welcome. Before submitting changes, test the application locally and document any modifications to model features, training data, or evaluation procedures.

If you find this project useful for learning, consider starring the repository on GitHub.
