# ❤️ `src/` — Core Modules for Heart Disease Prediction

This folder contains the main components of the **Heart Disease Prediction** pipeline — from data preprocessing to model development and evaluation.  
All modules are designed to integrate with the Streamlit web application and allow easy updates or retraining with new data.

---

## 📦 Module Structure

| File / Folder                  | Purpose                                                                 |
|--------------------------------|-------------------------------------------------------------------------|
| `notebooks/`                   | Contains all data preprocessing, cleaning, and feature engineering steps |
| `models/`                      | Contains Python scripts for machine learning model development and evaluation |

---

## 📂 Folder Details

### 🧹 `notebooks/`
This folder includes a **single Jupyter Notebook** that handles the entire data preprocessing workflow, including:
- Data loading and inspection  
- Data cleaning (handling missing values, duplicates, outliers, etc.)  
- Feature encoding and scaling  
- Feature selection and correlation analysis

All steps are executed in a single notebook for simplicity, consistency, and easier reproducibility.

---

### 🤖 `models/`
This folder contains Python scripts for developing and evaluating machine learning models for heart disease prediction.  
It includes implementations for:
- `LogisticRegression`  
- `RandomForestClassifier`  
- `XGBClassifier`  
- `CatBoostClassifier`  

Each script is modular, with functionality for:
- Model training  
- Hyperparameter tuning using **Optuna**  
- Evaluation metrics (Accuracy, Precision, Recall, F1-Score, ROC-AUC)  
- Saving the best trained model as `.pkl` for deployment in the Streamlit dashboard  

---

## 🔄 Execution Flow

1. **`notebooks/data_preprocessing.ipynb`**  
   → Clean and prepare the dataset for modeling.

2. **`models/`**  
   → Train and evaluate classification models.  
   → Export the best model to the `lib/` folder for integration with the web application.

---

## 🧠 Usage Notes

- Run the **notebook** first to preprocess and generate clean data.  
- Train models using scripts in the **`models/`** folder.  
- The best-performing model is saved to the `lib/` directory for prediction within the Streamlit app.  
- Execution order: `notebooks → models → webapp`.

---

## ⚖️ LICENSE

This project is proprietary. All rights reserved © 2025 Gerrald Andersen.  
No part of this repository may be copied, modified, reused, or redistributed without explicit written permission.

![License: Proprietary](https://img.shields.io/badge/license-Proprietary-red.svg)
