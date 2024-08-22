import streamlit as st
import requests
from manager.app_manager import AppManager
from utils import add_custom_css, loader, create_navbar

def update_user(user):
    loader("Carregando...")
    try:
        response = requests.put(
            f'http://127.0.0.1:8000/api/users/{user["id"]}/',
            json=user
        )
        response.raise_for_status()
        st.success("Informações do usuário atualizadas com sucesso!")
        return response.json()

    except requests.exceptions.RequestException as e:
        st.error(f"❗Aconteceu algum problema, tente novamente mais tarde")
        return None
    
def get_user():
    try:
        response = requests.get(
            f'http://127.0.0.1:8000/api/users/{st.session_state["user_id"]}/'
        )
        response.raise_for_status()
        data = response.json()
        st.session_state['name'] = data['name']
        st.session_state['email'] = data['email']

    except requests.exceptions.RequestException as e:
        st.error(f"❗Erro na requisição: {str(e)}")
        return None

def logout():
    loader("Carregando...")
    for key in ['name', 'email']:
        if key in st.session_state:
            st.session_state[key] = None

def main():
    st.set_page_config(
        page_title="Perfil", 
        page_icon="👾", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()
    app_manager = AppManager()
    get_user()

    col1, col2, col3 = st.columns([1, .2, 5])
    with col1:
        create_navbar()
    with col3:
        id = st.session_state.get('user_id', '')
        name = st.session_state.get('name', '')
        email = st.session_state.get('email', '')

        st.write("")
        st.write("## Perfil do Usuário")

        st.write("Email:")
        st.text_input("Email:", email, label_visibility='collapsed', disabled=True)

        st.write("Nome Completo:")
        row_name = st.columns([5, 1])
        new_name = row_name[0].text_input("Nome Completo:", name, label_visibility='collapsed')
        if row_name[1].button("Alterar Nome", use_container_width=True, help="Clique para alterar o nome"):
            try:
                updated_user = update_user({ 
                    "id": id,
                    "name": new_name,
                })
                if updated_user:
                    st.session_state['name'] = new_name
                    st.success("Nome alterado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao atualizar o nome: {e}")

        if st.button("Sair", use_container_width=True, type='primary', help="Clique para sair da sua conta"):
            logout()
            st.switch_page("pages/login.py")

if __name__ == "__main__":
    main()
