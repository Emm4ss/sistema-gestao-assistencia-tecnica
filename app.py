import streamlit as st
from streamlit_option_menu import option_menu

if "alto_contraste" not in st.session_state:
    st.session_state.alto_contraste = False

if "fonte" not in st.session_state:
    st.session_state.fonte = 16

st.set_page_config(layout="wide")
st.markdown("""
<style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.markdown("## ♿ Acessibilidade")

    if st.button("🌙 Alternar Alto Contraste"):
        st.session_state.alto_contraste = (
            not st.session_state.alto_contraste
        )

    st.session_state.fonte = st.slider(
        "Tamanho da Fonte",
        min_value=12,
        max_value=28,
        value=st.session_state.fonte
    )

    st.divider()

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
    st.nome = st.text_input("Nome")

    if st.button("Salvar Cliente"):
        st.success("Cliente salvo!")

elif selecionado == "Equipamentos":

    st.title("📱 Equipamentos")

    st.write("Cadastro de equipamentos")
    
if st.session_state.alto_contraste:

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-color: #000000;
            color: #ffffff;
            font-size: {st.session_state.fonte}px;
        }}

        h1,h2,h3,h4,h5,h6,p,label,span {{
            color:white !important;
            font-size: {st.session_state.fonte}px !important;
        }}

        section[data-testid="stSidebar"] {{
            background-color:#111111;
        }}

        .stButton button {{
            background-color:#ffff00;
            color:#000000;
            font-weight:bold;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        f"""
        <style>

        .stApp {{
            font-size:{st.session_state.fonte}px;
        }}

        h1,h2,h3,h4,h5,h6,p,label,span {{
            font-size:{st.session_state.fonte}px !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )