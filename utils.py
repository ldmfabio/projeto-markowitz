import streamlit as st

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
    st.session_state.portfolios = st.session_state.get('portfolios', [])

def verify_user():
    if st.session_state.get('authentication_status') != True:
        st.switch_page("pages/user.py")

def display_portfolios(portfolios, session_state):
    n_rows = len(portfolios) / 3
    col2_1, col2_2, col2_3 = st.columns([1, 1, 1])
    
    def display_portfolio_column(start_idx, end_idx, column):
        for i in range(start_idx, end_idx):
            container = column.container(border=True)
            container.markdown(f"##### **{portfolios[i]['name']}**")
            for j in range(len(portfolios[i]['stocks'])):
                container.markdown(f"- {portfolios[i]['stocks'][j]}")
            if container.button("Editar Carteira", key=f"edit_{i}", use_container_width=True):
                session_state.portfolios_edit = portfolios[i]
                st.switch_page("pages/edit_portfolio.py")
            st.write("")

    display_portfolio_column(0, int(n_rows), col2_3)
    display_portfolio_column(int(n_rows), int(n_rows * 2), col2_2)
    display_portfolio_column(int(n_rows * 2), len(portfolios), col2_1)