import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from datetime import datetime, timedelta

sns.set(style='dark')

# Mendapatkan tanggal sekarang
current_date = datetime.now().date()

# Mendefinisikan rentang waktu, misalnya 7 hari ke belakang dari tanggal sekarang
start_date = current_date - timedelta(days=365)
end_date = current_date

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/gloryindahs/bike-sharing/raw/main/bike.png")
    
    # Mengambil start_date & end_date dari date_input
    selected_dates = st.date_input(
        label='Rentang Waktu',
        min_value=datetime(2011, 1, 1).date(),
        max_value=datetime(2012, 12, 31).date(),
        value=[start_date, end_date]
    )
    
st.header('Bike Share Dashboard :sparkles:')

st.markdown('### Jumlah Sewa Sepeda Berdasarkan Musim, Cuaca, Suhu, dan Suhu Terasa')
# Membagi layar menjadi dua kolom untuk musim dan cuaca
col1, col2 = st.columns(2)

# Scatter plot untuk Musim
with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    season_mapping = {1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    day_df['season_name'] = day_df['season'].map(season_mapping)
    sns.barplot(x='season_name', y='cnt', data=day_df, palette="Blues_d")
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Musim')
    ax.set_xlabel('season')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot(fig)

# Scatter plot untuk Kondisi Cuaca
with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    weathersit_mapping = {1: 'Few clouds', 2: 'Mist', 3: 'Light Snow', 4: 'Snow + Fog'}
    day_df['weathersit_name'] = day_df['weathersit'].map(weathersit_mapping)
    sns.barplot(x='weathersit_name', y='cnt', data=day_df, palette="Blues_d")  
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Kondisi Cuaca')
    ax.set_xlabel('weathersit')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot(fig)

# Membagi layar menjadi dua kolom untuk suhu dan suhu terasa
col1, col2 = st.columns(2)

# Scatter plot untuk Suhu
with col1:
    sample_df = day_df.sample(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='temp', y='cnt', data=sample_df, palette="Blues_d")
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Suhu')
    ax.set_xlabel('temp')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot(fig)

# Scatter plot untuk Suhu Terasa
with col2:
    sample_df = day_df.sample(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='atemp', y='cnt', data=sample_df, palette="Blues_d")
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Suhu Terasa')
    ax.set_xlabel('atemp')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot(fig)



st.markdown('### Kolerasi antara Jumlah Sepeda Sewaan dengan Suhu, Kelembaban, dan Kecepatan Angin')
# Membagi layar menjadi dua kolom untuk msuhu dan kelembaban
col1, col2, = st.columns(2)

# Scatter plot untuk Korelasi Suhu vs Jumlah Sewa Sepeda
with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=day_df)
    ax.set_title('Korelasi Suhu vs Jumlah Sewa Sepeda')
    ax.set_xlabel('temp')
    ax.set_ylabel('Jumlah Sepeda')
    st.pyplot(fig)

# Scatter plot untuk Korelasi Kelembaban vs Jumlah Sewa Sepeda
with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='hum', y='cnt', data=day_df)
    ax.set_title('Korelasi Kelembaban vs Jumlah Sewa Sepeda')
    ax.set_xlabel('hum')
    ax.set_ylabel('Jumlah Sepeda')
    st.pyplot(fig)

# Scatter plot untuk Korelasi Kecepatan Angin vs Jumlah Sewa Sepeda
col1, = st.columns(1)
with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='windspeed', y='cnt', data=day_df)
    ax.set_title('Korelasi Kecepatan Angin vs Jumlah Sewa Sepeda')
    ax.set_xlabel('windspeed')
    ax.set_ylabel('Jumlah Sepeda')
    st.pyplot(fig)

st.markdown('### Jumlah Sewa Sepeda Selama Dua Tahun Terakhir')
# Membagi layar menjadi dua kolom untuk hari dan bulan
col1, col2, = st.columns(2)

# Scatter plot untuk Jumlah Sewa Sepeda Berdasarkan hari dan bulan
with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    weekday_mapping = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    day_df['weekday_name'] = day_df['weekday'].map(weekday_mapping)
    sns.barplot(x='weekday_name', y='cnt', data=day_df, palette="Blues_d")  
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Setiap Harinya')
    ax.set_xlabel('weekday')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    month_mapping = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
        7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    day_df['month_name'] = day_df['mnth'].map(month_mapping)
    sns.barplot(x='month_name', y='cnt', data=day_df, palette="Blues_d")  
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Setiap Bulan')
    ax.set_xlabel('month')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot(fig)

# Scatter plot untuk Jumlah Sewa Sepeda pada setiap Bulan dalam Dua Tahun Terakhir
col1, = st.columns(1)
with col1:
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='mnth', y='cnt', data=day_df, hue='yr', palette='Blues')
    ax.set_title('Jumlah Sewa Sepeda Tiap Bulan dalam 2 Tahun Terakhir')
    ax.set_xlabel('Month')
    ax.set_ylabel('Jumlah Sewa Sepeda')
    ax.legend(title='year')
    st.pyplot(fig)

