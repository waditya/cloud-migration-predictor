# Cloud Migration Predictor

Predict which on-premise servers are optimal for migration to the cloud using machine learning. Trained using synthetic server telemetry data and deployed as a REST API using Flask.

## Features
- Uses XGBoost and Random Forest models
- AWS SageMaker-compatible training code
- Flask REST API for predictions
- Containerized with Docker
- CI pipeline via GitHub Actions
- Makefile automation for quick setup

## How to Run
```bash
# Create virtual environment and install dependencies
make setup

# Train the model
make train

# Run the Flask inference API
make run

## Building and running Docker image locally
```bash
docker build -t cloud-migration-api .
docker run -p 5000:5000 cloud-migration-api
