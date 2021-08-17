import streamlit as st
from predict_page import show_predict_page
from explore_page import show_dashboard_page


page = st.sidebar.selectbox("Dashboard or Predict", ("Dashboard", "Predict"))

if page == "Predict":
    show_predict_page()
else:
    show_dashboard_page()

