SMART AGRICULTURE AI — BCA MACHINE LEARNING PROJECT

Project contents:
- app.py: Flask application and routes
- train_model.py: Random Forest model training
- requirements.txt: Python dependencies
- data/crop_recommendation.csv: illustrative sample data
- templates/: HTML pages
- static/css/style.css: responsive styling
- static/js/app.js: browser enhancements
- models/: model files generated after training
- instance/: SQLite database generated when the app starts

WINDOWS SETUP (PowerShell)
1. Extract this ZIP.
2. Open PowerShell in the Smart_Agriculture_AI folder (the folder containing app.py).
3. Create a virtual environment:
   py -m venv .venv
4. Activate it:
   .\\.venv\\Scripts\\Activate.ps1
   If script activation is blocked, use the direct executable in the next steps instead.
5. Install dependencies:
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
6. Train the model:
   python train_model.py
7. Start the website:
   python app.py
8. Open http://127.0.0.1:5000 in your browser.

If PowerShell activation is blocked:
   .\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt
   .\\.venv\\Scripts\\python.exe train_model.py
   .\\.venv\\Scripts\\python.exe app.py

IMPORTANT
The included CSV is a small illustrative dataset for demonstrating the software pipeline.
It is not sufficient for dependable real-world farming decisions. Irrigation and fertilizer
outputs are also demonstration heuristics. Confirm decisions with local agricultural
experts and soil tests. Do not use the app to automatically control irrigation equipment.
