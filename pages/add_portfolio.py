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
        st.title("Adicionar Carteira")
        cols_form_portflio = st.columns([4,1])

        with cols_form_portflio[0]:
            name_portfolio = st.text_input(
                "Nome da nova Carteira",
                placeholder="Digite aqui",
            )
        
        with cols_form_portflio[1]:
            number = st.number_input('Digite o número de', step=1, max_value=5,  min_value=1, value=1)

        stocks = [st.text_input(f"Nome da Ação {i+1}", placeholder="Digite aqui") for i in range(number)]

        # btn para enviar

        def validar_form():
            if name_portfolio == "":
                return False
            for stock in stocks:
                if stock == "":
                    return False
            return True

        if st.button("Adicionar Carteira"):
            if validar_form():
                st.session_state.portfolios.append({
                    "name": name_portfolio,
                    "stocks": stocks
                })
                st.success('Adicionado com sucesso', icon="✅")
            else:    
                st.warning("Preencha todos os campos", icon="⚠️")

if __name__ == "__main__":
    main()
