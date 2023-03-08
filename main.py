import streamlit as st
from ftplib import FTP
import render as r

ftp = None
fp = []

def retrive(s):
    global fp
    for i in s.decode("utf-8").splitlines():
        fp.append(i)

def main():
    try:
        retr = ftp.retrbinary('RETR index.html', retrive)
    except Exception:
        r.con.error("There isn't an index.html file")
    else:
        with r.con.container():
            st.markdown("\n".join(fp), unsafe_allow_html=True)
            st.button("Disconnect")


def connect(ip, user, passwd):
    global ftp
    try:
        ftp = FTP(ip, user, passwd)
    except Exception as e:
        st.error(f"Error: {e}")
    else:
        r.con.empty()
        main()

resp = r.run()
if resp != []:
    connect(resp[0], resp[1], resp[2])
