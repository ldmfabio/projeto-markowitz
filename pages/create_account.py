import streamlit as st
import requests
from utils import add_custom_css, loader

def create_user(name, email, password, confirm_password):
    loader('Carregando...')
    try:
        if password != confirm_password:
            st.error("❗As senhas não correspondem")
            return

        response = requests.post(
            'http://127.0.0.1:8000/api/register/',
            json={
                'name': name,
                'email': email,
                'password': password
            }
        )
        response.raise_for_status()
        data = response.json()

        if response.status_code == 201:  # Supondo que 201 é o código para criação bem-sucedida
            st.success('Usuário criado com sucesso! Redirecionando para login...')
            st.switch_page("pages/login.py")
        else:
            st.error(f"❗Erro ao criar conta: {data.get('detail', 'Erro desconhecido')}")

    except requests.exceptions.RequestException as e:
        st.error(f"❗Erro na requisição: {str(e)}")

def main():
    st.set_page_config(
        page_title="Criar Conta", 
        page_icon="🙃",
        layout="centered", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()

    st.title("Criar Conta")
    name = st.text_input("Nome Completo:", placeholder="Mateus Lopes Albano")
    email = st.text_input("Email:", placeholder="mateusalbano22@gmail.com")
    password = st.text_input("Senha:", type="password", placeholder="*********")
    confirm_password = st.text_input("Confirmar Senha:", type="password", placeholder="*********")

    if st.button("Criar Conta", use_container_width=True, type='primary', help="Clique para criar uma nova conta"):
        if name == '' or email == '' or password == '' or confirm_password == '':
            st.error("🚨 Não podem haver campos vazios")
        else:
            create_user(name, email, password, confirm_password)

    if st.button("Já tenho uma conta!", use_container_width=True, help="Clique para fazer login"):
        st.switch_page("pages/login.py")

    st.markdown("""
        <div style="text-align:center;margin-top: 1em;font-size: 1.4em; font-weight: 900;">
            ModernMKZ
        </div>         
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
