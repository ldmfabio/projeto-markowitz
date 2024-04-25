import streamlit as st
from streamlit_authenticator.authenticate.authentication import AuthenticationHandler
import yaml
from yaml.loader import SafeLoader
from utils import init_session, verify_user

def main():
    init_session()
    verify_user()
    st.set_page_config(
        page_title="Página Inicial", 
        page_icon="🌎", 
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
    with col3:
        # Carregar as credenciais do arquivo YAML e instanciar o objeto de autenticação
        with open('./config.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)
        auth_handler = AuthenticationHandler(credentials=config['credentials'])

        st.title("ModernMKZ")

        st.write('''
            Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.
        ''')
    

if __name__ == "__main__":
    main()
