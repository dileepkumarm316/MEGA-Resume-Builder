import streamlit as st
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from fpdf import FPDF
import io

st.set_page_config(page_title="PRO Resume")
st.markdown("## 🚀 AI Resume PRO - FINAL")

name = st.text_input("Name","Dileep Kumar M")
role = st.text_input("Role","Software Engineer")
email = st.text_input("Email","dileep@gmail.com")
phone = st.text_input("Phone","+91 98765 43210")
skills = st.text_area("Skills","Python, Java, SQL, AWS, Docker")
exp = st.text_area("Experience","Software Engineer at TechCorp | 2022-Present")
edu = st.text_input("Education","B.Tech CSE - Anna University")

if st.button("Generate PRO Resume"):
    st.success("PRO Resume Ready!")
    st.write(f"**{name} | {role}**")

    # --- PRO DOCX MAKER ---
    doc = Document()
    # Header
    p = doc.add_heading(name, 0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2 = doc.add_paragraph(f"{role} | {email} | {phone}")
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_heading("SUMMARY", 2)
    doc.add_paragraph(f"Detail-oriented {role} with experience in {skills}.")
    doc.add_heading("SKILLS", 2)
    doc.add_paragraph(skills)
    doc.add_heading("EXPERIENCE", 2)
    doc.add_paragraph(exp)
    doc.add_heading("EDUCATION", 2)
    doc.add_paragraph(edu)
    
    bio = io.BytesIO()
    doc.save(bio)

    # --- PRO PDF MAKER ---
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(30,70,130)
    pdf.rect(0,0,210,35,'F')
    pdf.set_y(10)
    pdf.set_text_color(255,255,255)
    pdf.set_font("Arial","B",20)
    pdf.cell(0,10,name,align='C',ln=True)
    pdf.set_font("Arial","",12)
    pdf.cell(0,8,f"{role} | {email}",align='C',ln=True)
    pdf.set_y(45)
    pdf.set_text_color(0,0,0)
    pdf.set_font("Arial","B",14)
    pdf.cell(0,10,"SUMMARY",ln=True)
    pdf.set_font("Arial","",11)
    pdf.multi_cell(0,7,f"Detail-oriented {role} with skills in {skills}")
    pdf.set_font("Arial","B",14)
    pdf.cell(0,10,"SKILLS",ln=True)
    pdf.set_font("Arial","",11)
    pdf.multi_cell(0,7,skills)
    pdf.set_font("Arial","B",14)
    pdf.cell(0,10,"EXPERIENCE",ln=True)
    pdf.set_font("Arial","",11)
    pdf.multi_cell(0,7,exp)
    pdf.set_font("Arial","B",14)
    pdf.cell(0,10,"EDUCATION",ln=True)
    pdf.set_font("Arial","",11)
    pdf.multi_cell(0,7,edu)
    
    pdf_bio = io.BytesIO(pdf.output(dest='S').encode('latin-1'))

    c1, c2 = st.columns(2)
    with c1:
        st.download_button("📄 DOCX",bio.getvalue(),"Dileep_PRO_Resume.docx")
    with c2:
        st.download_button("📕 PDF",pdf_bio.getvalue(),"Dileep_PRO_Resume.pdf")
