import yfinance as yf
import numpy as np
import plotly.graph_objects as go
import cvxopt as opt
from get_selic import get_selic
import os
import json

def get_graph(start_date, end_date): 
    np.random.seed(777)

    # stocks = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "EMBR3.SA", "BBDC4.SA"]
    stocks = ["PETR4.SA", "VALE3.SA", "ITUB4.SA"]

    start_date = start_date
    end_date = end_date

    table = yf.download(stocks, start=start_date, end=end_date)['Adj Close']

    # ===========================================

    returns = table.pct_change().dropna()
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    risk_free_rate = get_selic()

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
        marker=dict(size=10, color='red'),
        name='Portfólio de Menor Risco',
    ))

    # Reta tangente
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name='Reta Tangente',
    ))

    # Ponto da melhor relação risco/retorno (Sharpe)
    fig.add_trace(go.Scatter(
        x=[risk_sharpe],
        y=[returno_sharpe],
        mode='markers',
        marker=dict(size=10, color='green'),
        name='Portfólio de Melhor Relação Risco/Retorno (Sharpe)',
    ))

    # Ponto com risco definido
    fig.add_trace(go.Scatter(
        x=[x0],
        y=[y0],
        mode='markers',
        marker=dict(size=10, color='blue'),
        name='Portfólio com Risco Definido',
    ))

    # Atualizando o layout do gráfico
    fig.update_layout(
        xaxis=dict(title='Risco'),
        yaxis=dict(title='Retorno'),
        showlegend=True,
    )

    data = fig.to_json()
    data = json.loads(data)
    return [data, low_risk_portfolio, better_risk_return_portfolio, defined_risk_portfolio, risk_free_rate_asset]