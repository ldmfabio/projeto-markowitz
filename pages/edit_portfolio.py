import streamlit as st
import pandas as pd
from utils import init_session, verify_user

def main(): 
    init_session()
    verify_user()
    st.set_page_config(
        page_title="Adicionar Carteira", 
        page_icon="➕", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )

    col1, col2, col3 = st.columns([1, .2, 5])

    with col1:
        st.divider()
        st.page_link("app.py", label="Página Inicial", icon="🌎")
        st.page_link("pages/tool.py", label="Ferramenta", icon="📉")
        st.page_link("pages/portfolio.py", label="Carteiras", icon="💼")
        st.page_link("pages/user.py", label="Perfil", icon="👾")
        st.divider() 
    with col3:
        st.title(f"Editar Carteira: {st.session_state.portfolios_edit['name']}")
        name_portfolio = st.text_input(
            key=f"portfolio_{st.session_state.portfolios.index(st.session_state.portfolios_edit)}",
            value=st.session_state.portfolios_edit['name'],
            label="Nome da Carteira"
        )
        stocks = []
        for j in range(len(st.session_state.portfolios_edit['stocks'])):
            stock = st.text_input(
                key=f"stock_{j}",
                value=st.session_state.portfolios_edit['stocks'][j],
                label=f"Nome da Ação {j+1}"
            )
            stocks.append(stock)

        def validar_form():
            if name_portfolio == "":
                return False
            for stock in stocks:
                if stock == "":
                    return False
            return True

        if st.button("Salvar Alterações", key="save"):
            if validar_form():
                st.session_state.portfolios[st.session_state.portfolios.index(st.session_state.portfolios_edit)] = {
                    "name": name_portfolio,
                    "stocks": stocks
                }
                st.success('Adicionado com sucesso', icon="✅")
            else:
                st.warning("Preencha todos os campos", icon="⚠️")

        if st.button("Excluir Carteira", key="delete"):
            st.session_state.portfolios.remove(st.session_state.portfolios_edit)
            st.success('Excluído com sucesso', icon="✅")

if __name__ == "__main__":
    main()
