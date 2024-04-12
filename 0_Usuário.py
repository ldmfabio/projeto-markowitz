import streamlit as st
from streamlit_authenticator.authenticate.authentication import AuthenticationHandler
import yaml
from yaml.loader import SafeLoader

def main():
    st.set_page_config(
        page_title="Home", 
        page_icon="📉", 
        layout="centered", 
        initial_sidebar_state="expanded", 
    )  

    # Carregar as credenciais do arquivo YAML
    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Instanciar o AuthenticationHandler com as credenciais
    auth_handler = AuthenticationHandler(credentials=config['credentials'])

    if st.session_state.get('authentication_status') == None and st.session_state.get('authentication_status') != True:
        # Se o usuário não estiver autenticado, exibir o formulário de login
        username = st.text_input('Nome de usuário')
        password = st.text_input("Senha:", type="password")

        if st.button('Entrar no Sistema'):
            if auth_handler.check_credentials(username, password):
                # Se as credenciais estiverem corretas, fazer o login
                st.write("Login realizado com sucesso!")
                st.write("Carregando...")
                auth_handler.execute_login(username)
                st.switch_page("pages/2_Ferramenta.py")
            else:
                # Se as credenciais estiverem incorretas, exibir uma mensagem de erro
                st.write("Credenciais inválidas. Tente novamente.")

    if st.session_state.get('authentication_status', True):
        username = st.session_state['username']

        # Display user's current name and email
        st.title(f"Perfil")
        st.caption('## Informações de usuário')
        new_username = st.text_input("Nome de Usuário:", username, disabled=True)
        new_name = st.text_input("Nome Completo:", auth_handler.credentials['usernames'][username]['name'])
        new_email = st.text_input("Email:", auth_handler.credentials['usernames'][username]['email'])

        # Update user details if the user clicks the "Update" button
        if st.button("Alterar Informações", use_container_width=True):
            try:
                # Validate and update user details
                auth_handler.update_user_details(new_name, username, "name")
                auth_handler.update_user_details(new_email, username, "email")

                # Update name and email in session state
                st.session_state['name'] = auth_handler.credentials['usernames'][username]['name']
                st.session_state['email'] = auth_handler.credentials['usernames'][username]['email']

                # Display success message
                st.success("Perfil salvo com sucesso!")
                with open('./config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
            except Exception as e:
                # Handle validation or update errors
                st.error(f"{e}")

        
        # Create input field for new password
        st.caption('## Alterar Senha')
        old_password = st.text_input("Digite sua senha atual:", type="password", placeholder="Senha Atual")
        new_password = st.text_input("Digite sua nova senha:", type="password", placeholder="Nova Senha")
        new_confirm_password = st.text_input("Confirme sua nova senha:", type="password", placeholder="Confirmar Nova Senha")

        # Update password if the user clicks the "Change Password" button
        if st.button("Alterar Senha", use_container_width=True):
            try:
                # Validate and update password
                auth_handler.update_user_password(new_password, username)

                # Display success message
                st.success("Senha atualizada com sucesso!")
            except Exception as e:
                # Handle validation or update errors
                st.error(f"{e}")


if __name__ == "__main__":
    main()
