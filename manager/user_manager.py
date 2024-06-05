import streamlit as st

class UserManager:
    def __init__(self):
        self.init_session_state()

    def init_session_state(self):
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
        
    def verify_user(self):
        if st.session_state.get('authentication_status') != True:
            st.switch_page("pages/user.py")