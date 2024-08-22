import streamlit as st
import requests
from utils import add_custom_css, loader

def login(email, password):
    loader('Carregando...')
    try:
        response = requests.post(
            'http://127.0.0.1:8000/api/login/',
            json={'email': email, 'password': password}
        )
        response.raise_for_status()
        data = response.json()
        if data['access']:
            st.session_state['authentication_status'] = True
            st.session_state['user_id'] = data['id']
            st.success('Usuário logado')
            st.switch_page("pages/user.py")
        else:
            st.error('❗Falha na autenticação')
    except requests.exceptions.RequestException as e:
        st.error('❗Falha na autenticação')

def main():
    st.set_page_config(
        page_title="Login", 
        page_icon="🙂", 
        layout="centered", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()
    st.title("Login")

    email = st.text_input(
        key="email",
        value="",
        label="Digite seu Email",
        placeholder="Ex: admin@admin.com"
    )
    password = st.text_input(
        type="password",
        key="password",
        value="",
        label="Digite sua Senha",
        placeholder="**********"
    )

    if st.button("Login", key="login", use_container_width=True, type="primary", help="Clique para entrar no sistema"):
        if email == "" or password == "":
            st.error("🚨 Não podem haver campos vazios")
        else:
            login(email, password)

    if st.button("Ainda não tem uma conta?", use_container_width=True, help="Clique para criar uma nova conta"):
        st.switch_page("pages/create_account.py")

    st.markdown("""
        <div style="text-align:center;margin-top: 1em;font-size: 1.4em; font-weight: 900;">
            ModernMKZ
        </div>         
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
