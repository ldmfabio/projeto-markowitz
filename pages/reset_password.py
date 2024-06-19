import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_authenticator.authenticate.authentication import AuthenticationHandler

def main():
    username = st.session_state['username']
    
    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    
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

    password = st.text_input("Senha Atual:", type="password")
    new_password = st.text_input("Nova Senha:", type="password")
    confirm_new_password = st.text_input("Confirme a Nova Senha:", type="password")
    if st.button("Alterar Senha", use_container_width=True, type='primary'):
        if new_password != confirm_new_password:
            st.error("As senhas não coincidem")
            return
        try:
            auth_handler.reset_password(username, password, new_password, new_password)
            with open('./config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
            st.success('Senha modificada com sucesso')
        except Exception as e:
            st.error(e)
            
    if st.button("Voltar para página de Peril", use_container_width=True, type='secondary'):
        st.switch_page("pages/user.py")

if __name__ == "__main__":
    main()
