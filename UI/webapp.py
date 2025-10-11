import streamlit as st
import pickle
import time
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title='Heart Disease Prediction',
    page_icon='📊',
    layout='wide'
)

# ---------------------- HEADER ----------------------
st.title("📊 Machine Learning Portfolio")
st.write("Welcome to the Heart Disease Prediction Portfolio App!")

st.warning("""
⚠️ **Disclaimer**  
1. This prediction tool is intended for informational purposes only.
2. It is not a substitute for professional medical advice, diagnosis, or treatment.
3. Always seek the advice of a qualified healthcare provider regarding any medical condition.
4. Never disregard professional medical advice or delay seeking it because of results from this tool.
5. The developer is not responsible for any decisions or actions taken based on the predictions provided.
""")

# ---------------------- FUNCTION: HEART DISEASE ----------------------
def heart():
    st.header("❤️ Heart Disease Prediction")
    st.write("""
    This app predicts the **Heart Disease Risk**  
    Data obtained from the [Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease) by UCIML.
    """)
    
    st.sidebar.header('User Input Features')

    # Upload file CSV
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
    else:
        def user_input_features():
            st.sidebar.subheader('Manual Input')

            cp = st.sidebar.slider(
                'Chest pain type', 0, 3, 1,
                help="Type of chest pain experienced"
            )
            cp_dict = {
                0: "Typical Angina",
                1: "Atypical Angina",
                2: "Non-Anginal Pain",
                3: "Asymptomatic"
            }
            st.sidebar.write(f"Chest Pain Type: {cp_dict[cp]}")

            thalach = st.sidebar.slider(
                'Maximum Heart Rate Achieved', 60, 220, 150
            )
            slope = st.sidebar.selectbox(
                'Slope of ST Segment', [0, 1, 2], index=0
            )
            oldpeak = st.sidebar.slider(
                'Oldpeak', 0.0, 6.2, 1.0, 0.1
            )
            exang = st.sidebar.radio(
                'Exercise Induced Angina', ['Yes', 'No']
            )
            exang = 1 if exang == 'Yes' else 0
            ca = st.sidebar.selectbox(
                'Number of Major Vessels', [0, 1, 2, 3], index=0
            )
            thal = st.sidebar.selectbox(
                'Thalassemia', [1, 2, 3], index=0
            )
            sex = st.sidebar.radio('Sex', ['Male', 'Female'], index=0)
            sex = 0 if sex == "Female" else 1
            age = st.sidebar.number_input(
                'Age', min_value=29, max_value=77, value=30, step=1
            )

            data = {
                'sex': sex,
                'age': age,
                'cp': cp,
                'thalach': thalach,
                'slope': slope,
                'exang': exang,
                'ca': ca,
                'thal': thal,
                'oldpeak': oldpeak
            }
            return pd.DataFrame(data, index=[0])

        input_df = user_input_features()

    st.image("https://drramjimehrotra.com/wp-content/uploads/2022/09/Women-Heart-Disease-min-resize.png")

    # Predict Button
    if st.sidebar.button('Predict!'):
        st.subheader("Input Data")
        st.write(input_df)
        
        model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib', 'best_classifier.pkl'))
        with open(model_path, 'rb') as file:
            loaded_model = pickle.load(file)
        
        prediction_proba = loaded_model.predict_proba(input_df)
        prediction = 1 if prediction_proba[:, 1] >= 0.4 else 0

        result = 'No Heart Disease Risk' if prediction == 0 else 'Heart Disease Risk Detected'

        st.subheader('Prediction:')
        with st.spinner('Wait for it...'):
            time.sleep(4)
            if result == "No Heart Disease Risk":
                st.success(f"Prediction : {result}")
            else:
                st.error(f"Prediction : {result}")
                st.info("Please consult a doctor for further evaluation and advice.")

# ---------------------- APP SELECTOR ----------------------
select_var = st.sidebar.selectbox(
    "Choose App",
    ["Heart Disease"]
)

if select_var == "Heart Disease":
    heart()
