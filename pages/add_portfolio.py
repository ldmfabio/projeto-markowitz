import streamlit as st
import pandas as pd
from manager.user_manager import UserManager

def main():
    user_manager = UserManager()
    user_manager.verify_user()
    st.set_page_config(
        page_title="Adicionar Carteira", 
        page_icon="➕", 
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
    with col3:
        st.title("Adicionar Carteira")
        cols_form_portflio = st.columns([4,1])

        with cols_form_portflio[0]:
            name_portfolio = st.text_input(
                "Nome da nova Carteira",
                placeholder="Digite aqui",
            )
        
        with cols_form_portflio[1]:
            number = st.number_input('Digite o número de ações', step=1, max_value=5,  min_value=1, value=1)

        stocks = [st.text_input(f"Nome da Ação {i+1}", placeholder="Digite aqui") for i in range(number)]

        # btn para enviar

        def validar_form():
            if name_portfolio == "":
                return False
            for stock in stocks:
                if stock == "":
                    return False
            return True

        if st.button("Adicionar Carteira", key="add_portfolio", help="Adiciona uma nova carteira"):
            if validar_form():
                st.session_state.portfolios.append({
                    "name": name_portfolio,
                    "stocks": stocks
                })
                st.switch_page("pages/portfolio.py")
            else:
                st.warning("Preencha todos os campos", icon="⚠️")

if __name__ == "__main__":
    main()
