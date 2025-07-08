import streamlit as st
from components.router import homepage, dataframe_page, improved_page

st.set_page_config(
    page_title="Streamlit App",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.sidebar.header("Menu de Navegação")
st.sidebar.markdown("Selecione uma página para navegar")

st.logo(image="assets/logo_dark.png", size="large")

navigation = st.navigation({
    "Home": [homepage],
    "DataFrame": [dataframe_page],
    "Engenharia": [improved_page],
})

navigation.run()