import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

day_df = pd.read_csv("day.csv")

st.header('Bike Share Dashboard :sparkles:')
st.subheader('Rata-Rata Jumlah Sewa Sepeda Berdasarkan Musim dan Cuaca')

# Membagi layar menjadi dua kolom
col1, col2 = st.columns(2)

# Scatter plot untuk Suhu
with col1:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=day_df)
    plt.title('Korelasi Suhu vs Jumlah Sewa Sepeda')
    plt.xlabel('Suhu')
    plt.ylabel('Jumlah Sepeda')
    st.pyplot()

# Scatter plot untuk Kelembaban
with col2:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='hum', y='cnt', data=day_df)
    plt.title('Korelasi Kelembaban vs Jumlah Sewa Sepeda')
    plt.xlabel('Kelembaban')
    plt.ylabel('Jumlah Sepeda')
    st.pyplot()
