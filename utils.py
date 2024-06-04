import streamlit as st
import pandas as pd
import numpy as np
from streamlit_echarts import st_echarts

def init_session():
    # auth
    st.session_state.username = st.session_state.get('username', None)
    st.session_state.name = st.session_state.get('name', None)
    st.session_state.email = st.session_state.get('email', None)
    st.session_state.password = st.session_state.get('password', None)
    st.session_state.confirm_password = st.session_state.get('confirm_password', None)
    st.session_state.old_password = st.session_state.get('old_password', None)
    st.session_state.new_password = st.session_state.get('new_password', None)
    st.session_state.new_confirm_password = st.session_state.get('new_confirm_password', None)
    st.session_state.create_username = st.session_state.get('create_username', None)
    st.session_state.create_name = st.session_state.get('create_name', None)
    st.session_state.create_email = st.session_state.get('create_email', None)
    st.session_state.create_password = st.session_state.get('create_password', None)
    st.session_state.create_confirm_password = st.session_state.get('create_confirm_password', None)
    st.session_state.new_username = st.session_state.get('new_username', None)
    st.session_state.new_name = st.session_state.get('new_name', None)
    st.session_state.new_email = st.session_state.get('new_email', None)
    # tool
    st.session_state.showResult = st.session_state.get('showResult', False)
    # portfolios
    st.session_state.disable = False
    st.session_state.portfolios = st.session_state.get('portfolios', [{"name": "Carteira 1", "stocks": ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "EMBR3.SA", "BBDC4.SA"]}])
    st.session_state.test = st.session_state.get('test', None)

def verify_user():
    if st.session_state.get('authentication_status') != True:
        st.switch_page("pages/user.py")

def display_portfolios(portfolios, session_state):
    n_rows = len(portfolios) / 3
    col2_1, col2_2, col2_3 = st.columns([1, 1, 1])
    
    def display_portfolio_column(start, end, column):
        for i in range(start, min(end, len(portfolios))):
            container = column.container(border=True)
            container.write(f"##### {portfolios[i]['name']}")
            for j in range(len(portfolios[i]['stocks'])):
                container.markdown(f"- {portfolios[i]['stocks'][j]}")
            if container.button("Editar Carteira", key=f"edit_{i}", use_container_width=True):
                st.session_state.portfolios_edit = st.session_state.portfolios[i]
                st.switch_page("pages/edit_portfolio.py")
            st.write("")

    display_portfolio_column(0, int(n_rows + 1), col2_1)
    display_portfolio_column(int(n_rows + 1), (int(n_rows * 2)  + 1), col2_2)
    display_portfolio_column((int(n_rows * 2) + 1), (len(portfolios)), col2_3)

def display_results(datas):
    df = pd.DataFrame(datas)
    col1, col2, col3 = st.columns((1, .2, 1))
    with col1:
        x = datas["Ações"]
        x1 = datas["Porcentagem de Risco"]
        option = {
            "legend": {
                "grid": {
                    "left": "2%",
                },
            },
            "tooltip": {},
            "yAxis": { 
                "type": 'category',
                "axisTick": { "show": False },
                "data": datas["Ações"],
            },
            "xAxis": {
                "type": 'value',
            },
            "grid": {
                "left": '3%',
                "right": '4%',
                "bottom": '0%',
                "containLabel": True
            },
            "series": [
                { 
                    "type": 'bar',
                    "data": datas["Porcentagem de Risco"],
                    "label": {
                        "show": True,
                        "position": "inside",
                        "distance": 25,
                        "align": "center",
                        "verticalAlign": "middle",
                        "rotate": 0,
                        "formatter": '{c} %',
                        "fontSize": 16,
                        "rich": {
                            "name": {}
                        }
                    },
                }
            ],
        }

        # st_echarts(options=option, height="500px")
        
        df['Porcentagem de Risco'] = df['Porcentagem de Risco'].apply(lambda x: f"{x}%")
        st.table(df)
        
    with col3:
        st.write("gráfico 2")
        data = {
            'x': datas["Ações"],
            'y': datas["Porcentagem de Risco"]
        }
        df = pd.DataFrame(data)
        st.bar_chart(df)