import streamlit as st
import pandas as pd
from utils.data_utils import gather_data, display_dataframe

def main():
    st.title("Visualização de Dados com Streamlit")
    st.markdown("""
        Abaixo está uma tabela de visualização de dados.
        Você pode interagir com a tabela, filtrando e ordenando os dados.
    """)
    
    st.divider()
    st.subheader("Tabela de Dados")
    df = gather_data()
    if df is not None and not df.empty:
        display_dataframe(df)
    else:
        st.warning("No data available to display.")

    st.subheader("Legendas dos Dados")
    st.markdown("""
        A tabela acima contém informações sobre pinguins, incluindo:
        - **Culmen Length (mm)**: Comprimento do bico em milímetros
        - **Culmen Depth (mm)**: Profundidade do bico em milímetros
        - **Flipper Length (mm)**: Comprimento da nadadeira em milímetros
        - **Body Mass (g)**: Massa corporal em gramas
        - **Sex**: Sexo do pinguim (masculino ou feminino)
    """)

    st.divider()
    st.subheader("Limpeza e Melhoria de Dados")
    st.markdown("""
        Algo que podemos ver é, existem valores que estão faltando e campos que não
        estão preenchidos. Podemos fazer uma limpeza de dados para remover esses valores
        e melhorar a visualização da tabela.
        Podemos também adicionar mais colunas, como por exemplo, a coluna de `species` que
        representa a espécie do pinguim.
    """)

main()