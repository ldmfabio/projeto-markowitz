import streamlit as st
from manager.app_manager import AppManager
import requests
from utils import *

def fetch_portfolios():
    try:
        response = requests.get(f'http://127.0.0.1:8000/api/portfolios/?user={st.session_state["user_id"]}')
        response.raise_for_status()
        portfolios = response.json()
        st.session_state['portfolios'] = portfolios
        return portfolios
    except requests.exceptions.RequestException as e:
        st.error(f"❗Erro ao buscar carteiras: {str(e)}")
        return []

def main():
    app_manager = AppManager()
    st.set_page_config(
        page_title="Ferramenta", 
        page_icon="📉", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()
    fetch_portfolios()

    col1, col2, col3 = st.columns([1, .2, 5])
    
    with col1:      
        create_navbar(type='tool')
        st.write("__Opções__")
        st.write("Carteiras Cadastradas")
        if len(st.session_state['portfolios']) > 0:
            portfolio_titles = [portfolio['name'] for portfolio in st.session_state['portfolios']]
        else:
            portfolio_titles = ['Nenhuma Carteira Cadastrada']
        portfolio = st.selectbox(
            label="Selecione uma Carteira",
            options=portfolio_titles,
            placeholder='Selecione uma Carteira',
            label_visibility='collapsed',
            disabled=len(st.session_state.portfolios) == 0,
        )
        st.write("Selecione o período de tempo:")
        time_period = st.radio(
            "Selecione o período de tempo:",
            ('3 anos', '5 anos'),
            label_visibility='collapsed',
        )
        if st.button('Fazer Busca', type='primary', use_container_width=True):
            selected_portfolio = next((item for item in st.session_state.portfolios if item['name'] == portfolio), None)
            st.session_state.datas = app_manager.get_datas(time_period, selected_portfolio["stocks"], selected_portfolio)
        st.divider()
        st.write("")
        st.image('./assets/img/group3.png', use_column_width=True)
    with col3:
        if st.session_state.get('datas'):
            st.write("")
            st.write("## Resultado da Análise")
            st.caption("Este resultado foi alcançado por meio de uma análise detalhada dos dados históricos de ações, utilizando o método de Markowitz para identificar a combinação ideal de ativos que maximiza o retorno esperado para um dado nível de risco.")
            st.write(f"*Você selecionou a carteira __{portfolio}__ e o período de __{time_period}__ ( Taxa livre de risco: __{app_manager.get_selic() * 100} %__ )*")
            app_manager.pie_charts()
            app_manager.main_chart()
            app_manager.heatmap()
        else:
            st.write("")
            st.write("## Ferramenta de Análise de Carteiras de Ações")
            st.caption("Selecionando uma carteira e um período de tempo, você poderá visualizar o resultado da análise de risco e retorno da carteira selecionada.")
            st.markdown(
                '<div style="margin-top: 5em; display: flex; justify-content: center; align-items: center; width: 100%; padding: 5em"><div style="text-align: center; color: #bbb"><svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96" fill="none"><g clip-path="url(#clip0_17_12)"><path d="M72 24L60.36 49.04L81.36 70.04C85.56 63.72 88 56.16 88 48C88 25.92 70.08 8 48 8C39.84 8 32.28 10.44 25.96 14.64L46.96 35.64L72 24ZM11.24 22.56L14.64 25.96C9.16001 34.24 6.64001 44.68 8.72001 55.76C11.72 71.56 24.4 84.28 40.24 87.28C51.32 89.36 61.76 86.88 70.04 81.36L73.44 84.76C75 86.32 77.52 86.32 79.08 84.76C80.64 83.2 80.64 80.68 79.08 79.12L16.88 16.88C15.32 15.32 12.8 15.32 11.24 16.88C9.68001 18.44 9.68001 21 11.24 22.56ZM35.64 46.96L49.04 60.36L24 72L35.64 46.96Z" fill="#bbb"/></g><defs><clipPath id="clip0_17_12"><rect width="96" height="96" fill="white"/></clipPath></defs></svg><p style="margin-top: 1em">Selecione uma carteira e um período de tempo para visualizar os resultados.</p></div></div>',
                unsafe_allow_html=True
            )
  
if __name__ == "__main__":
    main()
