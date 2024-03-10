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

# Scatter plot untuk Musim
with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', data=day_df, palette="Blues_d")
    plt.title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot()

# Scatter plot untuk Kondisi Cuaca
with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=day_df, palette="Blues_d")
    plt.title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot()
