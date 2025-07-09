import streamlit as st

homepage = st.Page(
    page="views/0_homepage.py",
    title="Home",
    icon="🏠",
    default=True
)

dataframe_page = st.Page(
    page="views/1_dataframe.py",
    title="Contexto dos Dados",
    icon="📊",
)

students_page = st.Page(
    page="views/2_students.py",
    title="Estudantes",
    icon="📈",
)

workers_page = st.Page(
    page="views/3_workers.py",
    title="Profissionais",
    icon="👨‍💻",
)

treatment_page = st.Page(
    page="views/4_treatment.py",
    title="Tratamento de Dados",
    icon="🛠️"
)