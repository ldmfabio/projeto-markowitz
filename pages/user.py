import streamlit as st
from streamlit_authenticator.authenticate.authentication import AuthenticationHandler
import yaml
from yaml.loader import SafeLoader
from utils import init_session

def main():
    init_session()
    st.set_page_config(
        page_title="Perfil", 
        page_icon="👾", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )

    # Carregar as credenciais do arquivo YAML e instanciar o objeto de autenticação
    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    auth_handler = AuthenticationHandler(credentials=config['credentials'])

    # verificar usuário
    has_user = st.session_state.get('authentication_status') != None or st.session_state.get('authentication_status') == True

    col1, col2, col3 = st.columns([1, .2, 5])

    with col1:
        st.divider()
        st.page_link("app.py", label="Página Inicial", icon="🌎")
        st.page_link("pages/tool.py", label="Ferramenta", icon="📉")
        st.page_link("pages/portfolio.py", label="Carteiras", icon="💼")
        st.page_link("pages/user.py", label="Perfil", icon="👾")
        st.divider()
    with col3:
        # Usuário não autenticado
        if not has_user:
            st.caption('# Entrar no Sistema')
            login_username = st.text_input('Login', )
            login_password = st.text_input("Senha:", type="password")
            if st.button('Entrar no Sistema'):
                try:
                    auth_handler.check_credentials(login_username, login_password)
                    auth_handler.execute_login(login_username)
                    st.write("`Login realizado com sucesso!`")
                    st.caption("Carregando...")
                    st.session_state.authentication_status = True
                    st.switch_page("app.py")
                except Exception as e:
                    st.write(f"erro {e}")

            st.caption('# Criar novo usuário')
            create_username = st.text_input('Nome de Usuário ( Login )')
            create_name = st.text_input("Seu nome completo")
            create_email = st.text_input("Seu email")
            create_password = st.text_input("Sua senha:", type="password")
            create_confirm_password = st.text_input("Confirme sua senha:", type="password")
            if st.button('Criar nova Conta'):
                if create_password == create_confirm_password:
                    try:
                        auth_handler._register_credentials(create_username, create_name, create_password, create_email, False, [])
                        st.write("`Conta criada com sucesso!`")
                    except Exception as e:
                        st.write(f"Erro ao criar conta: {e}")
                else:
                    st.write("Senhas não coincidem. Tente novamente.")

        if has_user:
            username = st.session_state.get('username')
            if username is not None:
                st.title(f"Perfil")
                st.caption('## Informações de usuário')
                new_username = st.text_input("Nome de Usuário:", username, disabled=True)
                new_name = st.text_input("Nome Completo:", auth_handler.credentials['usernames'][username]['name'])
                new_email = st.text_input("Email:", auth_handler.credentials['usernames'][username]['email'])
                if st.button("Alterar Informações", use_container_width=True):
                    try:
                        if new_name != st.session_state['name']:
                            auth_handler.update_user_details(new_name, username, "name")
                            st.session_state['name'] = auth_handler.credentials['usernames'][username]['name']
                            st.success("Perfil salvo com sucesso! (Nome de Usuário Atualizado)")
                            
                        auth_handler.update_user_details(new_email, username, "email")
                        st.session_state['email'] = auth_handler.credentials['usernames'][username]['email']
                        with open('./config.yaml', 'w') as file:
                            yaml.dump(config, file, default_flow_style=False)
                    except Exception as e:
                        st.error(f"{e}")
                if st.button("Logout", use_container_width=True):
                    auth_handler.execute_logout()
                    st.session_state.authentication_status = False

                st.caption('## Alterar Senha')
                old_password = st.text_input("Digite sua senha atual:", type="password", placeholder="Senha Atual")
                new_password = st.text_input("Digite sua nova senha:", type="password", placeholder="Nova Senha")
                new_confirm_password = st.text_input("Confirme sua nova senha:", type="password", placeholder="Confirmar Nova Senha")

                if st.button("Alterar Senha", use_container_width=True):
                    try:
                        auth_handler.update_user_password(new_password, username)
                        st.success("Senha atualizada com sucesso!")
                    except Exception as e:
                        st.error(f"{e}")

            else:
                st.error("Nome de usuário não encontrado.")

if __name__ == "__main__":
    main()
