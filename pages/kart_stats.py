import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")
df_kart = pd.read_csv('data/kart_stats.csv')

df_kart = df_kart[['Body','Weight','Acceleration','On-Road traction','Mini-Turbo','Ground Speed','Ground Handling']]
st.dataframe(df_kart)

st.dataframe(df_kart.style
.highlight_max(color='green', axis=0, subset=['Body','Weight','Acceleration','On-Road traction','Mini-Turbo','Ground Speed','Ground Handling'])
.highlight_min(color='red', axis=0, subset=['Body','Weight','Acceleration','On-Road traction','Mini-Turbo','Ground Speed','Ground Handling']))

st.line_chart(df_kart,x='Body',y=['Weight','Acceleration','On-Road traction','Mini-Turbo','Ground Speed','Ground Handling'])

st.bar_chart(df_kart, x='Body', y='Acceleration', width=0, height=0, use_container_width=True)

chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]
df_single_kart = df_single_kart.drop(columns=['Body'])
df_unp_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)
st.bar_chart(df_unp_kart, x='category', y='strength')
