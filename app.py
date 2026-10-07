import streamlit as st
from docx import Document
from fpdf import FPDF
import io
from PIL import Image

st.set_page_config(page_title="Resume PRO MAX")
st.title("🚀 Resume PRO MAX")
st.write("By Dileep - 3 Templates + Photo + AI")

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Name","Dileep Kumar M")
    role = st.text_input("Role","Software Engineer")
with col2:
    email = st.text_input("Email","dileep@gmail.com")
    phone = st.text_input("Phone","+91 98765")

# NEW FEATURE 1: TEMPLATE SELECTION
template = st.selectbox("Choose Template", ["🔵 PRO Blue", "⚫ Executive Black", "✨ Minimal White"])

# NEW FEATURE 2: PHOTO UPLOAD
photo = st.file_uploader("Upload Photo (Optional)", type=["jpg","png","jpeg"])

skills = st.text_area("Skills","Python, Java, SQL, AWS, React")
exp_raw = st.text_area("Experience (Normal) ", "Worked as Software Engineer")
edu = st.text_area("Education","B.Tech CSE - Anna University - 2022")

# NEW FEATURE 3: AI BULLET BUTTON
if st.button("✨ Make My Experience PRO with AI"):
    # AI style rewriting (without API key)
    if "Software" in exp_raw:
        exp = "• Built scalable applications using Python & Java\n• Improved system performance by 30%\n• Collaborated with cross-functional teams"
    else:
        exp = f"• {exp_raw}\n• Achieved 95% client satisfaction\n• Led project development end-to-end"
    st.session_state['exp_ai'] = exp
    st.success("AI rewrote your experience! Check below")

exp = st.text_area("Final Experience (AI PRO)", value=st.session_state.get('exp_ai', exp_raw), height=120)

if st.button("Generate PRO MAX Resume", type="primary"):
    
    # Color based on template
    if "Blue" in template:
        r,g,b = 37,99,235
    elif "Black" in template:
        r,g,b = 20,20,20
    else:
        r,g,b = 255,255,255

    # DOCX
    doc = Document()
    doc.add_heading(name,0)
    doc.add_paragraph(f"{role} | {email} | {phone} | Template: {template}")
    doc.add_heading("SKILLS",2)
    doc.add_paragraph(skills)
    doc.add_heading("EXPERIENCE",2)
    doc.add_paragraph(exp)
    doc.add_heading("EDUCATION",2)
    doc.add_paragraph(edu)
    b1 = io.BytesIO()
    doc.save(b1)

    # PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Header color
    if "White" not in template:
        pdf.set_fill_color(r,g,b)
        pdf.rect(0,0,210,38,'F')
        pdf.set_text_color(255,255,255)
    else:
        pdf.set_fill_color(240,240,240)
        pdf.rect(0,0,210,38,'F')
        pdf.set_text_color(0,0,0)
    
    pdf.set_y(10)
    pdf.set_font("Arial","B",16)
    pdf.cell(0,10,name,align='C',ln=True)
    pdf.set_font("Arial","",10)
    pdf.cell(0,8,f"{role} | {email} | {phone}",align='C',ln=True)
    
    pdf.set_y(45)
    pdf.set_text_color(0,0,0)
    pdf.set_x(15)
    
    def add_sec