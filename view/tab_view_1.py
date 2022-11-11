import streamlit as st
from pathlib import Path

def tab_1():
    intro_markdown = Path("view/tab1.md").read_text()
    st.markdown(intro_markdown, unsafe_allow_html=True)
    