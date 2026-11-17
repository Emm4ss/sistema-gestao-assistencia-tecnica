# pages/4_Relatorios.py

import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect(
    "data/assistencia.db"
)

query = """
SELECT
os.id,
c.nome,
e.marca,
e.modelo,
os.status,
os.valor
FROM ordens_servico os
INNER JOIN clientes c
ON os.cliente_id = c.id
INNER JOIN equipamentos e
ON os.equipamento_id = e.id
"""

df = pd.read_sql(query, conn)

st.title("Relatório Geral")

st.dataframe(
    df,
    use_container_width=True
)

st.subheader("OS por Status")

st.bar_chart(
    df["status"].value_counts()
)