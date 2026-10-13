🌱 Smart Agriculture AI — Intelligent Farming Platform

Python · Flask · Scikit-learn · Pandas · NumPy · SQLite · Bootstrap 5 · Chart.js

Smart Agriculture AI is a responsive, machine-learning-powered web application designed to assist farmers and agriculture students with crop recommendation, irrigation planning, soil nutrient analysis, and farm data analytics.

The platform combines a trained Random Forest classifier with rule-based agricultural advisory modules, an interactive analytics dashboard, CSV dataset management, and SQLite-based prediction history. It runs locally on Windows without requiring paid APIs, cloud services, or physical IoT sensors.

Developed as an advanced Machine Learning Project, it demonstrates the practical application of artificial intelligence, machine learning, and data analytics in agriculture.


📑 Table of Contents
Project Overview
Key Features
Project Structure
Technology Stack
System Requirements
Installation and Setup
Dataset Preparation
Launch the Application
Machine Learning Architecture
Crop Recommendation System
Smart Irrigation Planner
Fertilizer and Soil Nutrient Advisory
Analytics Dashboard
API Documentation
Database Design
Testing and Evaluation
Security and Data Validation
Future Enhancements
Limitations and Disclaimer
Academic Project Information
Contributing
License


📌 1. Project Overview

Smart Agriculture AI integrates machine learning and agricultural decision-support features into a single web application.

Objectives
Recommend suitable crops using soil nutrient and climate data.
Estimate illustrative irrigation requirements using rule-based calculations.
Identify potentially low nitrogen, phosphorus, and potassium levels.
Provide general soil pH observations.
Visualize agricultural dataset statistics and crop distributions.
Store prediction history in a local SQLite database.
Allow compatible CSV datasets to be uploaded for model retraining.
Demonstrate an end-to-end machine learning workflow through a web interface.
Target Users
BCA and computer science students
Agriculture students and researchers
Machine learning beginners
Developers interested in agricultural technology
Users exploring data-driven agricultural decision support

✨ 2. Key Features

Feature	Description
🌾 Crop Recommendation	Predicts a candidate crop using a Random Forest classifier.
💧 Smart Irrigation	Estimates illustrative water requirements using environmental conditions and crop growth stage.
🧪 Fertilizer Advisory	Flags potentially low N, P, and K values and provides general pH guidance.
📊 Farm Analytics	Displays dataset statistics, crop distribution, model metrics, and prediction history.
📂 CSV Dataset Upload	Imports compatible crop datasets and supports model retraining.
🧠 Model Evaluation	Reports held-out classification accuracy and additional evaluation metrics.
🗄️ Prediction History	Stores crop, irrigation, and fertilizer results in SQLite.
🔌 JSON API	Provides health-check, crop prediction, and history endpoints.
📱 Responsive Interface	Supports desktop, tablet, and mobile layouts.
🖥️ Local Execution	Runs locally without paid APIs, cloud accounts, or physical sensors.


📁 3. Project Structure
smart-agriculture-ai/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
├── LICENSE
│
├── data/
│   └── crop_recommendation.csv
│
├── models/
│   ├── crop_model.joblib
│   └── metrics.json
│
├── instance/
│   └── agriculture.db
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── crop.html
│   ├── irrigation.html
│   ├── fertilizer.html
│   └── analytics.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
└── tests/
    ├── test_app.py
    └── test_models.py

File Descriptions

File or Directory	Purpose
app.py	Flask application, page routes, API endpoints, and database integration.
train_model.py	Dataset validation, model training, evaluation, and artifact generation.
requirements.txt	Python dependencies.
README.md	Project documentation and setup instructions.
data/	Crop recommendation training dataset.
models/	Trained model and evaluation metrics.
instance/	Local SQLite database and application data.
templates/	HTML templates for application pages.
static/css/	Application styling and responsive layouts.
static/js/	Client-side interactions and chart integration.
tests/	Automated application and model tests.
.env.example	Example environment configuration.
.gitignore	Files excluded from version control.
LICENSE	Project licensing terms.

Note: Generated files such as the trained model, metrics, and SQLite database may not exist until the project has been initialized. Create the test files if they are not already included in the repository.

🛠️ 4. Technology Stack

Component	Technology
Frontend	HTML5, CSS3, JavaScript
UI Framework	Bootstrap 5
Backend	Python, Flask
Machine Learning	Scikit-learn, Random Forest
Data Processing	Pandas, NumPy
Visualization	Chart.js
Database	SQLite
Model Persistence	Joblib
Dataset Format	CSV
Development Environment	Windows, Visual Studio Code
Version Control	Git and GitHub
💻 5. System Requirements
Recommended Environment
Operating system: Windows 10 or Windows 11
Python: 3.11 or 3.12
Package manager: pip
Code editor: Visual Studio Code
Version control: Git
Internet access: Required for initial package installation and CDN-hosted frontend assets

