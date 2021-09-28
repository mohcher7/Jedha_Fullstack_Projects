from flask import Flask, render_template, jsonify, request
import joblib
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Check if request has a JSON content
    if request.json:
        # Get the JSON as dictionnary
        req = request.get_json()
        # Check mandatory key
        if "wine" in req.keys():
            # Load model
            classifier = joblib.load("model.joblib")
            # Predict
            prediction = classifier.predict(req["wine"])
            # Return the result as JSON but first we need to transform the
            # result so as to be serializable by jsonify()
            prediction = prediction.tolist()
            return jsonify({"prediction": prediction}), 200
    return jsonify({"msg": "Error: not a JSON or no 'input' key in your request"})


if __name__ == "__main__":
    app.run(debug=True)