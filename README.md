
# Wine Quality Prediction Web Application

## Overview
This project is a web application that predicts the quality of wine based on user-provided chemical attributes. The application uses a machine learning model deployed with a Flask backend and provides a user-friendly HTML interface for inputs. The project integrates multiple data processing and training stages, MLflow for experiment tracking, and is organized for scalable and maintainable development.

---

## Features
- **Frontend Form**: An HTML form where users input chemical properties of the wine, such as acidity, residual sugar, pH, etc.
- **Backend Prediction**: A Flask server processes the input and uses a pre-trained machine learning model to predict wine quality.
- **Dynamic Result Rendering**: Displays the prediction result dynamically using Jinja2 templates.
- **MLflow Integration**: Logs model metrics, parameters, and artifacts for experiment tracking and evaluation.
- **Pipeline Automation**: Modularized pipeline stages for data ingestion, validation, transformation, model training, and evaluation.
- **DagsHub Repository**: Uses DagsHub for version control and MLflow tracking.

---

## Tech Stack
- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn, Joblib
- **Experiment Tracking**: MLflow with DagsHub integration

---

## Requirements
- Python 3.7+
- Flask
- Pandas
- Numpy
- Scikit-learn
- Joblib
- MLflow

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Prahaladha-Reddy/First_End_To_End.git
   ```

2. Navigate to the project directory:
   ```bash
   cd First_End_To_End
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # For Linux/Mac
   venv\Scripts\activate # For Windows
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Project Structure
```
<project-root>
│
├── app.py                     # Flask application
├── main.py                    # Orchestrates all pipeline stages
├── requirements.txt           # Python dependencies
├── templates/                 # HTML templates
│   ├── index.html             # Input form
│   └── results.html           # Prediction result display
├── static/                    # Static assets (CSS, images, etc.)
├── artifacts/                 # Stores pipeline outputs
│   ├── data_ingestion/        # Data ingestion artifacts
│   ├── data_transformation/   # Transformed data
│   ├── data_validation/       # Validation reports
│   ├── model_evaluation/      # Evaluation metrics
│   └── model_trainer/         # Trained model
├── config/                    # Configuration files
│   ├── config.yaml            # General configurations
│   ├── params.yaml            # Model parameters
│   └── schema.yaml            # Schema definitions
├── logs/                      # Log files for debugging
├── research/                  # Notebooks for experimentation
├── src/                       # Source code
│   ├── datascience/           # Main module
│       ├── components/        # Core components for each stage
│       ├── config/            # Configuration handlers
│       ├── constants/         # Constants used across the project
│       ├── entity/            # Entity classes for pipeline inputs/outputs
│       ├── pipeline/          # Pipelines for different stages
│       └── utils/             # Utility functions
└── README.md                  # Project documentation
```

---

## Pipeline Stages

### 1. **Data Ingestion**
   - Collects raw data and prepares it for processing.
   - Artifacts are stored in `artifacts/data_ingestion`.
   - Triggered in `main.py` using:
     ```python
     obj = DataIngestionTrainingPipeline()
     obj.initiate_data_ingestion()
     ```

### 2. **Data Validation**
   - Validates the schema and ensures data consistency.
   - Outputs validation reports in `artifacts/data_validation`.
   - Triggered in `main.py` using:
     ```python
     obj = DatavalidationTrainingPipeline()
     obj.initiate_data_validation()
     ```

### 3. **Data Transformation**
   - Processes and transforms data for training.
   - Artifacts are stored in `artifacts/data_transformation`.
   - Triggered in `main.py` using:
     ```python
     obj = DataTransformationTrainingPiprline()
     obj.initiate_data_transformation()
     ```

### 4. **Model Training**
   - Trains the machine learning model and stores it.
   - Outputs the model in `artifacts/model_trainer`.
   - Triggered in `main.py` using:
     ```python
     obj = ModelTrainerTrainingPipeline()
     obj.initiate_model_training()
     ```

### 5. **Model Evaluation**
   - Evaluates the trained model on test data.
   - Outputs metrics in `artifacts/model_evaluation`.
   - Triggered in `main.py` using:
     ```python
     obj = ModelEvaluationTrainingPipeline()
     obj.initiate_model_evaluation()
     ```

---

## Usage

### Run the Application
1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open a web browser and navigate to:
   ```
   http://127.0.0.1:8080/
   ```

3. Fill in the form with the required chemical properties and click **Predict**.

4. View the prediction result on the next page.

### Run Pipelines
To manually execute pipeline stages, run:
```bash
python main.py
```

---

## MLflow Integration
This project integrates MLflow for tracking experiments. The MLflow tracking URI is set to a DagsHub repository.

### Steps to Log Metrics and Models:
1. **Set Tracking URI**:
   Ensure that the MLflow tracking URI is set to the DagsHub repository in your configuration.
   ```python
   mlflow.set_tracking_uri("https://dagshub.com/<Username>/<Project name>")
   ```

2. **Run MLflow Tracking**:
   Metrics such as RMSE, MAE, and R² are logged along with the trained model. Example:
   ```python
   mlflow.log_metric("rmse", rmse)
   mlflow.log_metric("mae", mae)
   mlflow.log_metric("r2", r2)
   mlflow.sklearn.log_model(model, "model")
   ```

3. **View Logs on DagsHub**:
   Navigate to your DagsHub repository and explore the MLflow UI for detailed experiment tracking.

---

