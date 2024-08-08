import streamlit as st
from manager.app_manager import AppManager
from utils import *

# setitoff
def update_user(user):
    loader("Carregar...")

def logout():
    loader("Carregando...")
    for key in ['username', 'name', 'email']:
        if key in st.session_state:
            st.session_state[key] = None
    
def main():
    st.set_page_config(
        page_title="Perfil", 
        page_icon="👾", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()
    app_manager = AppManager()

    col1, col2, col3 = st.columns([1, .2, 5])
    with col1:
        create_navbar()
    with col3:
        name = st.session_state['name']
        username = st.session_state['username']
        email = st.session_state['email']
        st.write("")
        st.write("## Perfil do Usuário")

        st.write("Nome de Usuário:")
        st.text_input("Nome de Usuário:", username, disabled=True, label_visibility='collapsed')

        st.write("Nome Completo:")
        row_name = st.columns([5, 1])
        new_name = row_name[0].text_input("Nome Completo:", name, label_visibility='collapsed')
        if row_name[1].button("Alterar Nome", use_container_width=True, help="Clique para alterar o nome", disabled=False):
            try:
                update_user({ 
                    "username": username,
                    "name": new_name,
                    "email": email
                })
                st.success("Nome alterado com sucesso!")
                name = new_name
            except Exception as e:
                st.error(e)

        st.write("Email:")
        row_email = st.columns([5, 1])
        new_email = row_email[0].text_input("Email:", email, label_visibility='collapsed')
        if row_email[1].button("Alterar Email", use_container_width=True, help="Clique para alterar o email", disabled=False):
            try:
                update_user({ 
                    "username": username,
                    "name": name,
                    "email": new_email
                })
                st.success("Email alterado com sucesso!")
                email = new_email
            except Exception as e:
                st.error(e)

        if st.button("Sair", use_container_width=True, type='primary', help="Clique para sair da sua conta"):
            logout()
            st.switch_page("pages/login.py")

if __name__ == "__main__":
    main()