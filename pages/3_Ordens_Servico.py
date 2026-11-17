# pages/3_Ordens_Servico.py

import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect(
    "data/assistencia.db"
)

st.title("Ordens de Serviço")

clientes = pd.read_sql(
    "SELECT * FROM clientes",
    conn
)

equipamentos = pd.read_sql(
    "SELECT * FROM equipamentos",
    conn
)

cliente = st.selectbox(
    "Cliente",
    clientes["nome"]
)

equipamento = st.selectbox(
    "Equipamento",
    equipamentos["modelo"]
)

descricao = st.text_area(
    "Descrição do Serviço"
)

if st.button("Abrir Ordem"):

    cliente_id = clientes[
        clientes["nome"] == cliente
    ]["id"].iloc[0]

    equipamento_id = equipamentos[
        equipamentos["modelo"] == equipamento
    ]["id"].iloc[0]

    conn.execute("""
    INSERT INTO ordens_servico
    (cliente_id,equipamento_id,descricao)
    VALUES(?,?,?)
    """,
    (
        cliente_id,
        equipamento_id,
        descricao
    ))

    conn.commit()

    st.success("OS criada")
    ordens = pd.read_sql("""
    SELECT *
    FROM ordens_servico
    """, conn)

    os_id = st.selectbox(
    "Selecionar OS",
    ordens["id"]
)

novo_status = st.selectbox(
    "Novo Status",
    [
        "Em Análise",
        "Em Manutenção",
        "Concluído",
        "Entregue"
    ]
)

if st.button("Atualizar"):

    conn.execute("""
    UPDATE ordens_servico
    SET status=?
    WHERE id=?
    """,
    (
        novo_status,
        os_id
    ))

    conn.commit()

    st.success(
        "Status atualizado com sucesso"
    )