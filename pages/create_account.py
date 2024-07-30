import streamlit as st
from streamlit_authenticator.authenticate.authentication import AuthenticationHandler
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from utils import *

def main():
    st.set_page_config(
        page_title="Criar Conta", 
        page_icon="🙃",
        layout="centered", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()

    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    auth_handler = AuthenticationHandler(credentials=config['credentials'])

    st.title("Criar Conta")
    username = st.text_input("Usuário:")
    name = st.text_input("Nome Completo:")
    email = st.text_input("Email:")
    password = st.text_input("Senha:", type="password")
    confirm_password = st.text_input("Confirmar Senha:", type="password")

    if st.button("Criar Conta", use_container_width=True, type='primary', help="Clique para criar uma nova conta"):
        if auth_handler.register_user(new_password=password, new_password_repeat=confirm_password, pre_authorization=False, new_username=username, new_name=name, new_email=email):
            with open('./config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
            st.success("Conta criada com sucesso!")
        else:
            st.error("Erro ao criar conta")
    elif st.session_state['authentication_status'] is False:
        st.error('Erro ao criar conta')
    elif st.session_state['authentication_status'] is None:
        st.warning('Por favor, preencha os campos')
    
    st.caption("Opções:")
    st.button("Já tenho uma conta", use_container_width=False, help="Clique para fazer login")

if __name__ == "__main__":
    main()
