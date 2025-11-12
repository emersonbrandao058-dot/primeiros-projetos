# primeiro grande código
# autor: Emerson Brandão
# data: 12/11/2025

import psutil
from datetime import datetime
import streamlit as st
import pandas as pd
import time 

# VARIÁVEIS
CPU_LIMITE = 80
MEMORIA_LIMITE = 80
INTERVALO = 1 
PERIODO_MEDIA = 300

# HISTÓRICO
if "historico_cpu" not in st.session_state:
    st.session_state.historico_cpu = []
    st.session_state.historico_memoria = []
    st.session_state.historico_tempo = []

# CABEÇALHO VISUAL
st.set_page_config(page_title="MONITOR INTELIGENTE", layout="wide")
st.markdown("""
    <h1 style='color:white;'>🧠 Monitor Inteligente de Sistema</h1>
    <hr style='border:1px solid gray'>
""", unsafe_allow_html=True)

placeholder = st.empty()

# COLETA DE DADOS
cpu = psutil.cpu_percent(interval=0.5)
memoria = psutil.virtual_memory().percent
tempo = datetime.now().strftime("%H:%M:%S")

# ATUALIZAÇÃO DO HISTÓRICO
st.session_state.historico_cpu.append(cpu)
st.session_state.historico_memoria.append(memoria)
st.session_state.historico_tempo.append(tempo)

# MANTER SOMENTE ÚLTIMOS 5 MINUTOS
if len(st.session_state.historico_cpu) > PERIODO_MEDIA:
    st.session_state.historico_cpu.pop(0)
    st.session_state.historico_memoria.pop(0)
    st.session_state.historico_tempo.pop(0)

# DATAFRAME
df = pd.DataFrame({
    "Tempo": st.session_state.historico_tempo,
    "CPU (%)": st.session_state.historico_cpu,
    "Memória (%)": st.session_state.historico_memoria
})

# GRÁFICOS LADO A LADO
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💻 CPU")
    st.line_chart(df.set_index("Tempo")[["CPU (%)"]])

with col2:
    st.markdown("### 🧠 Memória")
    st.line_chart(df.set_index("Tempo")[["Memória (%)"]])

# ALERTA VISUAL
if cpu > CPU_LIMITE or memoria > MEMORIA_LIMITE:
    st.markdown(
       f"<div style='background-color:red; color:white; padding:10px; border-radius:5px;'>"
       f"⚠️ Alerta! {'CPU Alta!' if cpu > CPU_LIMITE else ''} {'Memória Alta!' if memoria > MEMORIA_LIMITE else ''}</div>",
       unsafe_allow_html=True
    )
