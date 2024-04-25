import streamlit as st
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

    col1, col2 = st.columns([1, 4])

    with col1:
        st.divider()
        st.page_link("app.py", label="Página Inicial", icon="🌎")
        st.page_link("pages/tool.py", label="Ferramenta", icon="📉")
        st.page_link("pages/wallets.py", label="Carteiras", icon="💼")
        st.page_link("pages/user.py", label="Perfil", icon="👾")
        st.divider()
        if st.button('Adicionar Carteira', type='primary', use_container_width=True):
            st.session_state.showResult = True
    with col2:
        st.title("Suas Carteiras")
        st.caption("""<p style='font-size: 1.4em; max-width: 900px'>
            Você pode se perguntar por que um designer optaria por usar o texto lorem ipsum em vez de alguns parágrafos em seu idioma nativo. 
        </p>""", unsafe_allow_html=True)
    
        for i in st.session_state.wallets:
            st.divider()
            cols = st.columns(2)
            cols[0].markdown(f"**Nome:** {i['name']}")
            cols[1].markdown(f"**Descrição:** {i['description']}")
            for j in i['stocks']:
                cols = st.columns(4)
                cols[0].markdown(f"**Nome:** {j['name']}")
                cols[1].markdown(f"**Descrição:** {j['description']}")
                cols[2].markdown(f"**Quantidade:** {j['quantity']}")
                cols[3].markdown(f"**Preço:** {j['price']}")
            st.write('---')

if __name__ == "__main__":
    main()
