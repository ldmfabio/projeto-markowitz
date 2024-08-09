import streamlit as st
from utils import add_custom_css, loader

def create_user(username, name, email, password, confirm_password):
    loader('Carregando...')
    st.switch_page("pages/login.py")

def main():
    st.set_page_config(
        page_title="Criar Conta", 
        page_icon="🙃",
        layout="centered", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()

    st.title("Criar Conta")
    username = st.text_input("Usuário:", placeholder="mateus-lopes")
    name = st.text_input("Nome Completo:", placeholder="Mateus Lopes Albano")
    email = st.text_input("Email:", placeholder="mateusalbano22@gmail.com")
    password = st.text_input("Senha:", type="password", placeholder="*********")
    confirm_password = st.text_input("Confirmar Senha:", type="password", placeholder="*********")

    if st.button("Criar Conta", use_container_width=True, type='primary', help="Clique para criar uma nova conta"):
        if username == '' or name == '' or email == '' or password == '' or confirm_password == '':
            st.error("🚨 Não podem haver campos vazios")
        else:
            try:
                create_user(username, password)
                st.success('Usuário logado')
            except Exception as e:
                # st.error(e)
                st.write('Erro ao criar conta')

    if st.button("Já tenho uma conta!", use_container_width=True, help="Clique para fazer login"):
        st.switch_page("pages/login.py")

    st.markdown("""
        <div style="text-align:center;margin-top: 1em;font-size: 1.4em; font-weight: 900;">
            ModernMKZ
        </div>         
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
