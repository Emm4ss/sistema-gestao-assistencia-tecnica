import pandas as pd

df = pd.DataFrame(
    {
        "OS":[
            "OS001",
            "OS002",
            "OS003"
        ],

        "Cliente":[
            "João Silva",
            "Maria Oliveira",
            "Carlos Santos"
        ],

        "Equipamento":[
            "Galaxy A54",
            "Moto G84",
            "Dell Inspiron"
        ],

        "Status":[
            "Em Manutenção",
            "Em Análise",
            "Concluído"
        ]
    }
)

st.header(
    "Ordens de Serviço"
)

st.success(
    "Status atualizado com sucesso."
)

pesquisa = st.text_input(
    "Pesquisar"
)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)