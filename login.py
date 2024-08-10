import streamlit as st
import requests
from time import sleep

# Function to handle login via Node.js server
def login_user(email, password):
    # Update BASE_URL with your Vercel deployment URL
    BASE_URL = "https://pilot-server-12yj.vercel.app"
    response = requests.post(
        f"{BASE_URL}/login", json={"email": email, "password": password}
    )
    if response.status_code == 200:
        token = response.json().get("token")
        return token, response
    else:
        return None, response

def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")
    return pages[ctx.page_script_hash]["page_name"]

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

def make_sidebar():
    with st.sidebar:
        st.markdown("# Daira Edtech")
        st.write("##### Where every step is a continuation.")
        st.write("---")
        st.write("")

make_sidebar()

# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "token" not in st.session_state:
    st.session_state.token = None
if "email" not in st.session_state:
    st.session_state.email = ""

# Streamlit app setup
st.title("User Login")

# Login form
st.write("---")

st.header("Login")
login_email = st.text_input("Email")
login_password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    token, response = login_user(login_email, login_password)
    
    if token:
        st.session_state.logged_in = True  # Set session state for logged-in status
        st.session_state.token = token  # Store the token in the session state
        st.session_state.email = login_email
        # st.write("LOged IN")
        sleep(5)
        st.switch_page("pages/home.py")
    else:
        st.error("Incorrect username or password")

# Link to registration page
if st.button("Register User"):
    st.switch_page("pages/register.py")
