import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from utils import *
def main():
    add_custom_css()
    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    name, authentication_status, username = authenticator.login()

    if authentication_status:
        st.write(f'Bem-vindo *{name}*')

        try:
            if authenticator.reset_password(username):
                with open('./config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
                st.success('Senha modificada com sucesso')
        except Exception as e:
            st.error(e)

        try:
            email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
            if email_of_registered_user:
                with open('./config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
                st.success('Usuário registrado com sucesso')
        except Exception as e:
            st.error(e)

        try:
            username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
            if username_of_forgotten_password:
                st.success('Nova senha será enviada de forma segura')
                # O desenvolvedor deve transferir a nova senha de forma segura para o usuário.
            elif username_of_forgotten_password is False:
                st.error('Nome de usuário não encontrado')
        except Exception as e:
            st.error(e)

        try:
            username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
            if username_of_forgotten_username:
                st.success('Nome de usuário será enviado de forma segura')
                # O desenvolvedor deve transferir o nome de usuário de forma segura para o usuário.
            elif username_of_forgotten_username is False:
                st.error('Email não encontrado')
        except Exception as e:
            st.error(e)

        try:
            if authenticator.update_user_details(username):
                with open('./config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
                st.success('Dados atualizados com sucesso')
        except Exception as e:
            st.error(e)

        authenticator.logout()

    elif authentication_status is False:
        st.error('Nome de usuário/senha incorretos')
    elif authentication_status is None:
        st.warning('Por favor, insira seu nome de usuário e senha')

if __name__ == "__main__":
    main()



# import streamlit as st
# from streamlit_authenticator.authenticate.authentication import AuthenticationHandler
# import yaml
# from yaml.loader import SafeLoader
#   # Assuming you're using UserManager

# def main():
#     

#     st.set_page_config(
#         page_title="Perfil",
#         page_icon="",
#         layout="wide",
#         initial_sidebar_state="collapsed"
#     )

#     # Verificar se o usuário está logado
#     has_user = st.session_state.get('authentication_status') != None or st.session_state.get('authentication_status') == True

#     if has_user:
#         username = st.session_state.get('username')
#         if username is not None:
#             user_data = user_manager.get_user_data(username)  # Assuming this method exists

#             # Exibir informações do usuário
#             st.title(f"Perfil - {user_data['name']}")
#             st.caption('## Dados do Usuário')
#             st.write(f"Nome Completo: {user_data['name']}")
#             st.write(f"Email: {user_data['email']}")

#             # Atualizar informações do usuário (opcional)
#             st.caption('## Atualizar Informações')
#             new_name = st.text_input("Nome Completo:", user_data['name'], disabled=True, label_visibility="collapsed")
#             new_email = st.text_input("Email:", user_data['email'], label_visibility="collapsed")

#             if st.button("Atualizar"):
#                 try:
#                     user_manager.update_user_data(username, new_name, new_email)  # Assuming this method exists
#                     st.success("Informações atualizadas com sucesso!")
#                 except Exception as e:
#                     st.error(f"Erro ao atualizar informações: {e}")

#             # Alterar senha do usuário (opcional)
#             st.caption('## Alterar Senha')
#             old_password = st.text_input("Digite sua senha atual:", type="password", placeholder="Senha Atual")
#             new_password = st.text_input("Digite sua nova senha:", type="password", placeholder="Nova Senha")
#             new_confirm_password = st.text_input("Confirme sua nova senha:", type="password", placeholder="Confirmar Nova Senha")

#             if st.button("Alterar Senha"):
#                 try:
#                     auth_handler.update_user_password(username, old_password, new_password, new_confirm_password)
#                     st.success("Senha atualizada com sucesso!")
#                 except Exception as e:
#                     st.error(f"Erro ao atualizar senha: {e}")

#             # Logout do usuário
#             if st.button("Logout"):
#                 st.experimental_set_query_params()
            
#         else:
#             st.error("Usuário não encontrado")
#     else:
#         st.error("Usuário não autenticado")

# if __name__ == "__main__":
#     main()