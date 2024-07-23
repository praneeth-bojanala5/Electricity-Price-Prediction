from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the pre-trained model and preprocessor
model = joblib.load('model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data)
    X = preprocessor.transform(df)
    predictions = model.predict(X)
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
