import streamlit as st
from docx import Document
import io

st.set_page_config(page_title="AI Resume Maker PRO", page_icon="🚀")
st.title("🚀 AI Resume Maker PRO")
st.markdown("Made by **Dileep Kumar M** - PRO Version")

name = st.text_input("Full Name", "Dileep Kumar M")
role = st.text_input("Target Role", "Software Engineer")
skills = st.text_area("Your Skills", "Python, SQL, Streamlit, GitHub")
experience = st.text_area("Experience", "B.Tech CSE, AI Projects")

if st.button("Generate PRO Resume"):
    if name and role:
        st.success("Resume Generated PRO Level!")
        st.subheader(f"{name} - {role}")
        st.write(f"Skills: {skills}")
        st.write(f"Experience: {experience}")
        
        doc = Document()
        doc.add_heading(name, 0)
        doc.add_paragraph(role)
        doc.add_paragraph(f"Skills: {skills}")
        doc.add_paragraph(f"Experience: {experience}")
        bio = io.BytesIO()
        doc.save(bio)
        st.download_button("Download DOCX", bio.getvalue(), file_name="Resume.docx")