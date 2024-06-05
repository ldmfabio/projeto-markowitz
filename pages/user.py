import streamlit as st
from streamlit_authenticator.authenticate.authentication import AuthenticationHandler
import yaml
from yaml.loader import SafeLoader
from manager.user_manager import UserManager

def main():
    user_manager = UserManager()
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
        st.page_link("app.py", use_container_width=True, label="Ferramenta", icon="📈")
        st.page_link("pages/about.py", use_container_width=True, label="Sobre o Projeto", icon="📄")
        st.page_link("pages/portfolio.py", use_container_width=True, label="Carteiras", icon="💼")
        st.page_link("pages/user.py", use_container_width=True, label="Perfil", icon="👾")
        st.divider()
    with col3:
        # Usuário não autenticado
        if not has_user:
            st.title('Entrar no Sistema')
            login_username = st.text_input('Login', )
            login_password = st.text_input("Senha:", type="password")
            if st.button('Entrar no Sistema', type="primary"):
                try:
                    auth_handler.check_credentials(login_username, login_password)
                    auth_handler.execute_login(login_username)
                    st.write("`Login realizado com sucesso!`")
                    st.caption("Carregando...")
                    st.session_state.authentication_status = True
                    st.switch_page("app.py")
                except Exception as e:
                    st.write(f"erro {e}")

            st.title('Criar novo usuário')
            create_username = st.text_input('Nome de Usuário ( Login )')
            create_name = st.text_input("Seu nome completo")
            create_email = st.text_input("Seu email")
            create_password = st.text_input("Sua senha:", type="password")
            create_confirm_password = st.text_input("Confirme sua senha:", type="password")
            if st.button('Criar nova Conta', type="primary"):
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
                new_username = st.text_input("Nome de Usuário:", username, disabled=True, label_visibility="collapsed" )
                cols1 = st.columns([5, 1])
                new_name = cols1[0].text_input("Nome Completo:", auth_handler.credentials['usernames'][username]['name'], label_visibility="collapsed" )
                if cols1[1].button("Alterar Nome", use_container_width=True):
                    try:
                        auth_handler.update_user_details(new_name, username, "name")
                        st.session_state['name'] = auth_handler.credentials['usernames'][username]['name']
                        st.success("Informações atualizadas com sucesso!")
                        with open('./config.yaml', 'w') as file:
                            yaml.dump(config, file, default_flow_style=False)
                    except Exception as e:
                        st.error(f"{e}")
                cols2 = st.columns([5, 1])
                new_email = cols2[0].text_input("Email:", auth_handler.credentials['usernames'][username]['email'], label_visibility="collapsed" )
                if cols2[1].button("Alterar Email", use_container_width=True):
                    try:
                        auth_handler.update_user_details(new_email, username, "email")
                        st.session_state['email'] = auth_handler.credentials['usernames'][username]['email']
                        st.success("Informações atualizadas com sucesso!")
                        with open('./config.yaml', 'w') as file:
                            yaml.dump(config, file, default_flow_style=False)
                    except Exception as e:
                        st.error(f"{e}")
                        
                if st.button("Sair", use_container_width=True, type="primary"):
                    st.session_state.authentication_status = False
                    auth_handler.execute_logout()

                st.caption('## Alterar Senha')
                old_password = st.text_input("Digite sua senha atual:", type="password", placeholder="Senha Atual")
                new_password = st.text_input("Digite sua nova senha:", type="password", placeholder="Nova Senha")
                new_confirm_password = st.text_input("Confirme sua nova senha:", type="password", placeholder="Confirmar Nova Senha")

                if st.button("Alterar Senha", use_container_width=True, type="primary"):
                    try:
                        auth_handler.update_user_password(new_password, username)
                        st.success("Senha atualizada com sucesso!")
                    except Exception as e:
                        st.error(f"{e}")

            else:
                st.error("Erro ao encotrar usuário, por favor reinicie a página.")


if __name__ == "__main__":
    main()
