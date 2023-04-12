from flask import Flask,make_response, request, jsonify
import joblib
import pandas as pd
import numpy as np


app = Flask(__name__)
model = joblib.load("Changed_russia_losses_personnel3.joblib")
@app.route("/")
def home():
    return "Predictions site under construction!"

@app.route("/predict", methods=["POST"])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    prediction = model.predict(query_df)
    return jsonify({"Prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)