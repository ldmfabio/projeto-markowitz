import streamlit as st
from streamlit_authenticator.authenticate.authentication import AuthenticationHandler
import yaml
from yaml.loader import SafeLoader
from manager.user_manager import UserManager
from utils import *

def main():
    user_manager = UserManager()
    user_manager.verify_user()

    st.set_page_config(
        page_title="Sobre o Projeto", 
        page_icon="📄", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )  
    add_custom_css()

    col1, col2, col3 = st.columns([1, .2, 5])

    with col1:
        create_navbar()
    with col3:
        # Carregar as credenciais do arquivo YAML e instanciar o objeto de autenticação
        with open('./config.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)
        auth_handler = AuthenticationHandler(credentials=config['credentials'])

       
        st.write("")
        st.write("## Bem-vindo ao Projeto de Pesquisa")
        st.write('''
            Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desco a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.
        ''')
        st.write('''
            Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.
        ''')

        col1, col2, col3 = st.columns([1, 1, 1])
        col1.caption("### Equipe:")
        col1.write('''
            - Professor Responsável: [Rafael Speroni](www.linkedin.com/in/rafael-speroni)
            - Professora Colaborador: [Larissa](www.linkedin.com/in/larissa)
            - Alunos Bolsistas:
                - [Amanda](www.linkedin.com/in/amanda)
                - [Gabriel](www.linkedin.com/in/gabriel)
            - Alunos Voluntários:
                - [Luan](www.linkedin.com/in/luan)
                - [Lucas](www.linkedin.com/in/lucas)
        ''')        
        col2.caption("### Tecnologias Utilizadas:")
        col2.write('''
            - Streamlit
            - Python
            - Pandas
            - Yfinance
            - Plotly
            - Streamlit Autheticator
            - YAML
            - Echarts
        ''')
        col3.caption("### Fontes de Dados:")
        col3.write('''
            - Yahoo Finance
        ''')
    

if __name__ == "__main__":
    main()
