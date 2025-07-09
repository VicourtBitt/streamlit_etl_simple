import streamlit as st
from components.router import homepage, dataframe_page, students_page, workers_page, treatment_page

st.set_page_config(
    page_title="Home | VBittDashboard",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.sidebar.header("Menu de Navegação")
st.sidebar.markdown("Selecione uma página para navegar")

st.logo(image="assets/logo_dark.png", size="large")

navigation = st.navigation({
    "Home": [homepage],
    "Dados": [dataframe_page],
    "Visualização": [students_page, workers_page],
    "Tratamento de Dados": [treatment_page],
})

navigation.run()