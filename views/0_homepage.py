import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def main():
    st.title("Streamlit Main Example")

    with stylable_container(
        css_styles="""{
            "backgroundColor": "#f0f0f0",
            "padding": "20px",
            "borderRadius": "10px",
            "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.1)"
        }""",
        key="custom_container"
    ):
        st.write("This is a custom styled container.")
        st.button("Click Me")
    
main()          