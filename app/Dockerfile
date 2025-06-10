FROM python:3.10-slim

WORKDIR /app
COPY ../model/xgboost_model.pkl ./
COPY inference.py ./
COPY ../requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "inference.py"]