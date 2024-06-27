import streamlit as st

class UserManager:
    def __init__(self):
        self.init_session_state()

    def init_session_state(self):
        if 'username' not in st.session_state:
            st.session_state['username'] = None
        if 'name' not in st.session_state:
            st.session_state['name'] = None
        if 'email' not in st.session_state:
            st.session_state['email'] = None
        
    def verify_user(self):
        if st.session_state.get('authentication_status') != True:
            st.switch_page("pages/login.py")
