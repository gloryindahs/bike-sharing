import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

day_df = pd.read_csv("day.csv")

st.header('Bike Share Dashboard :sparkles:')

col1, col2 = st.columns(2)
st.subheader('Rata-Rata Jumlah Sewa Sepeda Berdasarkan Musim dan Cuaca')

with col1:  
 season_count = data.groupby("season_label")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="season_label",
                              y="cnt", title="Jumlah Penyewa berdasarkan Musim")
    st.plotly_chart(fig_season_count, use_container_width=True,
                    height=400, width=600)

with col2:
    # Weather situation-wise bike share count
    # st.subheader("Weather Situation-wise Bike Share Count")

    weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weathersit",
                               y="cnt", title="Jumlah Penyewa berdasar Cuaca")
    # Mengatur tinggi dan lebar gambar
    st.plotly_chart(fig_weather_count, use_container_width=True,height=400, width=800)

