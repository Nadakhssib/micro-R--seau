import pandas as pd
import streamlit as st
import plotly.graph_objs as go
import time

# Load the data
excel_file = r'donnee par heure last - Copie.xlsx'
data = pd.read_excel(excel_file, sheet_name='Feuil1')

# Set up the Streamlit app
st.title("Mode En ligne⚡")

# Create an empty plot
plotly_fig = go.Figure()
plotly_fig.add_trace(go.Scatter(x=[], y=[], mode='lines', name='Consommation en W'))
plotly_fig.add_trace(go.Scatter(x=[], y=[], mode='lines', name='Production Solaire en W'))
plotly_fig.add_trace(go.Scatter(x=[], y=[], mode='lines', name='Puissance batterie en W'))
plotly_fig.update_layout(xaxis_title='Temps', yaxis_title='Valeur en Watt')

plot_placeholder = st.empty()

# Function to update the plot
def update_plot(index):
    consommation = data['charge'].iloc[:index].values
    production_solaire = data['puissance PV'].iloc[:index].values
    batterie_charge = data['batterie'].iloc[:index].values
    temps = data.index[:index]

    plotly_fig.data[0].x = temps
    plotly_fig.data[0].y = consommation
    plotly_fig.data[1].x = temps
    plotly_fig.data[1].y = production_solaire
    plotly_fig.data[2].x = temps
    plotly_fig.data[2].y = batterie_charge

    plot_placeholder.plotly_chart(plotly_fig, use_container_width=True)

# Initial index
index = 1

# Periodically update the plot
while index <= len(data):
    update_plot(index)
    index += 1
    time.sleep(1)
