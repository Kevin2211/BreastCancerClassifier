import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



@st.cache
def load_data():
    df = pd.read_csv("data.csv")
    cols = [1, 2, 4, 5, 8, 9, 22, 24, 25, 29]
    df = df[df.columns[cols]]

    return df

df = load_data()
print(df)

def show_dashboard_page():
    st.title("Breast Cancer Data Set Dashboard")

    st.write(
        """
    ### Breast Cancer Wisconsin (Diagnotic) Data Set 2020
    """
    )

    data = df["diagnosis"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Percentage of Benign and Malignant from data""")

    st.pyplot(fig1)

    st.write("""#### Malignant and Benign Data Based on Perimeter Mean""")

    data = df.groupby(['diagnosis'])["perimeter_mean"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Malignant and Benign Data Based on Radius Mean""")

    data = df.groupby(['diagnosis'])["radius_mean"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Malignant and Benign Data Based on Area Mean""")

    data = df.groupby(['diagnosis'])["area_mean"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Malignant and Benign Data Based on Concavity Mean""")

    data = df.groupby(['diagnosis'])["concavity_mean"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Malignant and Benign Data Based on Concave Point Mean""")

    data = df.groupby(['diagnosis'])["concave points_mean"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Malignant and Benign Data Based on Radius Worst""")

    data = df.groupby(['diagnosis'])["radius_mean"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Malignant and Benign Data Based on Perimeter Worst""")

    data = df.groupby(['diagnosis'])["perimeter_worst"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Malignant and Benign Data Based on Area Worst""")

    data = df.groupby(['diagnosis'])["area_worst"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Malignant and Benign Data Based on Concave Points Worst""")

    data = df.groupby(['diagnosis'])["concave points_worst"].mean().sort_values(ascending=True)
    st.bar_chart(data)








