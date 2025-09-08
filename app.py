import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão

st.header('Clique no botão para criar um histograma')
if hist_button: # se o botão for clicado
# escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
# criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
# exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
    
graph_button = st.button('Criar gráfico de dispersão') # cria outro botão

st.header('Clique bo botão para criar um gráfio de dispersão')
if graph_button: #se o botão for clicado
# escrevendo uma mensagem
    st.write('criando um gráfico de disperão para o conjunto de dados de anúncios de vendas de carros')

# criar um gráfico de dispersão
    fig2 = px.scatter(car_data, x="odometer", y="price")
    
# exibir um gráfico Plotly interativo
    st.plotly_chart(fig2, use_container_width=True)