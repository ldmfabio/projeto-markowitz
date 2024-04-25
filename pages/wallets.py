import streamlit as st
import pandas as pd
from utils import init_session, verify_user

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
        st.page_link("pages/wallets.py", label="Carteiras", icon="💼")
        st.page_link("pages/user.py", label="Perfil", icon="👾")
        st.divider()
        if st.button('Adicionar Carteira', type="primary",use_container_width=True):
            st.session_state.showResult = True
    with col3:
        st.title("Suas Carteiras")
        st.caption("""<p style='font-size: 1.4em; max-width: 900px; padding: 0 0 1em 0'>
            Você pode se perguntar por que um designer optaria por usar o texto lorem ipsum em vez de alguns parágrafos em seu idioma nativo.
        </p>""", unsafe_allow_html=True)

        n_rows = len(st.session_state.wallets) / 3
        col2_1, col2_2, col2_3 = st.columns([1, 1, 1])

        st.session_state.wallets = st.session_state.wallets[::-1]

        with col2_3:
            for i in range(int(n_rows))[::-1]:
                container = st.container(border=True)
                container.markdown(f"##### **{st.session_state.wallets[i]['name']}**")
                for j in range(len(st.session_state.wallets[i]['stocks'])):
                    container.markdown(f"- {st.session_state.wallets[i]['stocks'][j]['name']}")
                container.button("Editar Carteira", key=f"edit_{i}", use_container_width=True)
                st.write("")
        with col2_2:
            for i in range(int(n_rows), int(n_rows * 2))[::-1]:
                container = st.container(border=True)
                container.markdown(f"##### **{st.session_state.wallets[i]['name']}**")
                for j in range(len(st.session_state.wallets[i]['stocks'])):
                    container.markdown(f"- {st.session_state.wallets[i]['stocks'][j]['name']}")
                container.button("Editar Carteira", key=f"edit_{i}", use_container_width=True)
                st.write("")
        with col2_1:
            for i in range(int(n_rows * 2), len(st.session_state.wallets))[::-1]:
                container = st.container(border=True)
                container.markdown(f"##### **{st.session_state.wallets[i]['name']}**")
                for j in range(len(st.session_state.wallets[i]['stocks'])):
                    container.markdown(f"- {st.session_state.wallets[i]['stocks'][j]['name']}")
                container.button("Editar Carteira", key=f"edit_{i}", use_container_width=True)
                st.write("")
                            

if __name__ == "__main__":
    main()
