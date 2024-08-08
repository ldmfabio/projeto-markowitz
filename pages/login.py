import streamlit as st
from utils import add_custom_css, loader

def login(username, password):
    loader('Carregando...')
    st.session_state['authentication_status'] = True
    st.switch_page("pages/user.py")

def main():
    st.set_page_config(
        page_title="Login", 
        page_icon="🙂", 
        layout="centered", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()

    st.title("Login")
    username = st.text_input(
        key="username",
        value="",
        label="username"
    )
    password = st.text_input(
        type="password",
        key="password",
        value="",
        label="password"
    )

    if st.button("Login", key="login", use_container_width=True, type="secondary", help="Clique para entrar no sistema"):
        if username != "" and password != "":
            st.error("Usuário ou senha inválidos")
            return
        try:
            login(username, password)
            st.success('Usuário logado')
        except Exception as e:
            st.error(e)

    st.caption("Opções:")
    # st.button("Esqueci minha senha", use_container_width=False, help="Clique para redefinir sua senha")
    if st.button("Registrar novo usuário", use_container_width=False, help="Clique para criar uma nova conta"):
        st.switch_page("pages/create_account.py")

if __name__ == "__main__":
    main()
