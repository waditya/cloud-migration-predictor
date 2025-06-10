import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
import pickle

# Load data
df = pd.read_csv("../data/synthetic_server_data.csv")
df["storage_type"] = df["storage_type"].map({"ssd": 1, "hdd": 0})
df["os"] = df["os"].map({"linux": 1, "windows": 0})

X = df.drop("migration_feasible", axis=1)
y = df["migration_feasible"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = xgb.XGBClassifier()
model.fit(X_train, y_train)

# Save model
with open("xgboost_model.pkl", "wb") as f:
    pickle.dump(model, f)