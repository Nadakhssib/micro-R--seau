import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données
df = pd.read_excel('data.xlsx')
data_achat = df.set_index('date')['achat']
data_vente = df.set_index('date')['vente']

# Définir la page Streamlit
def display_finance_page():
    st.title("Étude Financière 📈")
    st.subheader("📆 Du 01 Jan 2023 au 31 Déc 2023")
    

    chart_type = st.selectbox("Sélectionnez le type de graphique", ["Barres", "Courbes"])
    
    if chart_type == "Barres":
        st.bar_chart(pd.concat([data_achat, data_vente], axis=1))
    elif chart_type == "Courbes":
        st.line_chart(pd.concat([data_achat, data_vente], axis=1))


# Exécuter l'application Streamlit
if __name__ == "__main__":
    display_finance_page()
