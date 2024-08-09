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
        label="Digite seu nome de usuário",
        placeholder="admin"
    )
    password = st.text_input(
        type="password",
        key="password",
        value="",
        label="Digite sua Senha",
        placeholder="**********"
    )

    if st.button("Login", key="login", use_container_width=True, type="primary", help="Clique para entrar no sistema"):
        if username == "" or password == "":
            st.error("🚨 Não podem haver campos vazios")
        else:
            try:
                login(username, password)
                st.success('Usuário logado')
            except Exception as e:
                st.error(e)

    if st.button("Ainda não tem uma conta?", use_container_width=True, help="Clique para criar uma nova conta"):
        st.switch_page("pages/create_account.py")

    st.markdown("""
        <div style="text-align:center;margin-top: 1em;font-size: 1.4em; font-weight: 900;">
            ModernMKZ
        </div>         
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
