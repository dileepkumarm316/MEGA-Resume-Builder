import streamlit as st
from docx import Document
from fpdf import FPDF
import io

st.set_page_config(page_title="PRO Resume")
st.markdown("## 🚀 AI Resume PRO - FINAL")

name = st.text_input("Name","Dileep Kumar M")
role = st.text_input("Role","Software Engineer")
email = st.text_input("Email","dileep@gmail.com")
phone = st.text_input("Phone","+91 98765")
skills = st.text_area("Skills","Python, Java, SQL")
exp = st.text_area("Exp","Software Engineer at TechCorp")
edu = st.text_input("Edu","B.Tech CSE")

if st.button("Generate PRO Resume"):
    st.success("PRO Resume Ready!")
    st.write(f"**{name} | {role}**")
    
    # DOCX
    doc = Document()
    doc.add_heading(name, 0)
    doc.add_paragraph(f"{role} | {email} | {phone}")
    doc.add_heading("SKILLS", 2)
    doc.add_paragraph(skills)
    doc.add_heading("EXPERIENCE", 2)
    doc.add_paragraph(exp)
    doc.add_heading("EDUCATION", 2)
    doc.add_paragraph(edu)
    bio = io.BytesIO()
    doc.save(bio)
    
    # PDF - FIXED
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(30,70,130)
    pdf.rect(0,0,210,35,'F')
    pdf.set_y(10)
    pdf.set_text_color(255,255,255)
    pdf.set_font("Arial","B",16)
    pdf.cell(0,10,name,align='C',ln=True)
    pdf.set_font("Arial","",10)
    pdf.cell(0,8,f"{role} | {email}",align='C',ln=True)
    pdf.set_y(45)
    pdf.set_text_color(0,0,0)
    pdf.set_font("Arial","B",12)
    pdf.cell(0,10,"SKILLS",ln=True)
    pdf.set_font("Arial","",10)
    pdf.multi_cell(0,6,skills)
    pdf.set_font("Arial","B",12)
    pdf.cell(0,10,"EXPERIENCE",ln=True)
    pdf.set_font("Arial","",10)
    pdf.multi_cell(0,6,exp)
    pdf.set_font("Arial","B",12)
    pdf.cell(0,10,"EDUCATION",ln=True)
    pdf.set_font("Arial","",10)
    pdf.multi_cell(0,6,edu)
    
    # New PDF method - no error
    out = pdf.output()
    pdf_bio = io.BytesIO(out)
    
    c1, c2 = st.columns(2)
    with c1:
        st.download_button("📄 DOCX",bio.getvalue(),"resume.docx")
    with c2:
        st.download_button("📕 PDF",pdf_bio.getvalue(),"resume.pdf")