# Cloud Migration Predictor

Predict which on-premise servers are optimal for migration to the cloud using machine learning. Trained using synthetic server telemetry data and deployed as a REST API using Flask.

## Features
- Uses XGBoost and Random Forest models
- AWS SageMaker-compatible training code
- Flask REST API for predictions
- Containerized with Docker
- CI pipeline via GitHub Actions

## How to Run
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Train model and run API
python model/train_model.ipynb
python app/inference.py
```

## Inference Sample
```json
{
  "cpu_utilization": 75,
  "memory_usage": 63,
  "uptime_days": 425,
  "network_in": 134,
  "network_out": 145,
  "storage_type": "ssd",
  "os": "linux"
}
```
