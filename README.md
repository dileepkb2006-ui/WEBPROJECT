Smart Agriculture AI – Intelligent Farming Platform

Python · Flask · Scikit-learn · Pandas · NumPy · SQLite · Bootstrap 5 · Chart.js 

Smart Agriculture AI is a machine-learning-powered web application designed to assist farmers and agriculture students with crop recommendation, irrigation planning, soil nutrient analysis, and agricultural data analytics. The application combines a trained Random Forest classifier with rule-based agricultural advisory modules, an interactive dashboard, CSV dataset management, and SQLite-based prediction history. It runs locally on Windows without requiring paid APIs, cloud services, or physical IoT sensors.

Project Structure

```text
Smart-Agriculture-AI/
├── app.py                  # Flask web application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── data/
│   └── crop_data.csv       # Agricultural dataset
│
├── models/
│   └── crop_model.pkl      # Trained ML model
│
├── templates/
│   ├── base.html           # Base website layout
│   ├── index.html          # Main dashboard
│   ├── recommend.html      # Crop recommendation
│   ├── irrigation.html     # Irrigation planner
│   ├── soil_analysis.html  # Soil nutrient analysis
│   ├── analytics.html      # Agricultural analytics
│   └── history.html        # Prediction history
│
├── static/
│   ├── css/
│   │   └── style.css       # Website styling
│   ├── js/
│   │   └── script.js       # Frontend interactions
│   └── images/             # Website images
│
└── database/
    └── agriculture.db     # SQLite database (if created)
```

Note: The structure above is an example. Keep the filenames consistent with the actual files in your project.

 Installation

 1. Prerequisites

- Python 3.10 or a compatible version
- pip package manager
- Windows 10 or Windows 11
- A modern web browser

 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
venv\Scripts\activate.bat
```

 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

4. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

The port may differ depending on your Flask configuration.

 Dataset Setup

The application uses agricultural data for crop recommendations and analysis.

The dataset may contain the following columns, depending on the model implementation:

| Column | Description |
|---|---|
| N | Nitrogen level |
| P | Phosphorus level |
| K | Potassium level |
| temperature | Temperature |
| humidity | Humidity |
| ph | Soil pH |
| rainfall | Rainfall |
| label | Recommended crop |

Use the column names and dataset format expected by your actual application. The dataset must contain suitable training examples for the model to produce meaningful predictions.

 Machine Learning

The project uses a Random Forest classifier for crop recommendation.

What the machine learning workflow does:

- Loads the agricultural dataset.
- Processes the input features.
- Trains a classification model.
- Predicts a suitable crop based on input values.
- Generates results for the website dashboard.
- Evaluates the model using appropriate performance metrics.

If your project includes a separate training script, run it before starting the application. If the model is already trained, use the model-loading procedure implemented in `app.py`.

Main Features

 1. Crop Recommendation

Recommends a suitable crop using available soil nutrient and environmental data.

 2. Smart Irrigation Planner

Estimates irrigation requirements using rule-based calculations and available input values.

 3. Soil Nutrient Analysis

Analyzes nitrogen, phosphorus, potassium, and soil pH values to provide general observations.

4. Agricultural Analytics Dashboard

Displays available agricultural statistics and crop distributions through interactive charts.

 5. Dataset Management

Supports compatible CSV datasets for agricultural data processing and analysis.

6. Prediction History

Uses SQLite to store and retrieve previous predictions when database functionality is enabled.

 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| Scikit-learn | Machine learning |
| Pandas | Data processing |
| NumPy | Numerical calculations |
| SQLite | Database management |
| HTML5 | Web page structure |
| CSS3 | Website styling |
| JavaScript | Frontend interactions |
| Bootstrap 5 | Responsive interface |
| Chart.js | Interactive charts |

Model Evaluation

The machine learning model should be evaluated using suitable classification metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Actual results depend on the dataset, model configuration, and training procedure. Report measured scores only after running the model evaluation.

 Sustainable Development Goals (SDGs)

| SDG | Goal | Project Contribution |
|---|---|---|
| SDG 2 | Zero Hunger | Supports crop selection |
| SDG 6 | Clean Water and Sanitation | Supports irrigation planning |
| SDG 9 | Industry, Innovation and Infrastructure | Demonstrates agricultural technology |
| SDG 12 | Responsible Consumption and Production | Supports data-driven resource use |
| SDG 13 | Climate Action | Can incorporate climate-related data |

 Testing

 Test crop recommendations with different inputs.
 Check soil nutrient analysis.
 Verify irrigation calculations.
  Test valid and invalid input values.
  Check database storage and retrieval.
  Verify dashboard charts.
 Test the website on different screen sizes.
  Evaluate machine learning performance using test data.

Limitations and Disclaimer

Smart Agriculture AI is an academic project designed for educational and agricultural decision-support purposes.

Predictions depend on the quality of the training dataset. Irrigation calculations are estimates and may not represent actual field conditions. The recommendations do not replace laboratory soil testing, local agricultural guidance, or professional farming advice.

 Future Enhancements

Real-time weather integration
 IoT-based soil moisture monitoring
  Plant disease detection
  Fertilizer recommendation
 Regional language support
 Advanced crop prediction models
  Cloud deployment
  Farmer registration and personalized dashboards

Credits

Built as a BCA Machine Learning Project to demonstrate the practical application of machine learning, data analytics, and web development in agriculture.

## 📜 License

This project is intended for academic and educational use. Add an appropriate license file if you wish to distribute the project under specific reuse terms.
