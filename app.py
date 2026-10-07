import streamlit as st
from docx import Document
from fpdf import FPDF
import io

st.set_page_config(page_title="Resume PRO MAX")
st.title("🚀 Resume PRO MAX")
st.write("By Dileep")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Name","Dileep Kumar M")
    role = st.text_input("Role","Software Engineer")
with col2:
    email = st.text_input("Email","dileep@gmail.com")
    phone = st.text_input("Phone","+91 98765")

template = st.selectbox("Template", ["PRO Blue", "Executive Black", "Minimal White"])

skills = st.text_area("Skills","Python, Java, SQL")
exp_raw = st.text_area("Experience", "Worked as Software Engineer")

if st.button("Make PRO with AI"):
    exp_new = "• Built scalable apps using Python & Java\n• Improved performance by 30%\n• Led team of 3 developers"
    st.session_state['exp'] = exp_new
    st.success("AI Rewrote!")

exp = st.text_area("Final Exp", value=st.session_state.get('exp', exp_raw))
edu = st.text_input("Education","B.Tech CSE")

if st.button("Generate PRO MAX", type="primary"):
    if "Blue" in template:
        r,g,b = 37,99,235
    elif "Black" in template:
        r,g,b = 20,20,20
    else:
        r,g,b = 200,200,200

    doc = Document()
    doc.add_heading(name,0)
    doc.add_paragraph(f"{role} | {email} | {phone}")
    doc.add_heading("SKILLS",2)
    doc.add_paragraph(skills)
    doc.add_heading("EXPERIENCE",2)
    doc.add_paragraph(exp)
    doc.add_heading("EDUCATION",2)
    doc.add_paragraph(edu)
    b1 = io.BytesIO()
    doc.save(b1)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(r,g,b)
    pdf.rect(0,0,210,38,'F')
    
    if "White" in template:
        pdf.set_text_color(0,0,0)
    else:
        pdf.set_text_color(255,255,255)
        
    pdf.set_y(10)
    pdf.set_font("Arial","B",16)
    pdf.cell(0,10,name,align='C',ln=True)
    pdf.set_font("Arial","",10)
    pdf.cell(0,8,role,align='C',ln=True)
    pdf.cell(0,8,email,align='C',ln=True)
    
    pdf.set_y(45)
    pdf.set_text_color(0,0,0)
    pdf.set_x(15)
    pdf.set_font("Arial","B",12)
    pdf.cell(0,10,"SKILLS",ln=True)
    pdf.set_x(15)
    pdf.set_font("Arial","",10)
    pdf.multi_cell(180,6,skills)
    pdf.ln(2)
    
    pdf.set_x(15)
    pdf.set_font("Arial","B",12)
    pdf.cell(0,10,"EXPERIENCE",ln=True)
    pdf.set_x(15)
    pdf.set_font("Arial","",10)
    pdf.multi_cell(180,6,exp)
    pdf.ln(2)
    
    pdf.set_x(15)
    pdf.set_font("Arial","B",12)
    pdf.cell(0,10,"EDUCATION",ln=True)
    pdf.set_x(15)
    pdf.set_font("Arial","",10)
    pdf.multi_cell(180,6,edu)

    out = pdf.output()
    b2 = io.BytesIO(out)

    st.success("Ready!")
    st.download_button("DOCX", b1.getvalue(), "resume.docx")
    st.download_button("PDF", b2.getvalue(), "resume.pdf")
    st.balloons()