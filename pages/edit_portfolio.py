import streamlit as st
import pandas as pd
from manager.user_manager import UserManager
import time

def loader(text):
    text = text + '...'
    with st.spinner(text):
        time.sleep(1)
    # fazer um toast no futuro

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
        st.title(f"Editar Carteira: {st.session_state.portfolios_edit['name']}")
        cols1 = st.columns([4,1])
        name_portfolio = cols1[0].text_input(
            key=f"portfolio_{st.session_state.portfolios.index(st.session_state.portfolios_edit)}",
            value=st.session_state.portfolios_edit['name'],
            label="Nome da Carteira",
        )
        number = cols1[1].number_input('Digite o número de', step=1, max_value=5,  min_value=1, value=len(st.session_state.portfolios_edit['stocks']))

        stocks = []
        for j in range(number):
            value = st.session_state.portfolios_edit['stocks'][j] if j < len(st.session_state.portfolios_edit['stocks']) else ""
            stock = st.text_input(
                key=f"stock_{j}",
                value=value,
                label=f"Nome da Ação {j+1}",
            )
            stocks.append(stock)

        def validar_form():
            if name_portfolio == "":
                return False
            for stock in stocks:
                if stock == "":
                    return False
            return True

        
        cols2 = st.columns([1,2])

        if cols2[1].button("Salvar Alterações", key="save", use_container_width=True, type="primary"):
            loader('Salvando Alterações')
            if validar_form():
                st.session_state.portfolios[st.session_state.portfolios.index(st.session_state.portfolios_edit)] = {
                    "name": name_portfolio,
                    "stocks": stocks
                }
                st.switch_page("pages/portfolio.py")
            else:
                st.warning("Preencha todos os campos", icon="⚠️")

        if cols2[0].button("Excluir Carteira", key="delete", use_container_width=True, type="secondary"):
            loader('Excluindo Carteira')
            st.session_state.portfolios.remove(st.session_state.portfolios_edit)
            st.switch_page("pages/portfolio.py")

if __name__ == "__main__":
    main()
