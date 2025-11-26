import streamlit as st
from random import randint

# Protect the page
if "current_user" not in st.session_state or st.session_state["current_user"] is None:
    st.error("You must log in first.")
    st.stop()

username = st.session_state["current_user"]

st.title(f"Welcome, {username}! 👋")
st.markdown("### Dashboard Overview")
st.write("---")

labels = ["Revenue", "Growth %", "Active Users", "NPS"]
values = ["$125,000", "8.4%", "3,240", "42"]

rows = 2
cols_per_row = 2

for r in range(rows):
    cols = st.columns(cols_per_row)
    for c in range(cols_per_row):
        idx = r * cols_per_row + c
        if idx < len(labels):
            cols[c].metric(labels[idx], values[idx], delta=f"{randint(-10,10)}%")

st.write("---")

if st.button("Logout"):
    st.session_state["current_user"] = None
    st.switch_page("app.py")
