import pandas as pd
import plotly.express as px
import streamlit as st
df = pd.read_csv('vehicles_us.csv')

st.header("Análisis de Vehículos en Venta")
if st.button("Mostrar histograma del odómetro"):
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig)
if st.button("Mostrar gráfico de dispersión (Precio vs Odómetro)"):
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig)
