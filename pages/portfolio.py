import streamlit as st
import requests
from manager.app_manager import AppManager
from utils import add_custom_css, create_navbar, loader

def fetch_portfolios():
    try:
        response = requests.get(f'http://127.0.0.1:8000/api/portfolios/?user={st.session_state["user_id"]}')
        response.raise_for_status()
        portfolios = response.json()
        st.session_state['portfolios'] = portfolios
        return portfolios
    except requests.exceptions.RequestException as e:
        st.error(f"❗Erro ao buscar carteiras: {str(e)}")
        return []

def main(): 
    app_manager = AppManager()
    st.set_page_config(
        page_title="Carteiras", 
        page_icon="💼", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()
    fetch_portfolios()

    col1, col2, col3 = st.columns([1, .2, 5])
    with col1:
        create_navbar(type='portfolio')
        st.write("__Opções__")
        filter_options = ["Data de Criação", "Alfabético", "Número de Ações"]
        st.session_state.selected_option = st.selectbox("Filtrar por:", filter_options, index=2)
        if st.button("Adicionar Carteira", key="add_portfolio", type="primary", use_container_width=True, help="Adiciona uma nova carteira"):
            st.switch_page("pages/add_portfolio.py")
        st.divider()
        st.write("")
        st.image('./assets/img/group3.png', use_column_width=True)

    with col3:
        st.write("")
        st.write("## Suas Carteiras")
        st.info("Aqui você pode visualizar e gerenciar suas carteiras de ações.")

        portfolios = st.session_state['portfolios']

        if not portfolios:
            st.caption("## Você ainda não possui nenhuma carteira cadastrada.")
        else:
            app_manager.display_portfolios()

if __name__ == "__main__":
    main()
