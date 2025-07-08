import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def main():
    st.title("Página Inicial")
    st.markdown("""
        Bem-vindo ao meu aplicativo simples do Streamlit, aqui irei exibir algumas
        interações simples entre várias tecnologias como Pandas, Typing, Streamlit e outros!
        Iremos aproveitar e mexer um pouco com tratamento e análise de dados também!
    """)

    st.divider()

    st.subheader("Sobre o Projeto")
    st.markdown("""
        Este projeto é um exemplo simples de como usar o Streamlit para criar uma aplicação
        web interativa. Ele demonstra como carregar e exibir dados usando o Pandas, além
        de como estilizar componentes com o Streamlit Extras.
    """)

    st.subheader("Tecnologias Utilizadas")
    st.markdown("""
        - **Streamlit**: Para criar a interface web interativa.
        - **Pandas**: Para manipulação e análise de dados.
        - **Streamlit Extras**: Para componentes adicionais e estilização.
    """)

    st.divider()
    st.subheader("Redes Sociais")
    st.markdown("""
        Você pode me encontrar nas seguintes redes sociais:
        - [GitHub](https://github.com/VicourtBitt)
        - [LinkedIn](https://www.linkedin.com/in/victorbitt/)
    """)
    
main()          