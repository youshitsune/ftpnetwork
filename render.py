import streamlit as st

con = st.empty()
def run():
    with con.form("connection"):
        ip = st.text_input("Hostname", label_visibility="hidden", placeholder="Hostname")
        user = st.text_input("Username", label_visibility="hidden", placeholder="Username")
        passwd = st.text_input("Password", label_visibility="hidden", placeholder="Password")
        submit = st.form_submit_button("Submit")
        if submit and ip != "":
            return [ip, user, passwd]
        else:
            return []
