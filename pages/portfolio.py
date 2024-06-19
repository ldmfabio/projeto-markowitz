import streamlit as st
import pandas as pd
from manager.user_manager import UserManager
from manager.app_manager import AppManager
from utils import create_navbar

def main(): 
    user_manager = UserManager()
    app_manager = AppManager()
    user_manager.verify_user()
    st.set_page_config(
        page_title="Carteiras", 
        page_icon="💼", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )

    col1, col2, col3 = st.columns([1, .2, 5])

    with col1:
        create_navbar(type='portfolio')
        st.write("__Opções__")
        filter_options = ["Data de Criação", "Alfabético", "Número de Ações"]
        selected_option = st.selectbox("Filtrar por:", filter_options)
        if st.button("Adicionar Carteira", key="add_portfolio", type="primary", use_container_width=True, help="Adiciona uma nova carteira"):
            st.switch_page("pages/add_portfolio.py")
        st.divider()
        st.write("")
        st.image('./assets/img/group3.png', use_column_width=True)
    with col3:
        st.title("Suas Carteiras")

        if st.session_state.portfolios == []:
            st.caption("## Você ainda não possui nenhuma carteira cadastrada.")
        else:
            app_manager.display_portfolios(st.session_state.portfolios, selected_option)
                            

if __name__ == "__main__":
    main()
