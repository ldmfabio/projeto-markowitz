import streamlit as st

import pandas as pd
# import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from utils import init_session, verify_user

def main(): 
    init_session()
    verify_user()
    st.set_page_config(
        page_title="Ferramenta", 
        page_icon="📉", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )

    col1, col2 = st.columns([1, 4])

    with col1:
        st.divider()
        # st.write("Menu de Navegação")
        st.page_link("app.py", label="Página Inicial", icon="🌎")
        st.page_link("pages/tool.py", label="Ferramenta", icon="📉")
        st.page_link("pages/portfolio.py", label="Carteiras", icon="💼")
        st.page_link("pages/user.py", label="Perfil", icon="👾")

        st.divider()

        portfolios = [
                {
                    'title': 'portfolio1'
                },
                {
                    'title': 'portfolio2'
                },
            ]

        portfolio_titles = [portfolio['title'] for portfolio in portfolios]

        st.write("Carteiras Cadastradas")
        portfolio= st.selectbox(
            label="Selecione uma Carteira",
            options=portfolio_titles,
            placeholder='Selecione uma Carteira',
            label_visibility='collapsed',
        )

        st.write("Selecione o período de tempo:")
        # Radio buttons para 3 e 5 anos
        time_period = st.radio(
            "Selecione o período de tempo:",
            ('3 anos', '5 anos'),
            label_visibility='collapsed',
        )
        
        if st.button('Fazer Busca', type='primary', use_container_width=True):
            st.session_state.showResult = True

    with col2:
        st.title("ModernMKZ")
        st.caption("""<p style='font-size: 1.4em; max-width: 900px'>
            Você pode se perguntar por que um designer optaria por usar o texto lorem ipsum em vez de alguns parágrafos em seu idioma nativo. 
        </p>""", unsafe_allow_html=True)

        col1, col2, col3 = st.columns((1, .2, 1))

        with col1:
            st.write("gráfico 1")
            data_other = {
                'x': [1, 2, 3, 4, 5],
                'y': [4, 6, 5, 8, 2]
            }
            df_other = pd.DataFrame(data_other)
            st.line_chart(df_other)
            
        with col3:
            st.write("gráfico 2")
            data = {
                'x': [1, 2, 8, 4, 8],
                'y': [4, 8, 5, 8, 2]
            }
            df = pd.DataFrame(data)
            st.bar_chart(df)

           
if __name__ == "__main__":
    main()
