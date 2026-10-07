import streamlit as st
from docx import Document
from fpdf import FPDF
import io

st.set_page_config(page_title="AI Resume Maker PRO", page_icon="🚀")
st.title("AI Resume Maker PRO")
st.markdown("Made by **Dileep Kumar M** - PRO Version ")

name = st.text_input("Full Name", "Dileep Kumar M")
role = st.text_input("Target Role", "Software Engineer")
skills = st.text_area("Your Skills", "Python, SQL, Streamlit, GitHub")
experience = st.text_area("Experience", "B.Tech CSE, Built AI Resume Maker")

if st.button("Generate PRO Resume"):
    if name and role:
       