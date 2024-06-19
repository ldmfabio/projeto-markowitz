import streamlit as st

def create_navbar(type=None):
    st.divider()
    st.write("__Menu de Navegação__")
    st.page_link("app.py", use_container_width=True, label="Ferramenta", icon="📈")
    st.page_link("pages/about.py", use_container_width=True, label="Sobre o Projeto", icon="📄")
    st.page_link("pages/portfolio.py", use_container_width=True, label="Carteiras", icon="💼")
    st.page_link("pages/user.py", use_container_width=True, label="Perfil", icon="👾")
    st.divider()
    if not type:
        st.write("__Créditos__")
        st.image('./assets/img/group3.png', use_column_width=True)
