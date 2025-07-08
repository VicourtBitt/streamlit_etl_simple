import streamlit as st

homepage = st.Page(
    page="views/0_homepage.py",
    title="Home",
    icon="🏠",
    default=True
)

dataframe_page = st.Page(
    page="views/1_dataframe.py",
    title="DataFrame Original",
    icon="📊",
)

improved_page = st.Page(
    page="views/2_improved_dataframe.py",
    title="DataFrame Melhorado",
    icon="🔧",
)