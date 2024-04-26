import streamlit as st
import pandas as pd
from utils import init_session, verify_user, display_portfolios


def main(): 
    init_session()
    verify_user()
    st.set_page_config(
        page_title="Carteiras", 
        page_icon="💼", 
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
        st.page_link("pages/add_portfolio.py", label="Adicionar Carteira", icon="➕")
    with col3:
        st.title("Suas Carteiras")
        st.caption("""<p style='font-size: 1.4em; max-width: 900px; padding: 0 0 1em 0'>
            Você pode se perguntar por que um designer optaria por usar o texto lorem ipsum em vez de alguns parágrafos em seu idioma nativo.
        </p>""", unsafe_allow_html=True)

        display_portfolios(st.session_state.portfolios, st.session_state)
                            

if __name__ == "__main__":
    main()
