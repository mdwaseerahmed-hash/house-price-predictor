# 🏠 House Price Predictor

A machine learning web app that predicts median house prices in California neighborhoods using XGBoost, built with Flask and deployed on Render.

🔗 **Live Demo:** [house-price-predictor-odi9.onrender.com](https://house-price-predictor-odi9.onrender.com)

---

## Overview

This project walks through the full machine learning pipeline — from raw data exploration to a deployed, production-ready web application. Users can enter block-level details about a California neighborhood and instantly receive a predicted median house value.

---

## Features

- Trained and compared 3 ML models: Linear Regression, Random Forest, and XGBoost
- XGBoost achieved the best performance with **R² of 0.848** and **MAE of ~$30,000**
- Full data preprocessing pipeline with outlier removal and feature scaling
- Flask backend with a clean, modern dark-themed UI
- Deployed live using Gunicorn on Render

---

## Tech Stack

| Layer | Tools |
|---|---|
| Data & EDA | Python, Pandas, NumPy, Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Backend | Flask, Gunicorn, Joblib |
| Frontend | HTML, CSS |
| Deployment | Render |

---

## Model Comparison

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | 0.5016 | 0.6808 | 0.6646 |
| Random Forest | 0.3188 | 0.4953 | 0.8225 |
| **XGBoost** | **0.2988** | **0.4583** | **0.8480** |

---

## Dataset

**California Housing Dataset** from scikit-learn — 20,640 samples, 8 features.

| Feature | Description |
|---|---|
| MedInc | Median income of households (×$10,000) |
| HouseAge | Median age of houses in the block |
| AveRooms | Average number of rooms per household |
| AveBedrms | Average number of bedrooms per household |
| Population | Block population |
| AveOccup | Average number of people per household |
| Latitude | Geographic latitude |
| Longitude | Geographic longitude |

---

## Project Structure

```
house-price-predictor/
├── data/
├── notebooks/
│   ├── eda.ipynb
│   ├── preprocessing.ipynb
│   ├── training.ipynb
│   └── evaluation.ipynb
├── model/
│   ├── house_price_model.pkl
│   └── scaler.pkl
├── templates/
│   └── index.html
├── app.py
├── Procfile
└── requirements.txt
```

---

## How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/mdwaseerahmed-hash/house-price-predictor.git
cd house-price-predictor
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**
```bash
python app.py
```

**5. Open in browser**
```
http://127.0.0.1:5000
```

---

## Key Findings

- **Median Income** is the strongest predictor of house price by far
- **Average Occupancy** and **Longitude** are the next most important features
- XGBoost outperformed Random Forest with a Train R² of 0.93 and Test R² of 0.85 — a small gap indicating the model generalizes well

---

## Author

**Md Waseer Ahmed**
- GitHub: [@mdwaseerahmed-hash](https://github.com/mdwaseerahmed-hash)
