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
season_mapping = {1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
result_df = day_df.groupby(by="season").mean()['cnt'].sort_values(ascending=False).reset_index(drop=False)
result_df['season'] = result_df['season'].map(season_mapping)
print(result_df)  

plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=result_df, palette="Blues_d")
plt.title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Sepeda')
plt.show()
