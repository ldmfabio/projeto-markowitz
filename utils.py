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
    # wallets
    st.session_state.wallets = st.session_state.get('wallets', [
        {
            "name": "Carteira 1",
            "stocks": [
                {
                    "name": "Ação 1",
                },
                {
                    "name": "Ação 2",
                }
            ]
        },
        {
            "name": "Carteira 2",
            "stocks": [
                {
                    "name": "Ação 3",
                },
                {
                    "name": "Ação 4",
                }
            ]
        },
        {
            "name": "Carteira 3",
            "stocks": [
                {
                    "name": "Ação 5",
                },
                {
                    "name": "Ação 6",
                }
            ]
        },
        {
            "name": "Carteira 4",
            "stocks": [
                {
                    "name": "Ação 7",
                },
                {
                    "name": "Ação 8",
                }
            ]
        },
        {
            "name": "Carteira 5",
            "stocks": [
                {
                    "name": "Ação 9",
                },
                {
                    "name": "Ação 10",
                }
            ]
        }
    ])
    st.session_state.wallet_name = st.session_state.get('wallet_name', None)
    st.session_state.wallet_description = st.session_state.get('wallet_description', None)

def verify_user():
    if st.session_state.get('authentication_status') != True:
        st.switch_page("pages/user.py")