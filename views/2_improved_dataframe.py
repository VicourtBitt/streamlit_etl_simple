import streamlit as st
from utils.data_utils import with_empty_values, display_dataframe, gather_data, without_empty_values

def main():
    st.title("Engenharia de Dados")
    st.markdown("""
        Nesta seção, vamos explorar como melhorar a visualização de dados
        e realizar limpeza de dados para uma melhor análise.
    """)

    st.divider()

    st.subheader("Dados com Valores Vazios")
    st.markdown("""        Abaixo estão os dados que contêm valores vazios. Vamos identificar
        esses valores e discutir como podemos melhorá-los.
    """)
    df = with_empty_values(gather_data())
    if df is not None and not df.empty:
        display_dataframe(df)
    else:
        st.warning("No data available to display.")

    st.subheader("Análise Rápida")
    st.markdown("""
        Podemos notar que, existem 9 linhas com informações faltantes, sendo uma linha
        inteira com valores nulos e uma com valores faltantes em relaçãao a coluna `sex`.
        Podemos remover essas linhas ou preencher os valores faltantes com a média, mediana
        ou moda, dependendo do contexto dos dados.
    """)

    st.divider()
    st.subheader("Processo de Limpeza de Dados")
    st.markdown("""
        Podemos facilmente de maneira programática remover esses valores utilizando o Pandas.
        Abaixo está um exemplo de como podemos fazer isso:
    """)
    st.code("""
        df = gather_data()
        df = df.dropna()  # Remove todas as linhas com valores nulos""", language='python') 
    
    st.divider()
    st.subheader("Dados sem Valores Vazios")
    st.markdown("""
        Abaixo estão os dados após a remoção dos valores vazios. Agora podemos
        realizar análises mais precisas e significativas.
    """)
    df = without_empty_values(gather_data())
    if df is not None and not df.empty:
        display_dataframe(df)
    else:
        st.warning("No data available to display.")

main()