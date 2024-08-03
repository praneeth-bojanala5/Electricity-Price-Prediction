from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load the pre-trained optimized model and preprocessor
model_path = 'model/optimized_model.pkl'
if not os.path.exists(model_path):
    raise Exception("Optimized model file not found. Train and optimize your model first.")
    
pipeline = joblib.load(model_path)

@app.route('/')
def home():
    return "Welcome to the Electricity Price Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)['inputs']
        df = pd.DataFrame(data)
        predictions = pipeline.predict(df)
        return jsonify(predictions=predictions.tolist())
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
