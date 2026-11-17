st.header("Nova Ordem de Serviço")

col1,col2 = st.columns(2)

with col1:

    nome = st.text_input(
        "Nome do Cliente *"
    )

with col2:

    telefone = st.text_input(
        "Telefone *"
    )

email = st.text_input(
    "E-mail"
)

st.divider()

col1,col2 = st.columns(2)

with col1:

    tipo = st.selectbox(
        "Tipo",
        [
            "Celular",
            "Notebook",
            "Tablet"
        ]
    )

    modelo = st.text_input(
        "Modelo"
    )

with col2:

    marca = st.text_input(
        "Marca"
    )

    serie = st.text_input(
        "Número de Série"
    )

problema = st.text_area(
    "Problema Relatado"
)

obs = st.text_area(
    "Observações"
)

salvar = st.button(
    "💾 Salvar Ordem de Serviço"
)