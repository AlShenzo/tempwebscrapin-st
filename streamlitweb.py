import streamlit as st
import sqlite3
from plotly import express as px

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


dates = cursor.execute("SELECT date FROM temp")
date = [item[0] for item in dates]
temps = cursor.execute("SELECT temperature FROM temp")
temp = [item[0] for item in temps]

figure = px.line(x=date, y=temp,
                 labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)
