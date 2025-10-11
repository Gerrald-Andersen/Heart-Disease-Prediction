# 📁 `UI/` — Streamlit Dashboard for Heart Disease Prediction

This folder contains the Streamlit-based web application for predicting heart disease risk.  
The dashboard allows users to input personal health data and instantly receive predictions using the trained Random Forest model.  
It provides a user-friendly interface for interacting with the model and visualizing results.

---

## 🚀 Features

- **User Input Forms** for patient health metrics (e.g., age, cholesterol, blood pressure, etc.)  
- **Random Forest Model Integration** for predicting heart disease risk  
- **Real-time Prediction** displayed immediately after form submission  
- **Result Interpretation** to indicate whether the user is at risk or not  
- **Clean and Interactive Layout** for ease of use

---

## 📦 Key Components

| Section                      | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `webapp.py`                  | Main Streamlit script that defines the web interface, inputs, and prediction logic |
| `Model Loading`              | Loads `best_classifier.pkl` using `pickle` for real-time predictions       |
| `User Input Handling`        | Collects user-provided health metrics and formats them for the model       |
| `Prediction Logic`           | Uses the trained Random Forest Classifier to generate a prediction         |
| `Result Display`             | Shows whether the user is at risk of heart disease along with probability  |

---

## 🔄 Usage Notes

- Run `webapp.py` to launch the Streamlit dashboard.  
- Ensure that `best_classifier.pkl` exists in the `lib/` folder for model predictions.  
- Users input their health data via the web form, and predictions are returned instantly.  

---

## 📁 Dependencies

- `streamlit`  
- `pandas`, `numpy`  
- `scikit-learn`  
- `pickle`

---

## ⚖️ License

This project is proprietary. All rights reserved © 2025 Gerrald Andersen.  
No part of this repository may be copied, modified, reused, or redistributed without explicit written permission.

![License: Proprietary](https://img.shields.io/badge/license-Proprietary-red.svg)
