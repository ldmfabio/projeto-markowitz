import streamlit as st
import time

def create_navbar(type=None):
    st.write("##### ")
    st.write("### ModernMKZ")
    st.divider()
    st.write("__Menu de Navegação__")
    st.page_link("app.py", use_container_width=True, label="Ferramenta", icon="📈")
    st.page_link("pages/about.py", use_container_width=True, label="Sobre o Projeto", icon="📄")
    st.page_link("pages/portfolio.py", use_container_width=True, label="Carteiras", icon="💼")
    st.page_link("pages/user.py", use_container_width=True, label="Perfil", icon="👾")
    st.divider()
    if not type:
        st.write("__Créditos__")
        st.image('./assets/img/group3.png', use_column_width=True)

def loader(text):
    text = text + '...'
    with st.spinner(text):
        time.sleep(1)
    # fazer um toast no futuro

def formatted_real(value):
    return f"{value:.2f}".replace(".", ",")

def validar_form(name_portfolio, stocks):
    if name_portfolio == "":
        return False
    for stock in stocks:
        if stock == "":
            return False
    return True

def add_custom_css():
    st.markdown(
        """
        <style>
        .custom-container {
            background-color: #f0f0f5;
            padding: 10px;
            border-radius: 5px;
        }
        .custom-title {
            color: #333;
            font-size: 24px;
            font-weight: bold;
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        .stDeployButton { visibility: hidden; }
        
        [data-testid="stStatusWidget"] { visibility: hidden; }
        [data-testid="stHeader"] { visibility: hidden; }
        [data-testid="stAppViewBlockContainer"] { padding: 2em 5em; }
        [data-testid="stSidebar"] { display: none;  }
        [data-testid="baseButton-headerNoPadding"] { display: none; visibility: hidden; }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    st.write("This is outside the custom container.")

if __name__ == "__main__":
    main()
