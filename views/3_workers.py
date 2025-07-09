import streamlit as st
from utils.data_utils import (
    get_worker_dataframe, get_metric_correlation_quadrant, display_dataframe, get_worker_metrics_dataframe
)
from plotly.express import pie, bar
from plotly.graph_objects import Figure
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.set_page_config(
        page_title="Profissionais | VBittDashboard",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Visualização dos Profissionais com Streamlit")
    st.divider()
    st.subheader("Tabela de Dados de Profissionais")
    st.markdown("""
        Ao avaliarmos profissionais, desconsideraremos as informações métricas relacionadas a estudantes somente nos casos de os estudantes não possuírem horas de estudo.
    """)
    df = get_worker_dataframe()
    if df is not None and not df.empty:
        display_dataframe(df)
    else:
        st.warning("No data available to display.")

    st.divider()
    st.subheader("Tabela de Métricas de Profissionais")
    st.markdown("""
        A tabela abaixo contém métricas de profissionais, como horas de estudo, satisfação com o trabalho e horas de sono.
        Essas métricas são importantes para entender o bem-estar dos profissionais e como isso pode afetar sua saúde mental.
        As métricas foram separadas da tabela principal para facilitar a análise e visualização dos dados.
    """)

    work_pressure, job_satisfaction, financial_stress = get_worker_metrics_dataframe(df)    
    with st.container():
        cols = st.columns(3, gap="small")
        with cols[0]:
            with st.container(border=True):
                st.subheader("Distribuição de Pressão de Trabalho")
                st.plotly_chart(bar(work_pressure, x='Work Pressure', y='Count', title='Distribuição de Pressão de Trabalho'), use_container_width=True)

        with cols[1]:
            with st.container(border=True):
                st.subheader("Distribuição de Estresse Financeiro")
                st.plotly_chart(pie(financial_stress, names='Financial Stress', values='Count', title='Distribuição de Estresse Financeiro'), use_container_width=True)

        with cols[2]:
            with st.container(border=True):
                st.subheader("Distribuição de Satisfação no Trabalho")
                st.plotly_chart(pie(job_satisfaction, names='Job Satisfaction', values='Count', title='Distribuição de Satisfação no Trabalho'), use_container_width=True)  

    st.divider()
    st.subheader("Quadrante de Correlação de Métricas")
    

main()