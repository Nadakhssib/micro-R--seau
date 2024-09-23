import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date

# Chargement des données depuis le fichier Excel
@st.cache_data
def load_data():
    return pd.read_excel(r'histMeteo.xlsx')

df = load_data()

# Interface utilisateur
st.title('Analyse des données météorologiques')

start_date = st.date_input('Date de début')
end_date = st.date_input('Date de fin')

if start_date < end_date:
    start_date = datetime.combine(start_date, datetime.min.time())
    end_date = datetime.combine(end_date, datetime.max.time())
    filtered_df = df[(df['date2'] >= start_date) & (df['date2'] <= end_date)]
    st.write(filtered_df)

    if st.button('Tracer les courbes'):
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

        # Tracé de la température
        ax1.plot(filtered_df['date2'], filtered_df['temperature'], color='#E05634')
        ax1.set_title('Température')
        ax1.set_ylabel('°C')

        # Tracé de la radiation
        ax2.plot(filtered_df['date2'], filtered_df['radiation'], color='#345FE0')
        ax2.set_title('Radiation')
        ax2.set_ylabel('kWh/m²')

        st.pyplot(fig)
else:
    st.error('Veuillez sélectionner une date de début antérieure à la date de fin.')