Verify Python installation:

py --version


Verify pip:

py -m pip --version

⚙️ 6. Installation and Setup
Step 1: Clone the Repository

Replace YOUR_USERNAME with your GitHub username.

git clone https://github.com/YOUR_USERNAME/smart-agriculture-ai.git
cd smart-agriculture-ai


Alternatively, download the repository as a ZIP file from GitHub and extract it.

Step 2: Create a Virtual Environment
py -3.12 -m venv .venv

Step 3: Activate the Environment

For Windows Command Prompt:

.venv\Scripts\activate


For PowerShell:

.\.venv\Scripts\Activate.ps1


If PowerShell blocks script execution, use Command Prompt or follow your organization's approved Python environment setup instructions.

Step 4: Upgrade pip
python -m pip install --upgrade pip

Step 5: Install Dependencies
pip install -r requirements.txt


If requirements.txt has not yet been created, prepare it with compatible versions of the required packages. For example:

Flask
scikit-learn
pandas
numpy
joblib
pytest


Pin and test dependency versions before final submission. Add other packages only if the implementation requires them.

📊 7. Dataset Preparation

The crop recommendation model uses a CSV dataset containing soil nutrient measurements and environmental conditions.

Ensure this file exists:

data/crop_recommendation.csv

Required Columns
N,P,K,temperature,humidity,ph,rainfall,label

Feature	Description	Expected Input
N	Nitrogen content	Numeric
P	Phosphorus content	Numeric
K	Potassium content	Numeric
temperature	Temperature in degrees Celsius	Numeric
humidity	Relative humidity percentage	Numeric
ph	Soil pH value	Numeric
rainfall	Rainfall measurement in millimetres	Numeric
label	Target crop category	Text
Dataset Validation Requirements

Before training, the application should:

Verify that all required columns exist.
Reject empty or malformed datasets.
Validate numeric feature values.
Handle missing values consistently.
Reject invalid or non-finite numeric inputs.
Verify that enough labeled records exist for the selected train/test split.
Check for duplicate records and potential data leakage.
Preserve the original dataset when a new upload fails validation.

Use a documented agricultural dataset with a known source and appropriate usage rights. Dataset quality, geographical relevance, crop coverage, and class balance directly affect model performance.

🚀 8. Launch the Application
Step 1: Train the Machine Learning Model

Run the training script:

python train_model.py


The training script should validate the dataset, train the Random Forest classifier, evaluate performance on a held-out test set, and save the model artifacts.

Expected generated files:

models/
├── crop_model.joblib
└── metrics.json

Step 2: Configure Flask to Use Port 8000

Open app.py and make sure the final section is configured as follows:

if __name__ == "__main__":
    app.run(debug=True, port=8000)


If an app.run() statement already exists, update it instead of adding a duplicate.

Step 3: Start the Application

Run:

python app.py

Step 4: Open the Application in Your Browser

Visit:

http://127.0.0.1:8000

Keep the terminal running while using the application.

Step 5: Run Automated Tests

Open another terminal in the project directory, activate the virtual environment, and run:

python -m pytest -v


This command works when the test directory and test files have been created and the required test dependencies are installed.

Troubleshooting: If port 8000 is already in use, stop the other application using that port before starting Smart Agriculture AI. The Flask development server is intended for local development, not production deployment.

🧠 9. Machine Learning Architecture

The crop recommendation system uses a supervised classification pipeline based on Scikit-learn's Random Forest algorithm.

Model Configuration
Component	Description
Learning Type	Supervised learning
Problem Type	Multiclass classification
Algorithm	Random Forest Classifier
Input Features	Seven numeric features
Target	Crop label
Preprocessing	Numeric validation and median imputation, where appropriate
Evaluation	Held-out test set and classification metrics
Persistence	Joblib
Output	Predicted crop class
Training Workflow
Agricultural CSV Dataset
          |
          v
     Data Validation
          |
          v
    Feature Selection
          |
          v
   Missing-Value Handling
          |
          v
      Train/Test Split
          |
          v
   Random Forest Training
          |
          v
     Model Evaluation
          |
          v
 Save Model and Metrics
          |
          v
    Crop Recommendation

Training Script Responsibilities

The train_model.py script should:

Load the dataset from the configured path.
Validate required columns and feature values.
Separate input features from target labels.
Build the preprocessing and classification pipeline.
Split the dataset into training and test sets.
Train the Random Forest classifier.
Evaluate predictions on held-out data.
Save the fitted pipeline to models/crop_model.joblib.
Save evaluation metrics to models/metrics.json.

