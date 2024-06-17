import streamlit as st
from manager.user_manager import UserManager
from manager.app_manager import AppManager

import pandas as pd
import numpy as np
import altair as alt

def main():
    user_manager = UserManager()
    app_manager = AppManager()
    user_manager.verify_user()

    st.set_page_config(
        page_title="Ferramenta", 
        page_icon="📉", 
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
        disabled = False
        if len(st.session_state.portfolios) > 0:
            portfolio_titles = [portfolio['name'] for portfolio in st.session_state.portfolios]
        else:
            portfolio_titles = ['Nenhuma Carteira Cadastrada']
        st.write("Carteiras Cadastradas")
        portfolio= st.selectbox(
            label="Selecione uma Carteira",
            options=portfolio_titles,
            placeholder='Selecione uma Carteira',
            label_visibility='collapsed',
            disabled=len(st.session_state.portfolios) == 0,
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
            selected_portfolio = next((item for item in st.session_state.portfolios if item['name'] == portfolio), None)
            st.session_state.test = app_manager.run(time_period, selected_portfolio["stocks"])

            
    with col3:
        st.title("ModernMKZ")
        st.caption("Ferramenta de Análise de Carteiras de Ações")
        if st.session_state.get('showResult'):
            st.write(f"*Você selecionou a carteira __{portfolio}__ e o período de __{time_period}__*")
            if st.session_state.test:
                fig = st.session_state.test[0]
                fig.update_layout(
                    title={
                        'text': "Análise de Carteira de Ações (Fronteira Eficiente)",
                        'y': 0.95,       # Posição do título no eixo y (0 a 1)
                        'x': 0.05,          # Posição do título no eixo x (0 a 1)
                        'xanchor': 'left',  # Ancoragem horizontal do título
                        'yanchor': 'top',   # Ancoragem vertical do título
                    },
                    legend=dict(
                        traceorder='normal',  # Ordem dos itens na legenda (normal ou reversed)
                        orientation='h',     # Orientação da legenda ('h' para horizontal ou 'v' para vertical)
                        x=0,                # Posição da legenda no eixo x (0 a 1)
                        y=1.15,               # Posição da legenda no eixo y (0 a 1, negativo para baixo)
                        xanchor='left',     # Ancoragem horizontal da legenda
                        yanchor='top',        # Ancoragem vertical da legenda
                    ),
                    title_font=dict(size=22, color='#333'),  # Tamanho e cor do título
                )
                [df_pr, df_mr, df_rd] = app_manager.display_results(st.session_state.test)
                datas = st.session_state.test
                container = st.container(border=True)
                container.markdown(f"<div style='text-align: center; padding-bottom: 1em'><span style='font-weight: 900'>Peso no Ativo Livre de Risco:</span> {datas[4]}</div>", unsafe_allow_html=True)
                col1, col2 = st.columns((1.1, 3))
                with col1:
                    container = st.container(border=True)
                    container.markdown(f"<span style='font-weight: 900'>Menor Risco:</span>", unsafe_allow_html=True)
                    for i in range(len(datas[1])):
                        container.markdown(f"- {datas[1][i]}")
                            
                    container = st.container(border=True)
                    container.markdown(f"<span style='font-weight: 900'>Melhor Relação Risco/Retorno:</span>", unsafe_allow_html=True)
                    for i in range(len(datas[2])):
                        container.markdown(f"- {datas[2][i]}")

                    container = st.container(border=True)
                    container.markdown(f"<span style='font-weight: 900'>Risco Definido:</span>", unsafe_allow_html=True)
                    for i in range(len(datas[3])):
                        container.markdown(f"- {datas[3][i]}")

                with col2:
                    container = st.container(border=True)
                    container.plotly_chart(
                        fig, 
                        use_container_width=True, 
                        config={
                            'displayModeBar': True,  # Hide the mode bar
                            'scrollZoom': True,       # Enable mouse wheel zooming
                            'displaylogo': True,     # Hide the Plotly logo
                            'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d']  # Remove specific buttons
                        }
                    )
                    container2 = st.container(border=True, height=370)
                
                app_manager.show_example_graphs(y=df_pr['Ações'], x=df_pr['Porcentagem de Risco'], title='Porcentagem de Risco')
                app_manager.show_example_graphs(y=df_mr['Ações'], x=df_mr['Melhor Relação Risco/Retorno'], title='Melhor Relação Risco/Retorno')
                app_manager.show_example_graphs(y=df_rd['Ações'], x=df_rd['Risco Definido'], title='Risco Definido')
        else:
            st.markdown(
                '<div style="margin-top: 1em; display: flex; justify-content: center; align-items: center; width: 100%; padding: 5em"><div style="text-align: center; color: #bbb"><svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96" fill="none"><g clip-path="url(#clip0_17_12)"><path d="M72 24L60.36 49.04L81.36 70.04C85.56 63.72 88 56.16 88 48C88 25.92 70.08 8 48 8C39.84 8 32.28 10.44 25.96 14.64L46.96 35.64L72 24ZM11.24 22.56L14.64 25.96C9.16001 34.24 6.64001 44.68 8.72001 55.76C11.72 71.56 24.4 84.28 40.24 87.28C51.32 89.36 61.76 86.88 70.04 81.36L73.44 84.76C75 86.32 77.52 86.32 79.08 84.76C80.64 83.2 80.64 80.68 79.08 79.12L16.88 16.88C15.32 15.32 12.8 15.32 11.24 16.88C9.68001 18.44 9.68001 21 11.24 22.56ZM35.64 46.96L49.04 60.36L24 72L35.64 46.96Z" fill="#bbb"/></g><defs><clipPath id="clip0_17_12"><rect width="96" height="96" fill="white"/></clipPath></defs></svg><p style="margin-top: 1em">Selecione uma carteira e um período de tempo para visualizar os resultados.</p></div></div>',
                unsafe_allow_html=True
            )

            
if __name__ == "__main__":
    main()
