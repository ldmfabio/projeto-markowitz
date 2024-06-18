import streamlit as st
from streamlit_authenticator.authenticate.authentication import AuthenticationHandler
import yaml
from yaml.loader import SafeLoader
from manager.user_manager import UserManager
import streamlit_authenticator as stauth

from utils import create_navbar

def main():
    user_manager = UserManager()
    user_manager.verify_user()
    st.set_page_config(
        page_title="Perfil", 
        page_icon="👾", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )

    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    auth_handler = AuthenticationHandler(credentials=config['credentials'])

    col1, col2, col3 = st.columns([1, .2, 5])

    with col1:
        create_navbar()
    with col3:
        name = st.session_state['name']
        username = st.session_state['username']
        email = st.session_state['email']
        st.title(f"Perfil")
        
        st.write("Nome de Usuário:")
        st.text_input("Nome de Usuário:", username, disabled=True, label_visibility='collapsed')

        st.write("Nome Completo:")
        row_name = st.columns([5, 1])
        new_name = row_name[0].text_input("Nome Completo:", name, label_visibility='collapsed')
        if row_name[1].button("Alterar Nome", use_container_width=True, help="Clique para alterar o nome", disabled=True):
            try:
                auth_handler.update_user_details(username, new_name)
                st.success("Nome alterado com sucesso!")
            except Exception as e:
                st.error(e)
        
        st.write("Email:")
        row_email = st.columns([5, 1])
        new_email = row_email[0].text_input("Email:", email, label_visibility='collapsed')
        if row_email[1].button("Alterar Email", use_container_width=True, help="Clique para alterar o email", disabled=True):
            try:
                auth_handler.update_user_details(username, new_email)
                st.success("Email alterado com sucesso!")
            except Exception as e:
                st.error(e)
                
        if st.button("Alterar Senha", use_container_width=True, help="Clique para alterar a senha"):
            st.switch_page("pages/reset_password.py")
        if st.button("Sair", use_container_width=True, type='primary', help="Clique para sair da sua conta"):
            authenticator.logout(location='unrendered')
                
if __name__ == "__main__":
    main()
