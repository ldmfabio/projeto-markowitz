import streamlit as st
from manager.app_manager import AppManager
from utils import add_custom_css, loader

def reset_password():
    loader("Carregando...")

def main():
    app_manager = AppManager()
    add_custom_css()
    st.title("Alterar Senha")
    password = st.text_input("Senha Atual:", type="password")
    new_password = st.text_input("Nova Senha:", type="password")
    confirm_new_password = st.text_input("Confirme a Nova Senha:", type="password")
    
    if st.button("Alterar Senha", use_container_width=True, type='primary'):
        if new_password != confirm_new_password:
            st.error("As senhas não coincidem")
            return
        try:
            reset_password()
            st.success('Senha modificada com sucesso')
        except Exception as e:
            st.error(e)
            
    if st.button("Voltar para página de Peril", use_container_width=True, type='secondary'):
        st.switch_page("pages/user.py")

if __name__ == "__main__":
    main()
