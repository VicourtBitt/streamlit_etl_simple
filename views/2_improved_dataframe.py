import streamlit as st
from utils.data_utils import (
    get_student_dataframe, get_metric_correlation_quadrant, display_dataframe, get_student_metrics_dataframe
)
from plotly.express import pie, bar, density_heatmap
from plotly.graph_objects import Figure

def main():
    st.set_page_config(
        page_title="Engenharia de Dados | VBittDashboard",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("Engenharia de Dados com Streamlit")
    st.markdown("""
        Abaixo seguem duas tabelas, das quais explicaremos o motivo de estarem separadas e quais foram os critérios utilizados para essa separação.
    """)

    st.divider()
    st.subheader("Tabela de Dados de Estudantes")
    st.markdown("""
        Ao avaliarmos estudantes, desconsideraremos as informações métricas relacionadas a profissionais somente nos casos de os profissionais não possuírem horas de estudo.
    """)
    df = get_student_dataframe()
    if df is not None and not df.empty:
        display_dataframe(df)
    else:
        st.warning("No data available to display.")

    st.divider()
    st.subheader("Tabela de Métricas de Estudantes")
    st.markdown("""
        A tabela abaixo contém métricas de estudantes, como CGPA, hábitos alimentares e horas de sono.
        Essas métricas são importantes para entender o bem-estar dos estudantes e como isso pode afetar sua saúde mental.
        As métricas foram separadas da tabela principal para facilitar a análise e visualização dos dados.
    """)

    cgpa, dietary_habits, sleep_hours = get_student_metrics_dataframe(df)
    with st.container():
        cols = st.columns(3, gap="small")
        with cols[0]:
            with st.container(border=True):
                st.subheader("Distribuição de CGPA")
                st.plotly_chart(bar(cgpa, x='CGPA Range', y='Count', title='Distribuição de CGPA'), use_container_width=True)

        with cols[1]:
            with st.container(border=True):
                st.subheader("Distribuição de Hábitos Alimentares")
                st.plotly_chart(pie(dietary_habits, names='Dietary Habits', values='Count', title='Distribuição de Hábitos Alimentares'), use_container_width=True)

        with cols[2]:
            with st.container(border=True):
                st.subheader("Distribuição de Horas de Sono")
                st.plotly_chart(pie(sleep_hours, names='Sleep Duration', values='Count', title='Distribuição de Horas de Sono'), use_container_width=True)

    st.divider()
    st.subheader("Quadrante de Correlação de Métricas")
    st.markdown("""
        Abaixo está o quadrante de correlação das métricas dos estudantes, que mostra a relação entre CGPA, satisfação com os estudos, horas de sono, hábitos alimentares e depressão
        Essa análise é importante para entender como esses fatores estão interligados e como podem afetar a saúde mental dos estudantes.
    """)
    quadrant = get_metric_correlation_quadrant(get_student_dataframe())
    if quadrant is not None and not quadrant.empty:
        st.dataframe(quadrant, use_container_width=True)
    else:
        st.warning("No data available to display.")

main()