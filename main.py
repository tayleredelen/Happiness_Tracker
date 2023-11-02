import streamlit as st
import plotly.express as px

st.title("Happiness Data by Country")
x = st.selectbox("Select the data for the X axis", ("GDP", "Happiness", "Generosity"))
y = st.selectbox("Select the data for the Y axis", ("GDP", "Happiness", "Generosity"))

st.subheader(f"{x} and {y}")

figure = px.scatter(x=x, y=y, labels="x": x, "y": y)

st.plotly_chart(figure)
