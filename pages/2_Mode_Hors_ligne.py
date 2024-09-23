import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title('Mode Hors ligne 🔌')

st.subheader('📆 du 1 jan 2023 au 31 dec 2023')

df = pd.read_excel(r'C:\PFE\data.xlsx')

data_pv = df.set_index('date')['puissance_pv']
data_reseau = df.set_index('date')['puissance_réseau']
data_cons = df.set_index('date')['puissance_charge1']
data_ex = df.set_index('date')['energie_Transmise']

container_main = st.container()
container_extra = st.container()

fig_cons, ax = plt.subplots(figsize=(8, 6))
bar_width = 0.4
bar_positions = np.arange(len(data_cons))
ax.bar(bar_positions, data_cons, color='#E05634', label='Consommation', width=bar_width)
ax.bar(bar_positions + bar_width, data_ex, color='#345FE0', label='Transfert au réseau', width=bar_width)
plt.title('Consommation & Transfert au Réseau')
plt.ylabel('W')
plt.legend()
plt.xticks(bar_positions, df['date']) 

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(data_pv.index, data_pv, color='#345FE0', label='Puissance PV', width=0.8)
ax.bar(data_reseau.index, data_reseau, color='#BFE095', label='Puissance Réseau', width=0.8)
plt.title('Production électrique mensuelle')
plt.ylabel('W')
plt.legend()

total_pv = data_pv.sum()
total_reseau = data_reseau.sum()
sizes = [total_pv, total_reseau]
labels = ['Puissance PV', 'Puissance Réseau']
colors = ['#345FE0', '#BFE095']
fig_donut, ax_donut = plt.subplots(figsize=(4, 3))
ax_donut.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
centre_circle = plt.Circle((0,0),0.70,fc='white')
ax_donut.add_artist(centre_circle)

data_reseau_extra = df.set_index('date')['puissance_batterie']
fig_extra, ax_extra = plt.subplots(figsize=(8, 6))
ax_extra.plot(data_reseau_extra.index, data_reseau_extra, color='#8B5B4F', label='Puissance batterie')
plt.title('Puissance batterie')
plt.ylabel('w')
plt.xticks(rotation=45)
plt.legend()

container1 = st.container()
col1, col2 = st.columns(2)

with container1:
    with col1:
        st.pyplot(fig)  
    with col2:
        st.pyplot(fig_donut)  

container2 = st.container()
col3, col4 = st.columns(2)

with container2:
    with col3:
        st.pyplot(fig_extra)
    with col4:
        st.pyplot(fig_cons) 
