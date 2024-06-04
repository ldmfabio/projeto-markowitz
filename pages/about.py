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
        st.page_link("app.py", use_container_width=True, label="Ferramenta", icon="📈")
        st.page_link("pages/about.py", use_container_width=True, label="Sobre o Projeto", icon="📄")
        st.page_link("pages/portfolio.py", use_container_width=True, label="Carteiras", icon="💼")
        st.page_link("pages/user.py", use_container_width=True, label="Perfil", icon="👾")
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
        st.write('#')

        col1, col2, col3 = st.columns(3, gap="large")

        with col1:
            st.image('./assets/img/logo-ifc.png', width=300)

        with col2:
            st.image('./assets/img/logo-fabrica.png')
        st.write("*Versão 1.0.3*")

    

if __name__ == "__main__":
    main()
