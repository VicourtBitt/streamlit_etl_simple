import streamlit as st
import pandas as pd
from utils.data_utils import gather_data, display_dataframe

def main():
    st.set_page_config(
        page_title="DataFrame | VBittDashboard",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Visualização de Dados com Streamlit")
    st.markdown("""
        Abaixo está uma tabela de visualização de dados.
        Você pode interagir com a tabela, filtrando e ordenando os dados.
    """)
    
    st.divider()
    st.subheader("Tabela de Dados")
    st.markdown(""" Aqui teremos menos dados do que na tabela original, pois estamos utilizando apenas uma amostra para visualização.""")
    df = gather_data()
    if df is not None and not df.empty:
        display_dataframe(df[:11])
    else:
        st.warning("No data available to display.")

    st.subheader("Legendas dos Dados")
    st.markdown("""
        A tabela acima contém dados e estimativas psicológicas de pacientes que podem ter depressão, sendo elas:
        - `Name`: Nome do paciente
        - `Gender`: Gênero do paciente
        - `Age`: Idade do paciente
        - `City`: Cidade onde o paciente reside
        - `Working Professional or Student`: Indica se o paciente é um profissional ou estudante
        - `Profession`: Profissão do paciente
        - `Academic Pressure`: Pressão acadêmica que o paciente enfrenta
        - `Work Pressure`: Pressão de trabalho que o paciente enfrenta
        - `CGPA`: Cumulative Grade Point Average, média de notas do paciente
        - `Study Satisfaction`: Satisfação com os estudos
        - `Job Satisfaction`: Satisfação com o trabalho
        - `Sleep Hours`: Horas de sono do paciente
        - `Dietary Habits`: Hábitos alimentares do paciente
        - `Degree`: Grau de formação do paciente
        - `Have you ever had suicidal thoughts?`: Indica se o paciente já teve pensamentos suicidas
        - `Work/Study Hours`: Horas de trabalho ou estudo do paciente
        - `Financial Stress`: Estresse financeiro que o paciente enfrenta
        - `Family History of Mental Illness`: Histórico familiar de doenças mentais
        - `Depression`: Indica se o paciente foi diagnosticado com depressão
    """)

    st.divider()
    st.subheader("Estatisticas Descritivas")
    if df is not None and not df.empty:
        st.markdown("""
            Abaixo estão as estatísticas descritivas dos dados, que incluem medidas como média, mediana, desvio padrão, mínimo e máximo.
            Essas estatísticas ajudam a entender melhor a distribuição dos dados e identificar possíveis outliers.
        """)
        st.dataframe(df.describe())

    if df is not None and not df.empty:
        st.markdown("""
            Aqui abaixo seguem informações adicionais sobre o dataframe:    
        """)
        st.write(f"""Total de linhas: `{df.shape[0]}`""")
        st.write(f"""Total de colunas: `{df.shape[1]}`""")
        st.write(f"""Colunas: `{', '.join(df.columns)}`""")


    st.divider()
    st.subheader("Limpeza e Melhoria de Dados")
    st.markdown("""
        Algo que podemos notar são ruídos claros em nossos dados, como valores faltantes (por contexto) ou inconsistências.
        Podemos melhorar essa visualização separando os dados em tabelas auxiliares, como por exemplo, uma tabela especializada
        para pessoas que são profissionais ou estudantes, e outra para pessoas que não são.
        Além disso, podemos remover valores nulos ou preenchê-los com a média, mediana ou moda, dependendo do contexto dos dados.
        Isso nos permitirá realizar análises mais precisas e significativas.
    """)

main()