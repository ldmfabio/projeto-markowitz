import streamlit as st
import os
import math
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import cvxopt as opt
import yfinance as yf
import requests
import datetime
from streamlit_echarts import st_echarts
from utils import *

class AppManager:
    def __init__(self):
        self.init_session_state()
        self.verify_user()

    def init_session_state(self):
        st.session_state.datas = st.session_state.get('datas', {})
        st.session_state.portfolios = st.session_state.get('portfolios', [])
        st.session_state.selected_option = st.session_state.get('selected_option', "Número de Ações")
        st.session_state['user_id'] = st.session_state.get('user_id', None)
        st.session_state['name'] = st.session_state.get('name', None)
        st.session_state['email'] = st.session_state.get('email', None)
        st.session_state['authentication_status'] = st.session_state.get('authentication_status', False)

    def verify_user(self):
        if st.session_state.get('authentication_status') != True:
            st.switch_page("pages/login.py")
    
    def formatted_real(self, value):
        return f"{value:.2f}".replace(".", ",")

    def diplay_portfolio(self, portfolios):
        x = 0
        while x < len(portfolios):
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                container = st.container(border=True)
                container.write(f"##### {portfolios[x]['name']}")
                for stock in portfolios[x]['stocks']:
                    container.markdown(f"<div style='display:flex; justify-content:space-between'>{stock['name']}<p style='text-align: right'>R$ {self.formatted_real(stock['value'])}</p></div>", unsafe_allow_html=True)
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
                    container.markdown(f"<div style='display:flex; justify-content:space-between'>{stock['name']}<p style='text-align: right'>R$ {self.formatted_real(stock['value'])}</p></div>", unsafe_allow_html=True)
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
                    container.markdown(f"<div style='display:flex; justify-content:space-between'>{stock['name']}<p style='text-align: right'>R$ {self.formatted_real(stock['value'])}</p></div>", unsafe_allow_html=True)
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

    def pie_charts(self):
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            container = st.container(border=True)
            with container:
                self.portfolio_pie('low_risk_portfolio', 'Menor Risco', 'Risco Mínimo', 'green')
                self.portifolio_list('low_risk_portfolio')
                    
        with col3:
            container = st.container(border=True)
            with container:
                self.portfolio_pie(type='defined_risk_portfolio', title='Risco Definido', subtext='Risco Definido', color='orange', risk='risk_free_rate_asset')
                self.portifolio_list(type='defined_risk_portfolio', risk='risk_free_rate_asset')

        with col4:
            container = st.container(border=True)
            with container:
                self.portfolio_pie('better_risk_return_portfolio', 'Maior Retorno', 'Risco Alto', 'red')
                self.portifolio_list('better_risk_return_portfolio')

        with col1:
            container = st.container(border=True)
            with container:
                self.portfolio_pie('selected_portfolio', 'Portifólio Atual', 'Risco não definido')
                self.portifolio_list('selected_portfolio')

    def portfolio_pie(self, type, title, subtext='Fake Data', color='gray', risk=False):
        names = [item.split(": ")[0] for item in st.session_state.datas[type]]
        percentages = [float(item.split(": ")[1].strip('%')) for item in st.session_state.datas[type]]

        if risk:
            risk = st.session_state.datas[risk]
            names.append('ATIVO LIVRE')
            percentages.append(float(risk.strip('%')))
            data = [{"value": value, "name": name} for value, name in zip(percentages, names)]
        else:
            data = [{"value": value, "name": name} for value, name in zip(percentages, names)]

        if subtext == 'Risco Mínimo':
            risk_colors = ['#56E280', '#1D7C39', '#165D2B', '#0B3017', '#0A2914']
        elif subtext == 'Risco Definido':
            risk_colors = ['#EE9149', '#D87E39', '#C26B29', '#A05821', '#83481B']
        elif subtext == 'Risco Alto':
            risk_colors = ['#EF4949', '#C62525', '#A31E1E', '#811818', '#400C0C']
        elif subtext == 'Risco não definido':
            risk_colors = ['#D3D3D3', '#A9A9A9', '#808080', '#696969', '#444']

        option = {
            "title": {
                "text": title,
                "subtext": subtext,
                "left": 'center',
                "textStyle": {
                    "color": color,
                    "fontSize": "16px",
                },
                "subtextStyle": {
                    "color": color
                }
            },
            "tooltip": {
            "trigger": 'item'
            },
            "legend": {
                "show": False,
                "left": 'center',
                "top": '0%',
            },
            "color": risk_colors,
            "series": [
            {
                "name": 'portifolio',
                "type": 'pie',
                "radius": ['45%', '80%'],
                "center": ['50%', '60%'],
                "avoidLabelOverlap": False,
                "tooltip": {
                    "trigger": '', 
                    "formatter": "" 
                },
                "label": {
                    "show": False,
                    "position": 'center',
                    "formatter": "{b} \n\n {c}%"
                },
                "emphasis": {
                    "label": {
                        "show": True,
                        "fontSize": 14,
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
        st_echarts(options=option, height="300px", key=f'{title}{subtext}{color}')

    def portifolio_list(self, type, risk=0):
        datas = st.session_state.datas[type]
        formatted_datas = []

        for item in datas:
            name = item.split(': ')[0]
            value = item.split(': ')[1].split('%')[0]
            formatted_datas.append({
                "name": name, 
                "value": value
            })
            percentage = float(value)
            formatted_value = f"R$ {formatted_real((percentage * st.session_state.datas['total']) / 100)}"
            weight = '' if percentage == 0 else 'font-weight: 900'
            st.markdown(f"<div style='display:flex; justify-content:space-between;'>{name}<p style='text-align: right; {weight}'>{formatted_value}</p></div>", unsafe_allow_html=True)
        
        hasRisk = formatted_real((float(st.session_state.datas['risk_free_rate_asset'].split('%')[0]) * st.session_state.datas['total']) / 100) if risk != 0 else 'R$ 0,00'
        st.markdown(f"<div style='display:flex; justify-content:space-between;'>ATIVO LIVRE<p style='text-align: right;'>{hasRisk}</p></div>", unsafe_allow_html=True)

    def main_chart(self):
        fig = st.session_state.datas['fig']
        fig.update_layout(
            title={
                'text': "Análise de Carteira de Ações (Fronteira Eficiente)",
                'y': 0.95,
                'x': 0.05,
                'xanchor': 'left',
                'yanchor': 'top',
            },
            legend=dict(
                traceorder='normal',
                orientation='h',
                x=0.01, 
                y=1.15,           
                xanchor='left',  
                yanchor='top',    
            ),
            title_font=dict(size=22, color='#333'),
        )
        st.plotly_chart(
            fig, 
            use_container_width=True, 
            config={
                'displayModeBar': True, 
                'scrollZoom': True,       
                'displaylogo': True,     
                'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d'] 
            }
        )

    def heatmap(self):
        returns = st.session_state.datas['returns']
        corr_matrix = returns.corr()
        stocks =  st.session_state.datas['stocks']

        df_heatmap = []
        x = 0
        y = 0
        for i in corr_matrix.columns:
            for j in corr_matrix.index:
                df_heatmap.append([x, y, round(corr_matrix[i][j], 4)])
                if y >= len(corr_matrix.columns) - 1:
                    x += 1
                    y = 0
                else:
                    y += 1
                
        data = df_heatmap

        option = {
            "title": {
                "text": 'Correlação entre Ações',
                "left": '5%',
                "top": 'top'
            },
            "tooltip": {
                "position": 'top'
            },
            "grid": {
                "height": '50%',
                "top": '10%'
            },
            "xAxis": {
                "type": 'category',
                "data": stocks[::-1],
                "splitArea": {
                    "show": True
                }
            },
            "yAxis": {
            "type": 'category',
            "data": stocks[::-1],
            "splitArea": {
                "show": True
            }
            },
            "visualMap": {
                "min": corr_matrix.min().min(),
                "max": corr_matrix.max().max(),
                "calculable": True,
                "orient": 'horizontal',
                "left": 'center',
                "bottom": '15%'
            },
            "series": [
                {
                    "name": 'Punch Card',
                    "type": 'heatmap',
                    "data": data,
                    "label": {
                    "show": True
                    },
                    "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowColor": 'rgba(0, 0, 0, 0.5)'
                    }
                    }
                }
            ]
        }
        st_echarts(options=option, height="400px")

    def get_datas(self, start_date, stocks, selected_portfolio): 
        np.random.seed(777)
        stocks = [stocks['name'] for stocks in stocks]

        end_date = self.get_current_date()
        current_year = int(end_date.split("-")[0])
        if start_date == "3 anos":
            start_date = str(current_year - 3) + end_date[4:]
        elif start_date == "5 anos":
            start_date = str(current_year - 5) + end_date[4:]

        table = yf.download(stocks, start=start_date, end=end_date)['Adj Close']

        # ===========================================

        returns = table.pct_change().dropna()
        mean_returns = returns.mean()
        nl, nc = returns.shape
        returns = returns[1:nl]
        cov_matrix = self.cov1Para(returns)
        risk_free_rate = self.get_selic()

        if isinstance(risk_free_rate, str):
            print("hola")
            st.write(risk_free_rate)
            return {}

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
        decimal_number = portfolios[i_min]
        percentage_number = [x * 100 for x in decimal_number]
        low_risk_portfolio = []
        for i in range(len(stocks)):
            low_risk_portfolio.append(f'{stocks[i]}: {percentage_number[i]:.2f}%')

        sharpe = [(returns[i] - risk_free_rate)/risks[i] for i in range(len(risks))]
        portfolio_sharpe = portfolios[np.argmax(sharpe)]

        decimal_number = portfolio_sharpe
        percentage_number = [x * 100 for x in decimal_number]
        better_risk_return_portfolio = []
        for i in range(len(stocks)):
            better_risk_return_portfolio.append(f'{stocks[i]}: {percentage_number[i]:.2f}%')

        x = np.linspace(0.0, max(risks))
        y = risk_free_rate + sharpe[np.argmax(sharpe)]*x

        returno_sharpe = opt.blas.dot(pbar, portfolio_sharpe)*252
        risk_sharpe = np.sqrt(opt.blas.dot(portfolio_sharpe, P*portfolio_sharpe)*252)

        # Cálculo do ponto com risco definido
        risco_requerido = 0.2
        if risco_requerido > risk_sharpe:
            return {
                "error": "Risco maior que aquele associado à carteira de Sharpe ótimo!\n\nNão há carteira ótima com esse risco!"
            }
        else:
            peso_requerido = risco_requerido/risk_sharpe
            decimal_number = peso_requerido*portfolio_sharpe
            percentage_number = [x * 100 for x in decimal_number]
            defined_risk_portfolio = []
            for i in range(len(stocks)):
                defined_risk_portfolio.append(f'{stocks[i]}: {percentage_number[i][0]:.2f}%')
            risk_free_rate_asset = f'{(1.0-peso_requerido)*100:.2f}%'
            x0 = peso_requerido*risk_sharpe
            y0 = peso_requerido*returno_sharpe + (1.0-peso_requerido)*risk_free_rate

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=risks,
            y=returns,
            mode='lines',
            name='Fronteira Eficiente',
        ))
        fig.add_trace(go.Scatter(
            x=[portfolio_min_risk],
            y=[portfolio_min_return],
            mode='markers',
            marker=dict(size=16, color='green'),
            name='Portfólio de Menor Risco',
        ))
        fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode='lines',
            name='Reta Tangente',
            line=dict(color='gray', dash='dash'),
        ))
        fig.add_trace(go.Scatter(
            x=[risk_sharpe],
            y=[returno_sharpe],
            mode='markers',
            marker=dict(size=16, color='red'),
            name='Portfólio de Melhor Relação Risco/Retorno (Sharpe)',
        ))
        fig.add_trace(go.Scatter(
            x=[x0],
            y=[y0],
            mode='markers',
            marker=dict(size=16, color='orange'),
            name='Portfólio com Risco Definido',
        ))
        fig.update_layout(
            xaxis=dict(title='Risco'),
            yaxis=dict(title='Retorno'),
            showlegend=True,
        )
        
        return {
            "fig": fig,
            "low_risk_portfolio": low_risk_portfolio,
            "better_risk_return_portfolio": better_risk_return_portfolio,
            "defined_risk_portfolio": defined_risk_portfolio,
            "risk_free_rate_asset": risk_free_rate_asset,
            "stocks": stocks,
            "returns": table.pct_change().dropna(),
            "selic": self.get_selic(),
            "selected_portfolio": self.format_portfolio(selected_portfolio),
            "total": sum(stock['value'] for stock in selected_portfolio['stocks'])
        }

    def format_portfolio(self, selected_portfolio):
        total_value = sum(stock['value'] for stock in selected_portfolio['stocks'])
        formatted_portfolio = []
        
        for stock in selected_portfolio['stocks']:
            percentage = (stock['value'] / total_value) * 100 if total_value != 0 else 0
            formatted_portfolio.append(f"{stock['name']}: {percentage:.2f}%")
        
        return formatted_portfolio

    def cov1Para(self, Y,k = None):
        N,p = Y.shape

        if k is None or math.isnan(k):
            mean = Y.mean(axis=0)
            Y = Y.sub(mean, axis=1)
            k = 1
        
        n = N-k                         
        sample = pd.DataFrame(np.matmul(Y.T.to_numpy(),Y.to_numpy()))/n

        diag = np.diag(sample.to_numpy())
        meanvar= sum(diag)/len(diag)
        target=meanvar*np.eye(p)

        Y2 = pd.DataFrame(np.multiply(Y.to_numpy(),Y.to_numpy()))
        sample2= pd.DataFrame(np.matmul(Y2.T.to_numpy(),Y2.to_numpy()))/n
        piMat=pd.DataFrame(sample2.to_numpy()-np.multiply(sample.to_numpy(),sample.to_numpy()))

        pihat = sum(piMat.sum())

        gammahat = np.linalg.norm(sample.to_numpy()-target,ord = 'fro')**2

        rho_diag=0
        rho_off=0

        rhohat=rho_diag+rho_off
        kappahat=(pihat-rhohat)/gammahat

        shrinkage=max(0,min(1,kappahat/n))
        sigmahat=shrinkage*target+(1-shrinkage)*sample

        return sigmahat

    def get_selic(self):
        try:
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
            return "Ocorreu um erro de conexão"

    def get_current_date(self):
        current_date = datetime.date.today()
        formatted_date = current_date.strftime("%Y-%m-%d")
        return formatted_date