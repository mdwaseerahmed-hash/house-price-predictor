import pandas as pd
from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler once when the app starts
model  = joblib.load('model/house_price_model.pkl')
scaler = joblib.load('model/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html', prediction=None, error=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Grab values from the form
        features = [
            float(request.form['MedInc']),
            float(request.form['HouseAge']),
            float(request.form['AveRooms']),
            float(request.form['AveBedrms']),
            float(request.form['Population']),
            float(request.form['AveOccup']),
            float(request.form['Latitude']),
            float(request.form['Longitude']),
        ]

        # Scale and predict
        feature_names = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
                 'Population', 'AveOccup', 'Latitude', 'Longitude']
        features_df = pd.DataFrame([features], columns=feature_names)
        features_scaled = scaler.transform(features_df)
        prediction = model.predict(features_scaled)[0]

        # Convert from $100k units to full dollars
        predicted_price = round(prediction * 100000, 2)

        return render_template('index.html', prediction=predicted_price, error=None)

    except Exception as e:
        return render_template('index.html', prediction=None, error=str(e))


if __name__ == '__main__':
    app.run(debug=False)