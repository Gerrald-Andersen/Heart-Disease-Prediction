# ❤️ `lib/` — Model and Pipeline Utilities

This folder contains the trained machine learning model and any preprocessing pipelines used in the **Heart Disease Prediction** web application.  
These components are loaded by the Streamlit app to perform real-time predictions.

---

## 📦 Contents

| File / Folder           | Purpose                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| `best_classifier.pkl`    | Serialized Random Forest Classifier (best-performing model) used for predicting heart disease |

---

## 🧠 Usage Notes

- The `.pkl` file can be loaded using `pickle.load()` in Python.  
- It contains the trained Random Forest Classifier ready for prediction.  
- This file is imported and used by the Streamlit web application; it is **not meant to be executed directly**.

---

## ⚖️ License

This project is proprietary. All rights reserved © 2025 Gerrald Andersen.  
No part of this repository may be copied, modified, reused, or redistributed without explicit written permission.

![License: Proprietary](https://img.shields.io/badge/license-Proprietary-red.svg)