Use stratified splitting when the dataset has sufficient examples in each class. Perform imputation and other learned preprocessing inside the training pipeline to avoid data leakage.

🌾 10. Crop Recommendation System

The crop recommendation interface accepts seven features and predicts a candidate crop based on the trained model.

Input Parameters
Nitrogen (N)
Phosphorus (P)
Potassium (K)
Temperature
Relative humidity
Soil pH
Rainfall
Prediction Process
The user enters soil and climate measurements.
The Flask backend validates the submitted values.
The trained model pipeline processes the input.
The classifier predicts a crop category.
The result is displayed in the interface.
The prediction and relevant input data may be stored in SQLite.
Example Input
{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 20.9,
  "humidity": 82,
  "ph": 6.5,
  "rainfall": 202.9
}


The values are illustrative and do not represent a validated recommendation for a particular farm.

Confidence Score

If the interface displays a confidence percentage, it should be derived from a documented model output, such as predict_proba() when supported by the fitted classifier.

A predicted probability is not necessarily a calibrated estimate of the probability that a crop will succeed. Avoid presenting confidence as a guarantee of agricultural suitability.

Important: The predicted crop is a model-generated candidate, not a guarantee of successful cultivation. Verify the result using local agronomic guidance and reliable soil and weather information.

💧 11. Smart Irrigation Planner

The irrigation module estimates an illustrative irrigation requirement using a rule-based calculation rather than a separately trained machine learning model.

Input Parameters
Soil moisture
Temperature
Relative humidity
Recent rainfall
Crop growth stage
Farm area in acres
Output

The interface can display:

Estimated irrigation depth in millimetres
Estimated water volume in litres
General irrigation guidance
A summary of the submitted conditions
Water Volume Conversion

For an estimated irrigation depth 
𝑑
 in millimetres and an area 
𝐴
 in acres:

𝑉
=
𝑑
×
𝐴
×
4046.8564224

Where:

𝑉
 is the gross water volume in litres.
𝑑
 is the irrigation depth in millimetres.
𝐴
 is the irrigated area in acres.

This conversion follows from one millimetre of water over one square metre equaling one litre.

The equation calculates a volume from a supplied depth; it does not validate whether that depth is appropriate for a crop.

Practical Considerations

Actual irrigation needs depend on:

Crop-specific water demand
Soil type and water-holding capacity
Root depth and growth stage
Effective rainfall
Evapotranspiration
Irrigation-system efficiency
Local weather and field conditions

The demonstration formula must be documented and validated before practical agricultural use. Do not interpret illustrative estimates as operational irrigation instructions.

🧪 12. Fertilizer and Soil Nutrient Advisory

The fertilizer advisory module accepts:

Nitrogen (N)
Phosphorus (P)
Potassium (K)
Soil pH
Crop name
Functionality

The module can:

Flag potentially low nutrient values.
Provide general observations about soil pH.
Display crop-specific contextual notes when supported by reliable guidance.
Explain that soil test interpretation depends on the measurement method and local recommendations.
Advisory Logic

The implementation may compare nutrient values against configurable thresholds. These thresholds must be documented as illustrative unless supported by a validated local soil-testing standard.

The module does not calculate a validated fertilizer dose.

Fertilizer selection, application rate, and timing should be based on laboratory soil tests, crop-specific nutrient requirements, local agronomic recommendations, and appropriate professional guidance.

📈 13. Analytics Dashboard

The analytics dashboard summarizes dataset characteristics, model performance, and application activity.

Dashboard Section	Information
Dataset Overview	Number of records, available columns, and crop classes
Crop Distribution	Number of records for each crop class
Model Evaluation	Held-out accuracy and other evaluation metrics
Dataset Management	CSV upload, validation, and model retraining
Prediction History	Recent crop, irrigation, and fertilizer results
Application Statistics	Total predictions and module usage
Visualization

Chart.js provides interactive charts, while Bootstrap 5 and custom CSS provide responsive layouts.

Possible visualizations include:

Crop class distribution bar chart
Model evaluation summary
Prediction activity chart
Historical prediction table
Dataset statistics cards
CSV Upload and Retraining

A compatible uploaded dataset can be used to retrain the model after validation.

The implementation should avoid replacing a working model with an invalid or failed training result.

Recommended process:

Validate the uploaded CSV.
Train the candidate model separately.
Evaluate its metrics.
Save candidate artifacts to temporary files.
Promote the new model only after successful completion.
Record the dataset and model version used for each training run.

