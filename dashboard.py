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
    season_mapping = {1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    day_df['season_name'] = day_df['season'].map(season_mapping)
    sns.barplot(x='season', y='cnt', data=day_df, palette="Blues_d")
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Musim')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

# Scatter plot untuk Kondisi Cuaca
with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=day_df, palette="Blues_d")
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Kondisi Cuaca')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
