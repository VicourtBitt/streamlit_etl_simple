import streamlit as st

def main():
    st.set_page_config(
        page_title="Tratamento de Dados | VBittDashboard",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    st.title("Tratamento de Dados com Streamlit")
    st.markdown("""
        Nesta seção, apresentamos o tratamento de dados realizado para preparar as informações dos estudantes e profissionais.
        O tratamento inclui a limpeza, transformação e análise dos dados para garantir a qualidade e a integridade das informações.
    """)
    
    st.divider()
    st.subheader("Tratamento de Dados")
    st.markdown("""
        O tratamento de dados é uma etapa crucial no processo de análise, pois garante que os dados estejam prontos para serem utilizados em análises e visualizações.
        Nesta seção, apresentamos as etapas realizadas no tratamento dos dados dos estudantes e profissionais.
    """)
    
    st.write("Página ainda incompleta, volte logo mais...")  

main()