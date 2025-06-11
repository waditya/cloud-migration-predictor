from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open("xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

def preprocess(data):
    os_map = {"linux": 1, "windows": 0}
    storage_map = {"ssd": 1, "hdd": 0}
    return [
        data["cpu_utilization"],
        data["memory_usage"],
        data["uptime_days"],
        data["network_in"],
        data["network_out"],
        storage_map[data["storage_type"]],
        os_map[data["os"]],
    ]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(preprocess(data)).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({"migration_feasible": bool(prediction)})

if __name__ == "__main__":
    app.run(debug=True)