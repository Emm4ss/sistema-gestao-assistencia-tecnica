# pages/1_Clientes.py

import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("data/assistencia.db")

st.title("Cadastro de Clientes")

with st.form("cliente"):

    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone")
    email = st.text_input("Email")

    salvar = st.form_submit_button("Salvar")

    if salvar:

        conn.execute("""
        INSERT INTO clientes(nome, telefone, email)
        VALUES(?,?,?)
        """, (nome, telefone, email))

        conn.commit()

        st.success("Cliente cadastrado!")

df = pd.read_sql(
    "SELECT * FROM clientes",
    conn
)

st.dataframe(df)