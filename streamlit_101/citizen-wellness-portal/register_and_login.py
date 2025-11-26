# app.py
import streamlit as st
import os
import hashlib
import hmac
import binascii
from datetime import datetime
import secrets

# -------------------------
# Helper functions (hashing)
# -------------------------
def _generate_salt(n_bytes: int = 16) -> bytes:
    return os.urandom(n_bytes)

def _hash_password(password: str, salt: bytes, iterations: int = 100_000) -> bytes:
    """
    Return the derived key (bytes) for `password` using PBKDF2-HMAC-SHA256.
    """
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations)

def _storeable(salt: bytes, derived_key: bytes) -> dict:
    """
    Convert bytes to hex strings for safe storage in session_state
    """
    return {
        'salt': binascii.hexlify(salt).decode('ascii'),
        'hash': binascii.hexlify(derived_key).decode('ascii'),
        'iterations': 100_000
    }

def _from_store(stored: dict) -> tuple:
    """
    Convert stored hex strings back to bytes (salt, derived_key).
    """
    salt = binascii.unhexlify(stored['salt'].encode('ascii'))
    derived_key = binascii.unhexlify(stored['hash'].encode('ascii'))
    iterations = stored.get('iterations', 100_000)
    return salt, derived_key, iterations

# -------------------------
# Initialize session_state
# -------------------------
def init_state():
    """
    Ensure required keys exist in st.session_state.
    - users: dict mapping username -> {salt, hash, iterations, created}
    - current_user: username or None
    - flash: transient message slot
    """
    if 'users' not in st.session_state:
        # Example: create a built-in demo user (optional)
        st.session_state['users'] = {}
    if 'current_user' not in st.session_state:
        st.session_state['current_user'] = None
    if 'flash' not in st.session_state:
        st.session_state['flash'] = None

init_state()

# -------------------------
# Registration
# -------------------------
def register_user(username: str, password: str) -> tuple[bool, str]:
    """
    Try to register. Returns (success, message).
    """
    username = username.strip()
    if not username or not password:
        return False, "Username and password are required."

    if username in st.session_state['users']:
        return False, "That username already exists. Choose a different one."

    # create salt + hash
    salt = _generate_salt()
    derived = _hash_password(password, salt)
    stored = _storeable(salt, derived)
    stored['created'] = datetime.utcnow().isoformat() + 'Z'
    st.session_state['users'][username] = stored
    return True, "Registration successful. You can now log in."

# -------------------------
# Login / credential check
# -------------------------
def check_credentials(username: str, password: str) -> tuple[bool, str]:
    """
    Validate username/password. Returns (success, message).
    """
    username = username.strip()
    if username not in st.session_state['users']:
        return False, "User not found."

    stored = st.session_state['users'][username]
    salt, stored_hash, iterations = _from_store(stored)
    derived = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations)

    # constant-time comparison
    if hmac.compare_digest(derived, stored_hash):
        st.session_state['current_user'] = username
        return True, f"Welcome, {username}!"
    else:
        return False, "Incorrect password."

# -------------------------
# Logout helper
# -------------------------
def logout():
    st.session_state['current_user'] = None
    st.session_state['flash'] = "Logged out."

# -------------------------
# UI
# -------------------------
st.title("Simple Streamlit Auth (session_state users)")

# flash message
if st.session_state.get('flash'):
    st.info(st.session_state['flash'])
    st.session_state['flash'] = None

# Show current user / logout
if st.session_state['current_user']:
    st.success(f"Logged in as: {st.session_state['current_user']}")
    if st.button("Logout"):
        logout()
    st.write("---")
else:
    st.info("You are not logged in.")

# Tabs: Register / Login / Debug
tab1, tab2, tab3 = st.tabs(["Register", "Login", "Debug"])

with tab1:
    st.header("Register")
    with st.form("register_form"):
        new_user = st.text_input("Username")
        new_pass = st.text_input("Password", type="password")
        confirm = st.text_input("Confirm password", type="password")
        submitted = st.form_submit_button("Register")
        if submitted:
            if new_pass != confirm:
                st.error("Passwords do not match.")
            else:
                ok, msg = register_user(new_user, new_pass)
                if ok:
                    st.success(msg)
                else:
                    st.error(msg)

with tab2:
    st.header("Login")
    with st.form("login_form"):
        user = st.text_input("Username", key="login_username")
        pwd = st.text_input("Password", type="password", key="login_password")
        login_sub = st.form_submit_button("Log in")
        if login_sub:
            ok, msg = check_credentials(user, pwd)
            if ok:
                st.success(msg)
            else:
                st.error(msg)

with tab3:
    st.header("Debug / Current users (in-memory)")
    st.write("**Note:** This information is stored in-memory in `st.session_state` and is not persistent.")
    st.write("Users (username -> metadata):")
    if st.session_state['users']:
        # show username + created date only
        for u, meta in st.session_state['users'].items():
            st.write(f"- **{u}** (created: {meta.get('created', 'unknown')})")
    else:
        st.write("No users yet.")
    if st.button("Clear all users (danger!)"):
        st.session_state['users'] = {}
        st.session_state['current_user'] = None
        st.success("All users cleared.")
