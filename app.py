import streamlit as st
from manager.user_manager import UserManager
from manager.app_manager import AppManager

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

            n = 0
            selected_portfolio = next((portfolio for portfolio in st.session_state.portfolios if portfolio['name'] == st.session_state.portfolios[n]['name']), None)
            
            st.session_state.test = app_manager.run(time_period, selected_portfolio["stocks"])

            st.write(selected_portfolio["stocks"])

    with col3:
        st.title("ModernMKZ")
        if st.session_state.get('showResult'):
            st.caption(f"Você selecionou a carteira {portfolio} e o período de {time_period}")
            if st.session_state.test:
                app_manager.display_results(st.session_state.test)
        else:
            st.caption("## Selecione uma carteira e um período de tempo para visualizar os resultados.")

if __name__ == "__main__":
    main()
