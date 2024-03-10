import pandas as pd
import streamlit as st
import plotly.express as px

# Load your data
day_df = pd.read_csv("day.csv")

# Set up Streamlit
st.header('Bike Share Dashboard :sparkles:')

# Create two columns layout
col1, col2 = st.columns(2)

# Subheader for the section
st.subheader('Rata-Rata Jumlah Sewa Sepeda Berdasarkan Musim dan Cuaca')

# Left column: Season-wise bike share count
with col1:
    season_count = day_df.groupby("season_label")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="season_label", y="cnt", title="Jumlah Penyewa berdasarkan Musim")
    
    # Display the plot in Streamlit
    st.plotly_chart(fig_season_count, use_container_width=True, height=400, width=600)

# Right column: Weather situation-wise bike share count
with col2:
    weather_count = day_df.groupby("weathersit")["cnt"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weathersit", y="cnt", title="Jumlah Penyewa berdasarkan Cuaca")
    
    # Display the plot in Streamlit
    st.plotly_chart(fig_weather_count, use_container_width=True, height=400, width=800)
