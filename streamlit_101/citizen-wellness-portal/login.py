import streamlit as st
import hashlib
import os
import base64
import hmac
from datetime import datetime

# -----------------------
# Helpers: init + crypto
# -----------------------
def init_state():
    """Initialize session_state keys if they don't exist."""
    if 'users' not in st.session_state:
        # users: { username: { 'salt': base64, 'pw_hash': base64, 'created': iso } }
        st.session_state['users'] = {}
    if 'current_user' not in st.session_state:
        st.session_state['current_user'] = None

def _hash_password(password: str, salt: bytes | None = None):
    """Return (salt_b64, hash_b64). Uses PBKDF2-HMAC-SHA256."""
    if salt is None:
        salt = os.urandom(16)
    # iterations chosen for example; raise for production strength
    iterations = 100_000
    dk = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations)
    return base64.b64encode(salt).decode('utf-8'), base64.b64encode(dk).decode('utf-8')

def _verify_password(password: str, salt_b64: str, hash_b64: str) -> bool:
    """Verify password using constant-time comparison."""
    salt = base64.b64decode(salt_b64)
    expected = base64.b64decode(hash_b64)
    new_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)
    return hmac.compare_digest(new_hash, expected)

# -----------------------
# User management
# -----------------------
def register_user(username: str, password: str):
    """Register a new user. Raises ValueError on errors."""
    if not username or not password:
        raise ValueError("Username and password are required.")
    users = st.session_state['users']
    if username in users:
        raise ValueError("User already exists.")
    salt_b64, hash_b64 = _hash_password(password)
    users[username] = {
        'salt': salt_b64,
        'pw_hash': hash_b64,
        'created': datetime.utcnow().isoformat() + 'Z'
    }
    # not strictly needed (dict is mutated), but explicit assignment can help clarity
    st.session_state['users'] = users

def login_user(username: str, password: str):
    """Attempt login. Raises ValueError on failure."""
    if not username or not password:
        raise ValueError("Username and password are required.")
    users = st.session_state['users']
    if username not in users:
        raise ValueError("No such user.")
    user = users[username]
    if not _verify_password(password, user['salt'], user['pw_hash']):
        raise ValueError("Wrong password.")
    st.session_state['current_user'] = username

def logout():
    st.session_state['current_user'] = None

# -----------------------
# Streamlit UI
# -----------------------
init_state()

st.title("Auth demo (session_state users dict)")

if st.session_state['current_user']:
    st.success(f"Logged in as: {st.session_state['current_user']}")
    if st.button("Logout"):
        logout()
else:
    mode = st.radio("Choose", ["Login", "Register"])

    with st.form(key="auth_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Submit")

    if submit:
        try:
            if mode == "Register":
                register_user(username.strip(), password)
                st.success("Registered successfully. You can now log in.")
            else:  # Login
                login_user(username.strip(), password)
                st.success(f"Welcome back, {st.session_state['current_user']}!")
        except ValueError as e:
            st.error(str(e))

# For debugging / demo only: show user list (masked)
if st.checkbox("Show users (debug)"):
    safe_list = {
        u: {"created": st.session_state['users'][u]['created']}
        for u in st.session_state['users']
    }
    st.write(safe_list)
