import streamlit as st
import requests
from manager.app_manager import AppManager
from utils import add_custom_css, create_navbar, loader, validar_form

def main():
    st.set_page_config(
        page_title="Editar Carteira", 
        page_icon="✏️", 
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
        st.write(f"## Editar Carteira: {st.session_state.portfolios_edit['name']}")
        
        cols1 = st.columns([4,1])

        # Nome da Carteira
        name_portfolio = cols1[0].text_input(
            key=f"portfolio_{st.session_state.portfolios.index(st.session_state.portfolios_edit)}",
            value=st.session_state.portfolios_edit['name'],
            label="Nome da Carteira",
        )

        # Número de Ações
        number = cols1[1].number_input(
            'Digite o número de ações', 
            step=1, 
            max_value=24,  
            min_value=1, 
            value=len(st.session_state.portfolios_edit['stocks'])
        )

        stocks = []
        for j in range(number):
            value = st.session_state.portfolios_edit['stocks'][j] if j < len(st.session_state.portfolios_edit['stocks']) else {"name": "", "value": 0.0}
            cols = st.columns([4,1])
            
            # Nome da Ação
            stock = cols[0].text_input(
                key=f"stock_{j}",
                value=value['name'] if isinstance(value, dict) else "",
                label=f"Nome da Ação {j+1}",
            )

            # Valor Investido
            stock_value = cols[1].number_input(
                key=f"stock_value_{j}",
                value=float(value['value']) if isinstance(value, dict) else 0.0,
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
                try:
                    # Enviar solicitação de exclusão para a API
                    response = requests.delete(
                        f'http://127.0.0.1:8000/api/portfolios/{st.session_state.portfolios_edit["id"]}/'
                    )
                    response.raise_for_status()  # Verifica se não houve erro na requisição

                    # Remover a carteira do session_state
                    st.session_state.portfolios.remove(st.session_state.portfolios_edit)
                    st.success("Carteira excluída com sucesso!")
                    st.switch_page("pages/portfolio.py")
                
                except requests.exceptions.RequestException as e:
                    st.error(f"❗Erro ao excluir carteira: {str(e)}")

        with cols_btn_2:
            if st.button("Salvar Alterações", key="save", use_container_width=True, type="primary", help="Salva as alterações feitas na carteira"):
                loader('Salvando Alterações')
                if validar_form(name_portfolio, stocks):
                    try:
                        # Enviar alterações para a API
                        response = requests.put(
                            f'http://127.0.0.1:8000/api/portfolios/{st.session_state.portfolios_edit["id"]}/',
                            json={
                                "name": name_portfolio,
                                "stocks": stocks,
                                "user": st.session_state.get("user_id")  # Certifique-se de que o user_id está presente no session_state
                            }
                        )
                        response.raise_for_status()  # Verifica se não houve erro na requisição

                        # Atualizar a lista de carteiras no session_state
                        st.session_state.portfolios[st.session_state.portfolios.index(st.session_state.portfolios_edit)] = response.json()
                        st.success("Alterações salvas com sucesso!")
                        st.switch_page("pages/portfolio.py")
                    
                    except requests.exceptions.RequestException as e:
                        st.error(f"❗Erro ao salvar alterações: {str(e)}")
                else:
                    st.warning("Preencha todos os campos", icon="⚠️")

if __name__ == "__main__":
    main()
