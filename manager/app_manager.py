import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
import requests
import yfinance as yf
import numpy as np
import plotly.graph_objects as go
import cvxopt as opt
import os
import json
import random

class AppManager:
    def __init__(self):
        self.init_session_state()

    def init_session_state(self):
        st.session_state.show_result = st.session_state.get('show_result', False)
        st.session_state.result = st.session_state.get('result', None)
        st.session_state.test = st.session_state.get('test', None)
        st.session_state.disable = False
        st.session_state.portfolios = st.session_state.get('portfolios', [
            {
                "name": "Carteira 4",
                "stocks": ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "EMBR3.SA", "BBDC4.SA"]
            },
            {
                "name": "Carteira 1", 
                "stocks": ["PETR4.SA", "VALE3.SA", "ITUB4.SA"]
            },
            {
                "name": "Carteira 2",
                "stocks": ["PETR4.SA" "EMBR3.SA", "BBDC4.SA"]
            },
            {
                "name": "Carteira 3",
                "stocks": ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "EMBR3.SA", "BBDC4.SA"]
            },
            {
                "name": "Carteira 5",
                "stocks": ["PETR4.SA"]
            },
            {
                "name": "Carteira 6",
                "stocks": ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "EMBR3.SA", "BBDC4.SA"]
            }
        ])
        st.session_state.selected_option = st.session_state.get('selected_option', "Número de Ações")
    
    def diplay_portfolio(self, portfolios):
        x = 0
        while x < len(portfolios):
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                container = st.container(border=True)
                container.write(f"##### {portfolios[x]['name']}")
                for stock in portfolios[x]['stocks']:
                    container.markdown(f"- {stock}")
                if container.button("Editar Carteira", key=f"edit_{portfolios[x]['name']}", use_container_width=True, help="Edita a carteira selecionada"):
                    st.session_state.portfolios_edit = portfolios[x]
                    st.switch_page("pages/edit_portfolio.py")
                st.write("")
            with col2:
                if x+1 >= len(portfolios):
                    break
                container = st.container(border=True)
                container.write(f"##### {portfolios[x+1]['name']}")
                for stock in portfolios[x+1]['stocks']:
                    container.markdown(f"- {stock}")
                if container.button("Editar Carteira", key=f"edit_{portfolios[x+1]['name']}", use_container_width=True, help="Edita a carteira selecionada"):
                    st.session_state.portfolios_edit = portfolios[x+1]
                    st.switch_page("pages/edit_portfolio.py")
                st.write("")
            with col3:
                if x+2 >= len(portfolios):
                    break
                container = st.container(border=True)
                container.write(f"##### {portfolios[x+2]['name']}")
                for stock in portfolios[x+2]['stocks']:
                    container.markdown(f"- {stock}")
                if container.button("Editar Carteira", key=f"edit_{portfolios[x+2]['name']}", use_container_width=True, help="Edita a carteira selecionada"):
                    st.session_state.portfolios_edit = portfolios[x+2]
                    st.switch_page("pages/edit_portfolio.py")
                st.write("")
            x += 3

    def display_portfolios(self):
        portfolios = st.session_state.portfolios
        selected_option = st.session_state.selected_option

        if selected_option == "Data de Criação":
            self.diplay_portfolio(portfolios)
        elif selected_option == "Alfabético":
            sorted_portfolios = sorted(portfolios, key=lambda x: x['name'])
            self.diplay_portfolio(sorted_portfolios)
        elif selected_option == "Número de Ações":
            sorted_portfolios = sorted(portfolios, key=lambda x: len(x['stocks']), reverse=True)
            self.diplay_portfolio(sorted_portfolios)
        else:
            st.error(f"Opção de filtro inválida: {selected_option}")


        # n_rows = len(portfolios) // 3  # Integer division for cleaner layout
        # col2_1, col2_2, col2_3 = st.columns([1, 1, 1])

        # def display_portfolio_column(start, end, column):
        #     """Displays portfolios in a specific column with filtering applied."""
        #     for i in range(start, min(end, len(portfolios))):
        #         container = column.container(border=True)
        #         container.write(f"##### {portfolios[i]['name']}")
        #         for stock in portfolios[i]['stocks']:
        #             container.markdown(f"- {stock}")
        #         if container.button("Editar Carteira", key=f"edit_{i}", use_container_width=True, help="Edita a carteira selecionada"):
        #             st.session_state.portfolios_edit = portfolios[i]
        #             st.switch_page("pages/edit_portfolio.py")
        #         st.write("")

        # # Display portfolios based on selected option
        # if selected_option == "Data de Criação":
        #     try:
        #         sorted_portfolios = portfolios
        #     except KeyError:
        #         st.error("Chave 'created_at' não encontrada nos dados do portfólio.")
        #         return
        #     display_portfolio_column(0, int(n_rows + 1), col2_1)
        #     display_portfolio_column(int(n_rows + 1), (int(n_rows * 2) + 1), col2_2)
        #     display_portfolio_column((int(n_rows * 2) + 1), (len(sorted_portfolios)), col2_3)
        # elif selected_option == "Alfabético":
        #     display_portfolio_column(0, int(n_rows + 1), col2_1)
        #     display_portfolio_column(int(n_rows + 1), (int(n_rows * 2) + 1), col2_2)
        #     display_portfolio_column((int(n_rows * 2) + 1), (len(portfolios)), col2_3)
        # elif selected_option == "Número de Ações":
        #     sorted_portfolios = sorted(portfolios, key=lambda x: len(x['stocks']), reverse=True)  # Sort by number of stocks (descending)
        #     display_portfolio_column(0, int(n_rows + 1), col2_1)
        #     display_portfolio_column(int(n_rows + 1), (int(n_rows * 2) + 1), col2_2)
        #     display_portfolio_column((int(n_rows * 2) + 1), (len(sorted_portfolios)), col2_3)
        # else:
        #     st.error(f"Opção de filtro inválida: {selected_option}")  # Handle unexpected options


    def display_results(self, datas):
        datas = st.session_state.result
        df_pr = pd.DataFrame(
            {
                "Ações": [datas[1][i].split(": ")[0] for i in range(len(datas[1]))],
                "Porcentagem de Risco": [float(datas[1][i].split(": ")[1].replace("%", "")) for i in range(len(datas[1]))]
            }
        )
        df_mr = pd.DataFrame(
            {
                "Ações": [datas[2][i].split(": ")[0] for i in range(len(datas[2]))],
                "Melhor Relação Risco/Retorno": [float(datas[2][i].split(": ")[1].replace("%", "")) for i in range(len(datas[2]))]
            }
        )
        df_rd = pd.DataFrame(
            {
                "Ações": [datas[3][i].split(": ")[0] for i in range(len(datas[3]))],
                "Risco Definido": [float(datas[3][i].split(": ")[1].replace("%", "")) for i in range(len(datas[3]))]
            }
        )

        return [df_pr, df_mr, df_rd]
        
    def show_example_graphs(self, x, y, title):
        option = {
            "title": {
                "text": title,
                "top": "top",
                "textStyle": {
                    "color": "#333",
                    "fontSize": 20,
                },
            },
            "legend": {
                "grid": {
                    "left": "2%",
                },
            },
            "tooltip": {},
            "yAxis": { 
                "type": 'category',
                "axisTick": { "show": False },
                "data": y.tolist(),
            },
            "xAxis": {
                "type": 'value',
            },
            "grid": {
                "top": "10%",
                "left": '0',
                "right": '10%',
                "bottom": '0%',
                "containLabel": True
            },
            "series": [
                { 
                    "type": 'bar',
                    "data": x.tolist(),
                    "label": {
                        "show": True,
                        "position": "right",
                        "distance": 5,
                        # "verticalAlign": "middle",
                        "rotate": 0,
                        "formatter": '{c} %',
                        "fontSize": 9,
                        "rich": {
                            "name": {}
                        }
                    },
                }
            ],
        }
        st_echarts(options=option, height="400px")

    def get_selic(self):
        try:
            # URL Banco Central do Brasil API - dados da SELIC
            api_url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"

            response = requests.get(api_url)

            if response.status_code == 200:

                selic_data = response.json()

                most_recent_entry = selic_data[len(selic_data)-1]

                value = most_recent_entry["valor"]

                return float(value)
            else:
                print(f"Failed to fetch SELIC data. Status code: {response.status_code}")
                return 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
    
    def run(self, start_date, stocks): 
        np.random.seed(777)

        start_date = '2022-01-01'
        end_date = '2023-01-01'

        print("===========================================")
        print("Iniciando a análise de carteira de ações...")
        print(f"Carteira de ações selecionada: {stocks}")
        print("===========================================")

        table = yf.download(stocks, start=start_date, end=end_date)['Adj Close']

        # ===========================================

        returns = table.pct_change().dropna()
        mean_returns = returns.mean()
        cov_matrix = returns.cov()
        risk_free_rate = self.get_selic()

        # ===========================================

        pbar = opt.matrix(mean_returns.values)
        n = len(mean_returns)
        P = opt.matrix(cov_matrix.values)
        q = opt.matrix(0.0, (n,1))
        G = opt.matrix(0.0, (n+1,n))
        for i in range(n):
            G[i,i] = -1.0
        G[n,:] = -pbar.T
        h = opt.matrix(0.0, (n+1,1))
        A = opt.matrix(1.0, (1,n))
        b = opt.matrix(1.0)

        # Construção da fronteira eficiente
        portfolios = []
        for mu in np.linspace(min(pbar), max(pbar)):
            h[n,0] = -mu
            portfolios.append(opt.solvers.qp(P, q, G, h, A, b)['x'])
        returns = [opt.blas.dot(pbar, x)*252 for x in portfolios]
        risks = [np.sqrt(opt.blas.dot(x, P*x)*252) for x in portfolios]

        os.system('cls||clear')

        # Portfólio de menor risco
        i_min = np.argmin(risks)
        portfolio_min_risk = risks[i_min]
        portfolio_min_return = returns[i_min]
        print("===========================================")
        print('Portfólio de Menor Risco:') # x * (10 ^ (-01))
        decimal_number = portfolios[i_min]
        percentage_number = [x * 100 for x in decimal_number]
        low_risk_portfolio = []
        for i in range(len(stocks)):
            print(f'{stocks[i]}: {percentage_number[i]:.2f}%')
            low_risk_portfolio.append(f'{stocks[i]}: {percentage_number[i]:.2f}%')
        print("===========================================")

        # Portfólio de melhor relação risco/retorno (Índice de Sharpe)
        sharpe = [(returns[i] - risk_free_rate)/risks[i] for i in range(len(risks))]
        portfolio_sharpe = portfolios[np.argmax(sharpe)]

        print('Portfólio de Melhor Relação Risco/Retorno(Sharpe):')
        decimal_number = portfolio_sharpe
        percentage_number = [x * 100 for x in decimal_number]
        better_risk_return_portfolio = []
        for i in range(len(stocks)):
            print(f'{stocks[i]}: {percentage_number[i]:.2f}%')
            better_risk_return_portfolio.append(f'{stocks[i]}: {percentage_number[i]:.2f}%')
        print("===========================================")

        # Cálculo da reta tangente
        x = np.linspace(0.0, max(risks))
        y = risk_free_rate + sharpe[np.argmax(sharpe)]*x

        # Cálculo do retorno e do risco de melhor relação
        returno_sharpe = opt.blas.dot(pbar, portfolio_sharpe)*252
        risk_sharpe = np.sqrt(opt.blas.dot(portfolio_sharpe, P*portfolio_sharpe)*252)

        # Cálculo do ponto com risco definido
        risco_requerido = 0.2
        if risco_requerido > risk_sharpe:
            print('Risco maior que aquele associado à carteira de Sharpe ótimo!')
            print('Não há carteira ótima com esse risco!')
            return "bla"
        else:
            peso_requerido = risco_requerido/risk_sharpe
            print('Portfólio com Risco Definido:')
            decimal_number = peso_requerido*portfolio_sharpe
            percentage_number = [x * 100 for x in decimal_number]
            defined_risk_portfolio = []
            for i in range(len(stocks)):
                print(f'{stocks[i]}: {percentage_number[i][0]:.2f}%')
                defined_risk_portfolio.append(f'{stocks[i]}: {percentage_number[i][0]:.2f}%')
            print("===========================================")
            print('Peso no Ativo Livre de Risco')
            risk_free_rate_asset = f'{(1.0-peso_requerido)*100:.2f}%'
            print(f'{(1.0-peso_requerido)*100:.2f}%')
            x0 = peso_requerido*risk_sharpe
            y0 = peso_requerido*returno_sharpe + (1.0-peso_requerido)*risk_free_rate

        # Construção do gráfico interativo
        fig = go.Figure()

        # Scatter plot para a fronteira eficiente
        fig.add_trace(go.Scatter(
            x=risks,
            y=returns,
            mode='lines',
            name='Fronteira Eficiente',
        ))

        # Ponto de menor risco
        fig.add_trace(go.Scatter(
            x=[portfolio_min_risk],
            y=[portfolio_min_return],
            mode='markers',
            marker=dict(size=16, color='green'),
            name='Portfólio de Menor Risco',
        ))

        # Reta tangente
        fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode='lines',
            name='Reta Tangente',
            line=dict(color='gray', dash='dash'),
        ))

        # Ponto da melhor relação risco/retorno (Sharpe)
        fig.add_trace(go.Scatter(
            x=[risk_sharpe],
            y=[returno_sharpe],
            mode='markers',
            marker=dict(size=16, color='red'),
            name='Portfólio de Melhor Relação Risco/Retorno (Sharpe)',
        ))

        # Ponto com risco definido
        fig.add_trace(go.Scatter(
            x=[x0],
            y=[y0],
            mode='markers',
            marker=dict(size=16, color='orange'),
            name='Portfólio com Risco Definido',
        ))

        # Atualizando o layout do gráfico
        fig.update_layout(
            xaxis=dict(title='Risco'),
            yaxis=dict(title='Retorno'),
            showlegend=True,
        )
        
        return [fig, low_risk_portfolio, better_risk_return_portfolio, defined_risk_portfolio, risk_free_rate_asset]
    

    def get_portfolio_pie(self, datas, title, subtext='Fake Data', color='gray'):
        names = [item.split(": ")[0] for item in datas]
        percentages = [int(float(item.split(": ")[1].strip('%'))) for item in datas]
        data = [{"value": value, "name": name} for value, name in zip(percentages, names)]

        if subtext == 'Risco Mínimo':
            risk_colors = ['#56E280', '#1D7C39', '#165D2B', '#0B3017', '#0A2914']
        elif subtext == 'Risco Definido':
            risk_colors = ['#EE9149', '#D87E39', '#C26B29', '#A05821', '#83481B']
        elif subtext == 'Risco Alto':
            risk_colors = ['#EF4949', '#C62525', '#A31E1E', '#811818', '#400C0C']
        elif subtext == 'Risco não definido':
            risk_colors = ['#D3D3D3', '#A9A9A9', '#808080', '#696969', '#000000']

        option = {
            "title": {
            "text": title,
            "subtext": subtext,
            "left": 'center',
            "subtextStyle": {
                "color": color
            }
            },
            "tooltip": {
            "trigger": 'item'
            },
            "legend": {
            "left": 'center',
            "top": '16%',
            },
            "color": risk_colors,
            "series": [
            {
                "name": 'portifolio',
                "type": 'pie',
                "radius": ['35%', '65%'],
                "center": ['50%', '65%'],
                "avoidLabelOverlap": False,
                "label": {
                "show": False,
                "position": 'center'
                },
                "emphasis": {
                "label": {
                    "show": True,
                    "fontSize": 18,
                    "fontWeight": 'bold'
                }
                },
                "labelLine": {
                "show": False
                },
                "data": data
            }
            ]
        }
        st_echarts(options=option, height="400px", key=title)

    def get_pie_portfolios(self):
        datas = st.session_state.result
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            container = st.container(border=True)
            with container:
                self.get_portfolio_pie(datas=datas[1], title='Menor Risco', subtext='Risco Mínimo', color='green')
                    
        with col3:
            container = st.container(border=True)
            with container:
                self.get_portfolio_pie(datas=datas[3], title='Risco Definido', subtext='Risco Definido', color='orange')

        with col4:
            container = st.container(border=True)
            with container:
                self.get_portfolio_pie(datas=datas[2], title='Melhor Relação Risco/Retorno', subtext='Risco Alto', color='red')
        
        with col1:
            container = st.container(border=True)
            with container:
                self.get_portfolio_pie(datas=datas[1], title='Portifólio Atual', subtext='Risco não definido')

    def show_results(self):
        self.get_pie_portfolios()
        fig = st.session_state.result[0]
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
                orientation='h',     # Orientação da legenda ('h' para hmorizontal ou 'v' para vertical)
                x=0,                # Posição da legenda no eixo x (0 a 1)
                y=1.15,               # Posição da legenda no eixo y (0 a 1, negativo para baixo)
                xanchor='left',     # Ancoragem horizontal da legenda
                yanchor='top',        # Ancoragem vertical da legenda
            ),
            title_font=dict(size=22, color='#333'),  # Tamanho e cor do título
        )
        st.plotly_chart(
            fig, 
            use_container_width=True, 
            config={
                'displayModeBar': True,  # Hide the mode bar
                'scrollZoom': True,       # Enable mouse wheel zooming
                'displaylogo': True,     # Hide the Plotly logo
                'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d']  # Remove specific buttons
            }
        )
        self.show_results_old()

    def show_results_old(self):
        datas = st.session_state.result
        container = st.container(border=True)
        container.markdown(f"<div style='text-align: center; padding-bottom: 1em'><span style='font-weight: 900'>Peso no Ativo Livre de Risco:</span> {datas[4]}</div>", unsafe_allow_html=True)