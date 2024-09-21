import pandas as pd
import streamlit as st
from plotly import express as px

df = pd.read_csv('data.txt')
dates = df['date']
temp = df['temperature']


figure = px.line(x=dates, y=temp, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)
