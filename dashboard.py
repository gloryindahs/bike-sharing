import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

day_df = pd.read_csv("https://raw.githubusercontent.com/gloryindahs/bike-sharing/main/day.csv")

st.header('Bike Share Dashboard :sparkles:')
st.subheader('Rata-Rata Jumlah Sewa Sepeda Berdasarkan Musim dan Cuaca')
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 6))

# Grafik pertama: Musim
sns.barplot(x='season', y='cnt', data=result_df, palette="Blues_d", ax=axes[0])
axes[0].set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Musim')
axes[0].set_xlabel('Musim')
axes[0].set_ylabel('Rata-rata Jumlah Sepeda')

# Grafik kedua: Kondisi Cuaca
sns.barplot(x='weathersit', y='cnt', data=day_df, palette="Blues_d", ax=axes[1])
axes[1].set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Kondisi Cuaca')
axes[1].set_xlabel('Kondisi Cuaca')
axes[1].set_ylabel('Rata-rata Jumlah Sepeda')

# Tampilkan plot
plt.tight_layout()
plt.show()