Restrict dataset uploads to trusted users in any shared or deployed environment.

🔌 14. API Documentation

The application can expose JSON endpoints for programmatic access to core functionality.

Available Endpoints
Method	Endpoint	Purpose
GET	/api/health	Checks application and model-file status.
POST	/api/crop-predict	Returns a crop prediction from JSON input.
GET	/api/history	Returns recent prediction records.

These endpoint names describe the intended interface and should match the actual routes implemented in app.py.

14.1 Health Check

Request:

GET /api/health


The endpoint should report whether the application is running and whether the required model artifacts are available.

A successful health check does not by itself prove that the model is accurate or that the dataset is agronomically valid.

14.2 Crop Prediction

Request:

POST /api/crop-predict
Content-Type: application/json


Example request body:

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
  "crop": "example_crop",
  "confidence": 85.0,
  "note": "Verify the recommendation against local agronomic guidance."
}


The crop name and confidence shown here are placeholders illustrating the response format. Actual outputs depend on the trained model, its classes, the input values, and the implemented confidence calculation.

14.3 Prediction History

Request:

GET /api/history


The endpoint can return recent stored predictions with their timestamps, module names, inputs, and results.

Do not expose private farm records to unauthorized users. If the application is made accessible to multiple users, enforce authentication and appropriate record-level access controls.

Recommended API Validation

The backend should:

Reject malformed JSON.
Check that all required features are present.
Validate numeric types and allowed ranges.
Reject NaN, positive infinity, and negative infinity.
Return clear error messages with appropriate HTTP status codes.
Handle missing model files gracefully.
Avoid returning internal stack traces or sensitive configuration details.

🗄️ 15. Database Design

Smart Agriculture AI uses SQLite, so a separate database server is not required.

The database file is stored at:

instance/agriculture.db


The application can create the database and required tables during initialization.

Prediction History Fields
Field	Description
id	Unique record identifier
timestamp	Date and time of the prediction
module	Crop, irrigation, or fertilizer module
input_data	Submitted input values, preferably stored as JSON
result	Prediction or advisory output

The exact column names and schema should match the database implementation.

Database Responsibilities
Store prediction history.
Support recent activity views.
Provide aggregate statistics for the dashboard.
Preserve records across application restarts.
Enable local inspection with an SQLite database viewer.
Data Management

Use parameterized SQL statements, validate stored data, and avoid logging unnecessary personal information.

If prediction history is sensitive, document retention and deletion practices. Back up important records before replacing or deleting the database.

🧪 16. Testing and Evaluation

Testing is necessary before presenting the application as a completed academic project.

Application Testing Checklist
Verify that Flask starts successfully on port 8000.
Confirm that all application pages load.
Test crop predictions with valid inputs.
Confirm that invalid numeric values are rejected.
Test missing and malformed JSON requests.
Verify that missing model artifacts produce clear errors.
Confirm that malformed CSV uploads are rejected.
Check that failed retraining does not replace a working model.
Verify that prediction history is saved correctly.
Test irrigation boundary values.
Test fertilizer advisory inputs.
Confirm that metrics correspond to the latest training run.
Test the interface on desktop and mobile layouts.
Run the automated test suite before pushing changes to GitHub.
Model Evaluation Metrics

For a stronger academic evaluation, include:

Accuracy
Precision
Recall
F1-score
Confusion matrix
Per-class classification report
Stratified cross-validation, where appropriate
Comparison against baseline classifiers

Potential comparison models include:

Decision Tree Classifier
Random Forest Classifier
Gradient Boosting Classifier

Use the same data splits and evaluation methodology for fair comparisons. Report dataset size, class distribution, preprocessing, hyperparameters, and limitations alongside the results.

Do not invent model accuracy or claim experimental results until the training and evaluation scripts have actually produced them.

🔐 17. Security and Data Validation

Although the application is intended for local educational use, good engineering practices should be followed.

Keep secret keys and credentials out of source control.
Use environment variables for deployment-specific secrets.
Do not commit virtual environments or unnecessary generated files.
Validate uploaded files before processing them.
Apply reasonable CSV upload size limits.
Prevent path traversal when handling filenames.
Use parameterized SQL queries.
Validate all API inputs on the server.
Avoid exposing stack traces in production.
Restrict model retraining to authorized users in shared deployments.
Treat serialized model files as trusted artifacts because loading untrusted Joblib or pickle-based files can execute arbitrary code.
Use a production WSGI server and appropriate deployment configuration outside local development.

The Flask development server is suitable for local development, not production hosting.

🚀 18. Future Enhancements
1. Crop Yield Prediction

Estimate crop yield using documented historical yield, weather, soil, and management data.

