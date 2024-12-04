import streamlit as st
import matplotlib.pyplot as plt
import random
from io import BytesIO
import time
import webbrowser
from time import sleep

# Configuração inicial da página

st.set_page_config(page_title="Sistema de Votação com Gráfico", layout="centered")

# Títulos e descrição
st.title("🗳️ Sistema de Votação")
st.write("Vote com cuidado! Veja com atenção o discurso de cada um, e então vote. Você só pode votar uma vez!")

# Variáveis de estado para armazenar votos
if "votos_candidato1" not in st.session_state:
    st.session_state.votos_candidato1 = 0

if "votos_candidato2" not in st.session_state:
    st.session_state.votos_candidato2 = 0

if "ja_votou" not in st.session_state:
    st.session_state.ja_votou = False

# Verifica se o usuário já votou

col1, col2 = st.columns(2)

with col1:
    if st.button("Discurso do candidato 1"):
        webbrowser.open("https://drive.google.com/file/d/1YJOv0VQ5r7zRlWuPXgO2Dnzn5vA9S4Yb/view")
with col2:
        if st.button("Discurso do candidato 2"):
            webbrowser.open("https://drive.google.com/file/d/1bkQBIT-VOzSOpsaIwRznS-MUA1daJItR/view")

if st.session_state.ja_votou:
    st.warning("Você já votou! Obrigado por participar.")
else:
    # Botões de votação
    col3, col4 = st.columns(2)

    with col3:
        if st.button("Votar no Candidato 1"):  
            st.session_state.votos_candidato1 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 1!")
 
    with col4:
        if st.button("Votar no Candidato 2"):
            st.session_state.votos_candidato2 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 2!")
            
col5, col6 = st.columns(2)
with col5:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZKGt2jCtNO-DJdIg4em02pymsSpmODM9GFg&s", width=160)
with col6:
    st.image("data:image/jpeg;base64,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", width=160)

if st.button("Ver resultado"):
    st.success("Transferindo")
    sleep(0.5)
    st.switch_page("pages/resultado.py")
