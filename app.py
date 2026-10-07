import streamlit as st
from docx import Document
from fpdf import FPDF
import io

st.set_page_config(page_title="AI Resume PRO - FINAL")

st.markdown("## 🚀 AI Resume PRO - FINAL")
st.markdown("Build by Dileep - ATS Ready")

# --- INPUTS ---
name = st.text_input("Full Name", "Dileep Kumar M")
role = st.text_input("Role / Title", "Software Engineer")
email = st.text_input("Email", "dileep@gmail.com")
phone = st.text_input("Phone", "+91 98765 43210")
skills = st.text_area("Skills", "Python, Java, SQL, AWS, React")
exp = st.text_area("Experience", "Software Engineer at TechCorp - Building AI apps")
edu = st.text_input("Education", "B.Tech CSE - Anna University - 2022")

if st.button("Generate PRO Resume", type="primary"):
    st.success("✅ PRO Resume Ready! Dileep!")

    # ========== DOCX ==========
    doc = Document()
    title = doc.add_heading(name, 0)
    doc.add_paragraph(f"{role} | {email} | {phone}")
    
    doc.add_heading("SKILLS", level=2)
    doc.add_paragraph(skills)
    
    doc.add_heading("EXPERIENCE", level=2)
    doc.add_paragraph(exp)
    
    doc.add_heading("EDUCATION", level=2)
    doc.add_paragraph(edu)
    
    bio_doc = io.BytesIO()
    doc.save(bio_doc)

    # ========== PDF - NO CUT FIX ==========
    pdf = FPDF()
    pdf.add_page()
    
    # Blue Header
    pdf.set_fill_color(37, 99, 235)
    pdf.rect(0, 0, 210, 35, 'F')
    
    pdf.set_y(10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, name, align='C', ln=True)
    
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 7, f"{role} | {email}", align='C', ln=True)
    
    # Body
    pdf.set_y(45)
    pdf.set_text_color(0, 0, 0)
    
    pdf.set_x(15)
    pdf.set_font("Arial", "B", 13)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(180, 10, "SKILLS", ln=True)
    
    pdf.set_x(15)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(180, 7, skills)
    
    pdf.ln(3)
    pdf.set_x(15)
    pdf.set_font("Arial", "B", 13)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(180, 10, "EXPERIENCE", ln=True)
    
    pdf.set_x(15)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(180, 7, exp)
    
    pdf.ln(3)
    pdf.set_x(15)
    pdf.set_font("Arial", "B", 13)
    pdf.set_text_color(