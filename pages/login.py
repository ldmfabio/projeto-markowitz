import streamlit as st
from streamlit_authenticator.authenticate.authentication import AuthenticationHandler
import yaml
from yaml.loader import SafeLoader

def main():
    st.set_page_config(
        page_title="Login", 
        page_icon="🙂", 
        layout="centered", 
        initial_sidebar_state="collapsed"
    )

    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    auth_handler = AuthenticationHandler(credentials=config['credentials'])

    st.title("Login")
    username = st.text_input("Usuário:")
    password = st.text_input("Senha:", type="password")

    if st.button("Login", use_container_width=True, type='primary', help="Clique para fazer login"):
        if auth_handler.check_credentials(username, password):
            st.session_state['authentication_status'] = True
            st.session_state['username'] = username
            st.session_state['name'] = auth_handler.credentials['usernames'][username]['name']
            st.session_state['email'] = auth_handler.credentials['usernames'][username]['email']
            st.success("Login realizado com sucesso!")
            st.switch_page("pages/user.py")
        else:
            st.error("Usuário ou senha inválidos")
    elif st.session_state['authentication_status'] is False:
        st.error('Nome de usuário/senha incorretos')
    elif st.session_state['authentication_status'] is None:
        st.warning('Por favor, insira seu nome de usuário e senha')

    st.caption("Opções:")
    st.button("Esqueci minha senha", use_container_width=False, help="Clique para redefinir sua senha")
    if st.button("Registrar novo usuário", use_container_width=False, help="Clique para criar uma nova conta"):
        st.switch_page("pages/create_account.py")

if __name__ == "__main__":
    main()
