import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]



def show_predict_page():
    st.title("Breast Cancer Prediction")

    st.write("""According to global statistics, breast cancer (BC) is one of the most prevalent diseases among women globally,
     accounting for the majority of new cancer cases and cancer related deaths, making it a major public health issue in today's 
     society. 
        """)
    st.write("""Early detection of BC improves the prognosis and chances of survival by allowing patients to get timely therapeutic 
    therapy. Patients may avoid needless therapies if benign tumors are classified more precisely. As a result, accurate BC diagnosis 
    and categorization of individuals into malignant or benign groups is a hot topic of research. Machine learning (ML) is widely 
    acknowledged as the approach of choice in BC pattern classification and forecast modeling due to its unique benefits in detecting 
    important characteristics from complicated BC datasets. 
          """)
    st.write("""The use of classification and data mining technologies to categorize data is quite successful. Particularly in the medical 
    profession, where such approaches are frequently utilized in diagnosis and decision-making. 
        """)

    st.write("""### We need some information to predict if the cancer is Malignant or Benign""")


    radius_mean = st.number_input(
        "Radius Mean",
        min_value=0.0,
        max_value=30.000000,
        format="%.6f")
    perimeter_mean = st.number_input(
        "Perimeter Mean",
        min_value=0.0,
        max_value=200.000000,
        format="%.6f")
    area_mean = st.number_input(
        "Area Mean",
        min_value=0.0,
        max_value=2500.000000,
        format="%.6f")
    concavity_mean = st.number_input(
        "Concavity Mean",
        min_value=0.0,
        max_value=0.500000,
        format="%.6f")
    concave_points_mean = st.number_input(
        "Concave Points Mean",
        min_value=0.0,
        max_value=0.300000,
        format="%.6f")
    radius_worst = st.number_input(
        "Radius Worst",
        min_value=0.0,
        max_value=37.000000,
        format="%.6f")
    perimeter_worst = st.number_input(
        "Perimeter Worst",
        min_value=0.0,
        max_value=252.000000,
        format="%.6f")
    area_worst = st.number_input(
        "Area Worst",
        min_value=0.0,
        max_value=4254.000000,
        format="%.6f")
    concave_point_worst = st.number_input(
        "Concave Point Worst",
        min_value=0.0,
        max_value=0.300000,
        format="%.6f")

    predict_button = st.button("Predict")
    if predict_button:
        X = np.array([[radius_mean, perimeter_mean, area_mean, concavity_mean, concave_points_mean, radius_worst, perimeter_worst, area_worst, concave_point_worst]])
        X = X.astype(float)
        X = sc.fit_transform(X)

        prediction = model.predict(X)
        result = ""

        if prediction[0] == 1:
            result = "Cancer Tumor is Malignant"
        else:
            result = "Cancer Tumor is Benign"

        st.subheader(result)

    st.write("""### Objective
    The goal of this study is to identify which features are most useful in predicting whether a cancer 
    is malignant or benign, as well as to look for general trends that might help us pick models and hyper-parameters. 
    After running through a correlation test, we found 9 main features that mostly influence the output of our prediction. 
    Logistic Regression model was chosen among other classification models with an accuracy of 95.3%. 
    """)





