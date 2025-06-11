# Dockerfile in root
FROM python:3.13-slim

WORKDIR /app

# Copy model and app code
COPY model/xgboost_model.pkl ./xgboost_model.pkl
COPY app/inference.py ./inference.py
COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "inference.py"]