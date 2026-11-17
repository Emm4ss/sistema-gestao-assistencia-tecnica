# app.py

import streamlit as st
from database import criar_banco

criar_banco()

st.set_page_config(
    page_title="Assistência Técnica",
    layout="wide"
)

st.title("🔧 Sistema de Gestão para Assistência Técnica")

st.write("""
Sistema para gerenciamento de:

- Clientes
- Equipamentos
- Ordens de Serviço
- Histórico de Atendimentos
""")