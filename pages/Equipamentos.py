import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "data/assistencia.db"
)

clientes = pd.read_sql(
    "SELECT id,nome FROM clientes",
    conn
)

st.title("Equipamentos")

cliente = st.selectbox(
    "Cliente",
    clientes["nome"]
)

tipo = st.selectbox(
    "Tipo",
    ["Celular", "Notebook", "Tablet"]
)

marca = st.text_input("Marca")
modelo = st.text_input("Modelo")
problema = st.text_area("Problema")

if st.button("Salvar"):

    cliente_id = clientes[
        clientes["nome"] == cliente
    ]["id"].iloc[0]

    conn.execute("""
    INSERT INTO equipamentos
    (cliente_id,tipo,marca,modelo,problema)
    VALUES(?,?,?,?,?)
    """,
    (cliente_id,tipo,marca,modelo,problema))

    conn.commit()

    st.success("Equipamento cadastrado")