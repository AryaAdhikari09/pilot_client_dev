import streamlit as st
import requests
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages
# from navigation import login_button  # Importing login_button from navigation module


def register_user(email, password):
    BASE_URL = "https://pilot-server-12yj.vercel.app"
    response = requests.post(
        f"{BASE_URL}/register", json={"email": email, "password": password}
    )
    return response


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")
    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        
        st.markdown("# Daira Edtech")
        st.write("##### Where every step is a continuation.")
        st.write("---")
        st.write("")
make_sidebar()

def login_button():
    if st.button("Login", key="sdfsdfsdfsdfsdggfth"):
        st.session_state.logged_in = False

        st.switch_page("login.py")


def logout():
    st.session_state.logged_in = False
    st.session_state.token = None
    st.session_state.email = ""
    st.info("Logged out successfully!")

    st.switch_page("login.py")



# Streamlit app for user registration
st.title("User Registration")
st.write("---")

# Register user
st.header("Register")
register_email = st.text_input("Email")
register_password = st.text_input("Password", type="password")

if st.button("Register"):
    response = register_user(register_email, register_password)

    if response.status_code == 201:
        st.success("User registered successfully!")
        # login_button()
    else:
        error_message = response.json().get("message", "Registration failed.")
        st.error(error_message)
        # if error_message == "User already exists":
        #     # login_button()
login_button()
