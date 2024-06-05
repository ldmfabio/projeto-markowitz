import streamlit as st
import pandas as pd
from manager.user_manager import UserManager
from manager.app_manager import AppManager
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
        st.divider()
        st.page_link("app.py", use_container_width=True, label="Ferramenta", icon="📈")
        st.page_link("pages/about.py", use_container_width=True, label="Sobre o Projeto", icon="📄")
        st.page_link("pages/portfolio.py", use_container_width=True, label="Carteiras", icon="💼")
        st.page_link("pages/user.py", use_container_width=True, label="Perfil", icon="👾")
        st.divider()
        if st.button("Adicionar Carteira", key="add_portfolio", type="primary", use_container_width=True):
            st.switch_page("pages/add_portfolio.py")
    with col3:
        st.title("Suas Carteiras")

        if st.session_state.portfolios == []:
            st.caption("## Você ainda não possui nenhuma carteira cadastrada.")
        else:
            app_manager.display_portfolios(st.session_state.portfolios)
                            

if __name__ == "__main__":
    main()