2. Plant Disease Detection

Add an image-classification model trained on an appropriately labeled plant disease dataset.

3. Weather Integration

Incorporate reliable weather forecasts and historical weather observations into irrigation planning.

4. Explainable AI

Display feature importance and other model explanations to help users understand predictions.

5. Model Comparison

Compare Random Forest, Decision Tree, Gradient Boosting, and other suitable algorithms.

6. User Authentication

Introduce secure login, user-specific farm records, and role-based access control.

7. IoT Integration

Integrate validated soil moisture sensors and other agricultural devices when suitable hardware becomes available.

8. Advanced Analytics

Add cross-validation, confusion matrices, model monitoring, and dataset quality reports.

9. Production Deployment

Prepare secure configuration, a production WSGI server, logging, backups, and deployment documentation.

10. Regional Agricultural Support

Incorporate reliable regional crop calendars, soil-testing interpretations, and locally appropriate agricultural guidance.

⚠️ 19. Limitations and Disclaimer

Smart Agriculture AI is an educational project developed to demonstrate machine learning and data analytics in agriculture.

The following limitations apply:

The included sample dataset may be small or illustrative.
Model evaluation metrics do not establish real-world agricultural accuracy.
The model may not generalize to different geographical regions, soil types, or growing conditions.
Crop predictions are based on the data used for training and may omit important agronomic variables.
Predicted probabilities, if displayed, may not be calibrated.
Irrigation estimates use demonstration rules and have not been independently validated for farm management.
Fertilizer advisories do not establish scientifically validated fertilizer application rates.
CSV uploads and retraining can change model performance and require appropriate evaluation.

The application should not replace laboratory soil testing, verified weather information, crop-specific recommendations, or advice from qualified agricultural professionals.

Before using this platform for real farming decisions, validate the model and calculations with reliable local data and appropriate agronomic expertise.

🎓 20. Academic Project Information

Project Title: Smart Agriculture AI — All-in-One Intelligent Farming Platform

Project Type: BCA Final-Year Project

Domain: Artificial Intelligence, Machine Learning, Data Analytics, and Smart Agriculture

Primary Objective: To demonstrate how machine learning and web technologies can support crop selection, irrigation planning, soil nutrient assessment, and agricultural data exploration through a unified application.

Expected Learning Outcomes
Understanding supervised machine learning classification.
Preparing and validating structured agricultural datasets.
Training and evaluating a Random Forest model.
Building a Flask-based web application.
Integrating machine learning with a web backend.
Designing REST-style JSON endpoints.
Persisting data using SQLite.
Creating interactive data visualizations.
Writing automated tests and documenting limitations.
Suggested Project Demonstration
Launch the application at http://127.0.0.1:8000.
Open the main dashboard.
Submit sample inputs to the crop recommendation module.
Explore the irrigation planner.
Review the fertilizer advisory.
Open the analytics dashboard.
Demonstrate prediction history.
Explain the model training workflow and evaluation metrics.
Discuss limitations, data quality, and future enhancements.
🤝 21. Contributing

Contributions and educational improvements are welcome.

To contribute:

Fork the repository.
Create a feature branch.
Implement the proposed change.
Run the available automated tests.
Document changes to model features, training data, evaluation procedures, or application behavior.
Submit a pull request describing the changes.

Example:

git checkout -b feature/improved-analytics
git add .
git commit -m "Improve agricultural analytics dashboard"
git push origin feature/improved-analytics


Only include files intended for version control. Keep virtual environments, secrets, local databases, temporary uploads, and other generated files out of Git unless there is a documented reason to track them.

If you find this project useful for learning, consider starring the repository on GitHub.

📄 22. License

This project can be distributed under the MIT License if that matches the author's intended licensing terms.

Before claiming that the project is MIT-licensed:

Add a LICENSE file containing the complete MIT License text.
Replace the copyright holder and year placeholders with the appropriate information.
Check the licensing terms of the training dataset and any third-party assets.

Until the license is added, the repository's licensing status should be described accurately.

🌱 Conclusion

Smart Agriculture AI demonstrates how Python, Flask, machine learning, data processing, and interactive visualizations can be combined to build an educational agricultural decision-support platform.

By integrating crop recommendation, rule-based irrigation estimation, soil nutrient advisories, dataset management, and prediction history, the project provides a foundation for exploring AI applications in agriculture.

The platform is designed for local development, academic demonstration, and further experimentation. Its practical agricultural use requires reliable datasets, validated calculations, appropriate evaluation, and qualified agronomic guidance.

Smart Agriculture AI — Combining Machine Learning and Data Analytics for Smarter Agriculture.
