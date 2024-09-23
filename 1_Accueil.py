import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

st.set_page_config(layout="wide")
st.title('ÉcoRéseau')
st.subheader('📆 du 1 jan 2023 au 31 dec 2023')
df = pd.read_excel('data.xlsx')
data_pv = df.set_index('date')['puissance_pv']
data_cons = df.set_index('date')['puissance_charge1']
data_achat = df.set_index('date')['achat']
data_vente = df.set_index('date')['vente']

if all(col in df.columns for col in ['puissance_réseau','puissance_pv', 'puissance_batterie', 'puissance_charge1']):
    max_réseau = df['puissance_réseau'].max()
    max_pv = df['puissance_pv'].max()
    max_batterie = df['puissance_batterie'].max()
    max_charge1 = df['puissance_charge1'].max()

    a1, a2, a3, a4, a5 = st.columns(5)
    a1.metric("Réseau ⚡", f"{max_réseau:.0f} W")
    a2.metric("Solaire ☀️", f"{max_pv:.0f} W")
    a3.metric("Batterie 🔋", f"{max_batterie:.0f} W")
    a4.metric("Charge 💡", f"{max_charge1:.0f} W")
    a5.metric("Etat de charge 🔌", f"{90} %")

    total_cons = data_cons.sum()
    total_achat = data_achat.sum()
    total_vente = data_vente.sum()

    sizes = [total_cons, total_achat, total_vente]

    labels = ['Consommation\nTotale', 'Total \nAchat', 'Total \nVente']
    custom_colors = ['#BFE095', '#E05634', '#345FE0']  # Define your custom colors

    # Create columns
    col1, col2 = st.columns(2)

    # Display pie chart in the first column
    with col1:
        fig_secteur, ax_secteur = plt.subplots(figsize=(6, 4))
        wedges, texts, autotexts = ax_secteur.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4), colors=custom_colors)
        ax_secteur.axis('equal')  

        for text in texts:
            text.set_fontsize(10)
        for autotext in autotexts:
            autotext.set_fontsize(8)

        canvas_secteur = FigureCanvas(fig_secteur)
        st.pyplot(fig_secteur)

    # Display bar chart in the second column
    with col2:
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.bar(data_pv.index, data_pv, color='#345FE0', label='Puissance PV', width=0.8)
        ax2.bar(data_cons.index, data_cons, color='#BFE095', label='Consommation', width=0.8)
        ax2.set_title('Production & Consommation')
        ax2.set_ylabel('W')
        ax2.legend()
        st.pyplot(fig2)