import streamlit as st

st.title("Bem-vindo!")

st.write("Faça login para acessar o sistema")

with st.form("login"):

    usuario = st.text_input("Usuário")

    senha = st.text_input(
        "Senha",
        type="password"
    )

    entrar = st.form_submit_button(
        "Entrar"
    )

    if entrar:

        if usuario == "tecnico01" and senha == "123":

            st.success(
                "Login realizado!"
            )

        else:

            st.error(
                "Usuário ou senha inválidos."
            )