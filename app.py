import streamlit as st

import streamlit_authenticator as stauth

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import yaml
from yaml.loader import SafeLoader



def main():
    st.set_page_config(
        page_title="Projeto Markowitz", 
        page_icon="💣", 
        layout="wide", 
        initial_sidebar_state="expanded", 
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': """About this app: This is a cool app that does cool things. Have fun! 🚀"""
        }
    )  

    with st.sidebar:
        pass

    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    
    # authenticator = Authenticate(
    #     config['credentials'],
    #     config['cookie']['name'],
    #     config['cookie']['key'],
    #     config['cookie']['expiry_days'],
    #     config['preauthorized']
    # )

    # name, authentication_status, username = authenticator.login('Login', 'main')
    # st.write(name, authentication_status, username)

    st.write('Hello, world!')

if __name__ == '__main__':
    main()