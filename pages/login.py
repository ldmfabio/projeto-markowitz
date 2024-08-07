import streamlit as st
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader
from utils import add_custom_css

def main():
    st.set_page_config(
        page_title="Login", 
        page_icon="🙂", 
        layout="centered", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()

    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    st.title("Login")
    fields = {
        'Form name':'Login', 
        'Username':'Username', 
        'Email':'Email',
        'Password':'Password',
        'Login':'Login'
    }
    name, authentication_status, username = authenticator.login(fields=fields)

    if authentication_status:
        st.session_state['authentication_status'] = True
        st.session_state['username'] = username
        st.session_state['name'] = config['credentials']['usernames'][username]['name']
        st.session_state['email'] = config['credentials']['usernames'][username]['email']
        st.success("Login realizado com sucesso!")
        st.switch_page("pages/user.py")
    elif authentication_status == False:
        st.error("Usuário ou senha inválidos")
    elif authentication_status == None:
        st.warning('Por favor, insira seu nome de usuário e senha')

    st.caption("Opções:")
    st.button("Esqueci minha senha", use_container_width=False, help="Clique para redefinir sua senha")
    if st.button("Registrar novo usuário", use_container_width=False, help="Clique para criar uma nova conta"):
        st.switch_page("pages/create_account.py")

if __name__ == "__main__":
    main()
