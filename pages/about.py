import streamlit as st
from manager.app_manager import AppManager
from utils import *

def main():
    st.set_page_config(
        page_title="Sobre o Projeto", 
        page_icon="📄", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )  
    app_manager = AppManager()
    add_custom_css()

    col1, col2, col3 = st.columns([1, .2, 5])
    with col1:
        create_navbar()
    with col3:
        st.write("")
        st.write("## Bem-vindo ao Projeto de Pesquisa")
        st.write('''
            Este projeto consiste numa aplicação web de gerenciamento de carteiras de investimentos na perspectiva da Teoria de Markowitz. Sua finalidade é avaliar e determinar o equilíbrio entre o risco e o retorno a partir de um conjunto de ativos disponíveis.
        ''')
        st.write('''
            É consenso no mercado financeiro que distribuir os recursos disponíveis em classes de ativos não correlacionados constitui a melhor maneira de diminuir os riscos nos investimentos. Isso ocorre porque a descorrelação dos ativos faz com que os mesmos se comportem de maneira distinta num mesmo período, acabando por contribuir com a redução da volatilidade global da carteira. A montagem de uma carteira de investimento que segue os princípios de alocação de ativos, pertinentes à Teoria Moderna do Portfólio, segue o pressuposto de que dentre duas carteiras que produzem o mesmo retorno, é preferível aquela que possui o menor risco. A teoria desenvolvida por Markowitz propõe um modelo que fornece a carteira com o menor risco para um retorno definido ou, fixado o nível de risco, aquela carteira com o maior retorno para um nível de risco especificado.
        ''')
        st.write('''
            Nessa teoria, o risco é interpretado como a volatilidade e é medido a partir da variância. O modelo matemático adotado se insere na área de otimização convexa e foi implementado numericamente na linguagem python. A partir do conjunto de ativos que compõem a carteira do investidor, a aplicação web fornece três composições de portfólios:
        ''')
        st.write('''
            - A carteira global de menor risco (volatilidade) possível;
            - A carteira com a melhor relação entre risco e retorno, no sentido do Índice de Sharpe; e
            - A carteira com a melhor relação entre risco e retorno, na presença do ativo livre de risco.
        ''')
        col1, col2, col3 = st.columns([1.5, 1, 1])
        col1.caption("### Equipe:")
        col1.write('''
            - Coordenador: [Prof. Adriano Rodrigues de Melo](www.linkedin.com/in/adriano-rodrigues-de-melo)
            - Colaborador: [Prof. Fábio Longo de Moura](www.linkedin.com/in/fabio-longo-de-moura)
            - Colaborador: [Jonathan Ache Dias](www.linkedin.com/in/jonathan-ache-dias)
            - Estudante Bolsista: [Mateus Lopes Albano](www.linkedin.com/in/mateus-lopes-albano)
            - Estudante Bolsista: [Gabriel Lopres Pereira](www.linkedin.com/in/gabriel-lopres-pereira)
            - Estudante Voluntário: [Lucas Antonete](www.linkedin.com/in/lucas-antonete)
        ''')
        col3.caption("### Tecnologias Utilizadas:")
        col3.write('''
            - Streamlit
            - Python
            - Pandas
            - Yfinance
            - Echarts
            - Django
        ''')
        col2.caption("### Fontes de Dados:")
        col2.write('''
            - Yahoo Finance
        ''')
        st.write('')
        st.write('')
        st.write('')

if __name__ == "__main__":
    main()
