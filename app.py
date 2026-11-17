import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
st.markdown("""
<style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:

    selecionado = option_menu(
        "Assistência Técnica",
        [
            "Início",
            "Nova Ordem",
            "Consultar Ordens",
            "Clientes",
            "Equipamentos"
        ],
        icons=[
            "house-fill",
            "file-earmark-plus-fill",
            "list-task",
            "people-fill",
            "phone-fill"
        ],
        default_index=0
    )

# Exibe a página selecionada

if selecionado == "Início":

    st.title("🏠 Dashboard")
    st.write("Página inicial do sistema")

elif selecionado == "Nova Ordem":

    st.title("📄 Nova Ordem de Serviço")

    cliente = st.text_input("Cliente")
    equipamento = st.text_input("Equipamento")
    problema = st.text_area("Problema")

    if st.button("Salvar"):
        st.success("Ordem criada com sucesso!")

elif selecionado == "Consultar Ordens":

    st.title("📋 Consultar Ordens")

    st.write("Lista de Ordens de Serviço")

elif selecionado == "Clientes":

    st.title("👥 Clientes")

    st.write("Cadastro de clientes")

elif selecionado == "Equipamentos":

    st.title("📱 Equipamentos")

    st.write("Cadastro de equipamentos")
