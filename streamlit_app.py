import streamlit as st
from components.router import homepage, dataframe_page, improved_page

st.set_page_config(
    page_title="Streamlit App",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Navegação entre Páginas com Streamlit")
st.markdown("""
    Este é um exemplo de como criar uma navegação entre páginas usando o Streamlit.
    Você pode navegar entre as páginas clicando nos links abaixo.
""")
st.logo(image="assets/logo_dark.png", size="large")

navigation = st.navigation({
    "Home": [homepage],
    "DataFrame": [dataframe_page],
    "Engenharia": [improved_page],
})

navigation.run()