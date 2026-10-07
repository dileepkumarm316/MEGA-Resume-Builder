import streamlit as st
from fpdf import FPDF
from docx import Document
from docx.shared import Pt, RGBColor
import io

st.set_page_config(page_title="Resume PRO MAX", layout="centered")
st.title("🔥 Resume PRO MAX - ATS + AI")

# Templates
template = st.selectbox("Template:", ["Modern Blue", "Classic Black", "Minimal"])

# Inputs
name = st.text_input("Full Name", "Dileep Kumar M")
role = st.text_input("Target Role", "Software Engineer")
email = st.text_input("Email", "dileep@gmail.com")
phone = st.text_input("Phone", "+91 98765 43210")
skills = st.text_area("Skills", "Python, Java, React, SQL")
exp = st.text_area("Experience (Raw)", "Worked on Python projects, improved app")

# Session state for AI
if 'exp' not in st.session_state:
    st.session_state['exp'] = exp
else:
    exp = st.session_state['exp']

# === SMART AI - FREE - NO API NEEDED ===
if st.button("Make PRO with AI 🧠"):
    role_lower = role.lower()

    if "software" in role_lower or "developer" in role_lower or "engineer" in role_lower:
        exp_new = f"• Built scalable applications using {skills.split(',')[0] if ',' in skills else skills} handling 10k+ users\n• Improved system performance by 40% and reduced latency by 25%\n• Led development of 3+ core modules in Agile team of 5"
    elif "marketing" in role_lower or "digital" in role_lower:
        exp_new = "• Increased social media engagement by 150% in 3 months\n• Managed campaigns with 2L+ budget, achieved 3.5x ROI\n• Created content strategy boosting qualified leads by 60%"
    elif "data" in role_lower or "analyst" in role_lower or "science" in role_lower:
        exp_new = "• Analyzed 1M+ records using Python & SQL, built interactive dashboards\n• Built predictive models improving business accuracy by 25%\n• Automated reporting saving 15 hours/week for team"
    elif "design" in role_lower or "ui" in role_lower or "ux" in role_lower:
        exp_new = "• Designed 50+ UI screens improving user experience by 35%\n• Created brand guidelines and reusable design systems\n• Collaborated with devs to ship 10+ features on time"
    elif "sales" in role_lower or "business" in role_lower:
        exp_new = "• Achieved 120% of sales target for 3 consecutive quarters\n• Built client relationships generating 50L+ revenue\n• Negotiated deals closing 20+ enterprise clients"
    else:
        exp_new = f"• Delivered high-quality work as {role} using {skills.split(',')[0] if ',' in skills else skills}\n• Improved process efficiency by 30% through innovative solutions\n• Collaborated with cross-functional teams to achieve business goals"

    st.session_state['exp'] = exp_new
    st.success(f"AI rewrote for {role}! 🔥 Check Final Exp below")
    st.balloons()
    st.rerun()

# Final Exp Box
final_exp = st.text_area("Final Experience (AI Generated - Editable)", value=st.session_state['exp'], height=150)

# Color logic
if "Blue" in template:
    header_color = (0, 102, 204)
    header_rgb = RGBColor(0, 102, 204)
else:
    header_color = (0, 0, 0)
    header_rgb = RGBColor(0, 0, 0)

# Generate
if st.button("Generate PRO MAX 🚀"):
    # PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(header_color[0], header_color[1], header_color[2])
    pdf.rect(0, 0, 210, 40, 'F')
    pdf.set_y(10)
    pdf.set_text_color(255,255,255)
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(0, 10, name, align='C', ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 8, f"{role} | {email} | {phone}", align='C', ln=True)
    pdf.set_y(50)
    pdf.set_text_color(0,0,0)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "SKILLS", ln=True)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, skills)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "EXPERIENCE", ln=True)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, final_exp)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "EDUCATION", ln=True)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, "B.E. Computer Science - 2024")

    pdf_bytes = pdf.output(dest='S').encode('latin-1')

    # DOCX
    doc = Document()
    p = doc.add_paragraph()
    p.alignment = 1
    run = p.add_run(f"{name}\n")
    run.bold = True
    run.font.size = Pt(20)
    run.font.color.rgb = header_rgb
    run2 = p.add_run(f"{role} | {email} | {phone}")
    run2.font.size = Pt(11)

    doc.add_heading('SKILLS', 2)
    doc.add_paragraph(skills)
    doc.add_heading('EXPERIENCE', 2)
    doc.add_paragraph(final_exp)
    doc.add_heading('EDUCATION', 2)
    doc.add_paragraph("B.E. Computer Science - 2024")

    doc_io = io.BytesIO()
    doc.save(doc_io)

    st.success("Ready da thalaiva! 🔥")
    st.download_button("Download PDF", pdf_bytes, f"{name}_Resume.pdf", "application/pdf")
    st.download_button("Download DOCX", doc_io.getvalue(), f"{name}_Resume.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")