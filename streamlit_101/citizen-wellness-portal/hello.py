import streamlit as st

st.set_page_config(page_title="Greeting App", page_icon=":wave:")

st.title("Greeting App")
st.write("Enter your name below and press **Greet** to see a friendly message.")

name = st.text_input("Name", value="")

if st.button("Greet"):
    if name.strip():
        st.success(f"Hello, {name}!")
    else:
        st.warning("Please enter a name before greeting.")
