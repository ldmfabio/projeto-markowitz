import streamlit as st
import requests
from manager.app_manager import AppManager
from utils import add_custom_css, create_navbar, loader, validar_form

def main():
    st.set_page_config(
        page_title="Adicionar Carteira", 
        page_icon="➕", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()
    app_manager = AppManager()

    col1, col2, col3 = st.columns([1, .2, 5])
    with col1:
        create_navbar(type='portfolio')
    
    with col3:
        st.write("")
        st.write("## Adicionar Carteira")
        cols1 = st.columns([4,1])
        
        # Nome da Carteira
        name_portfolio = cols1[0].text_input(
            key=f"add_portfolio",
            value="",
            label="Nome da Carteira",
        )

        # Número de Ações
        number = cols1[1].number_input(
            'Digite o número de ações', 
            step=1, 
            max_value=24,  
            min_value=1, 
            value=1
        )

        stocks = []
        for j in range(number):
            cols = st.columns([4,1])
            
            # Nome da Ação
            stock = cols[0].text_input(
                key=f"stock_{j}",
                value="",
                label=f"Nome da Ação {j+1}",
            )

            # Valor Investido
            stock_value = cols[1].number_input(
                key=f"stock_value_{j}",
                value=0.0,
                label=f"Valor Investido (R$)",
                step=0.01, 
                max_value=10000.0,
                min_value=0.0,
                format='%.2f'
            )

            stocks.append({
                "name": stock,
                "value": stock_value
            })

        cols_btn_1, cols_btn_2 = st.columns([1,2])
        with cols_btn_1:
            if st.button("Excluir Carteira", key="delete", use_container_width=True, type="secondary", help="Exclui a carteira"):
                loader('Excluindo Carteira')
                st.session_state.portfolios.remove(st.session_state.portfolios_edit)
                st.switch_page("pages/portfolio.py")

        with cols_btn_2:
            if st.button("Adicionar nova Carteira", key="save", use_container_width=True, type="primary", help="Adiciona a carteira"):
                loader('Salvando Alterações')
                
                # Validação e Adição da Carteira
                if validar_form(name_portfolio, stocks):
                    try:
                        # Enviar dados para a API
                        response = requests.post(
                            'http://127.0.0.1:8000/api/portfolios/',
                            json={
                                "name": name_portfolio,
                                "stocks": stocks,
                                "user": st.session_state.get("user_id")  # Certifique-se de que o user_id está presente no session_state
                            }
                        )
                        response.raise_for_status()  # Verifica se não houve erro na requisição

                        # Atualizar a lista de carteiras no session_state
                        st.session_state.portfolios.append(response.json())
                        st.success("Carteira adicionada com sucesso!")
                        st.switch_page("pages/portfolio.py")
                    
                    except requests.exceptions.RequestException as e:
                        st.error(f"❗Erro ao salvar carteira: {str(e)}")

                else:
                    st.warning("Preencha todos os campos", icon="⚠️")

if __name__ == "__main__":
    main()