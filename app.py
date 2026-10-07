import streamlit as st
from fpdf import FPDF
from docx import Document
from docx.shared import Pt, RGBColor
import io

st.set_page_config(page_title="Resume PRO MAX", layout="centered")
st.title("🔥 Resume PRO MAX - ATS + AI")

template = st.selectbox("Template:", ["Modern Blue", "Classic Black", "Minimal"])
name = st.text_input("Full Name", "Dileep Kumar M")
role = st.text_input("Target Role", "Software Engineer")
email = st.text_input("Email", "dileep@gmail.com")
phone = st.text_input("Phone", "+91 98765 43210")
skills = st.text_area("Skills", "Python, Java, React, SQL")
raw_exp = st.text_area("Experience (Raw)", "Worked on Python projects, improved app")

if 'final_exp' not in st.session_state:
    st.session_state['final_exp'] = "• Built scalable applications using Python handling 10k+ users\n• Improved system performance by 40% and reduced latency by 25%\n• Led development of 3+ core modules in Agile team of 5"

if st.button("Make PRO with AI 🧠"):
    r = role.lower()
    first_skill = skills.split(',')[0] if ',' in skills else skills
    if "software" in r or "developer" in r or "engineer" in r:
        new_exp = f"• Built scalable applications using {first_skill} handling 10k+ users\n• Improved system performance by 40% and reduced latency by 25%\n• Led development of 3+ core modules in Agile team of 5"
    elif "marketing" in r or "digital" in r:
        new_exp = "• Increased social media engagement by 150% in 3 months\n• Managed campaigns with 2L+ budget, achieved 3.5x ROI\n• Created content strategy boosting qualified leads by 60%"
    elif "data" in r or "analyst" in r:
        new_exp = "• Analyzed 1M+ records using Python & SQL, built dashboards\n• Built predictive models improving accuracy by 25%\n• Automated reports saving 15 hours/week"
    elif "design" in r or "ui" in r:
        new_exp = "• Designed 50+ UI screens improving UX by 35%\n• Created brand guidelines and design systems\n• Collaborated with devs to ship 10+ features"
    else:
        new_exp = f"• Delivered high-quality work as {role} using {first_skill}\n• Improved process efficiency by 30% through innovation\n• Collaborated with teams to achieve goals"
    st.session_state['final_exp'] = new_exp
    st.success(f"AI rewrote for {role}! 🔥")
    st.balloons()

final_exp = st.text_area("Final Experience (AI Generated - Editable)", value=st.session_state['final_exp'], height=160)

# ATS SCORE
def check_ats():
    score = 0
    tips = []
    if "@" in email and "." in email: score += 20
    else: tips.append("❌ Add proper Email")
    if len(phone) >= 10: score += 10
    if len(skills.split(',')) >= 3: score += 20
    else: tips.append("❌ Add 3+ skills with comma")
    if any(c in final_exp for c in ["%", "10k", "1M", "+"]): score += 20
    else: tips.append("❌ Add numbers like 40%, 10k+ in exp")
    if any(v in final_exp.lower() for v in ["built","improved","led","managed"]): score += 15
    else: tips.append("❌ Use action verbs: Built, Led")
    if len(final_exp) > 100: score += 15
    else: tips.append("❌ Write 3 bullets minimum")
    return score, tips

if st.button("Check ATS Score 📊"):
    score, tips = check_ats()
    st.progress(score/100)
    if score >= 80: st.success(f"ATS Score: {score}/100 - MASS DA! Ready to apply 🔥")
    elif score >= 50:
        st.warning(f"ATS Score: {score}/100 - Okay da, improve pannalam")
        for t in tips: st.write(t)
    else:
        st.error(f"ATS Score: {score}/100 - Work pannanum da")
        for t in tips: st.write(t)

# PDF/DOCX
if "Blue" in template: header_color = (0, 102, 204); header_rgb = RGBColor(0, 102, 204)
else: header_color = (0, 0, 0); header_rgb = RGBColor(0, 0, 0)

if st.button("Generate PRO MAX 🚀"):
    pdf = FPDF(); pdf.add_page()
    pdf.set_fill_color(header_color[0], header_color[1], header_color[2])
    pdf.rect(0, 0, 210, 40, 'F')
    pdf.set_y(10); pdf.set_text_color(255,255,255)
    pdf.set_font("Arial", 'B', 24); pdf.cell(0, 10, name, align='C', ln=True)
    pdf.set_font("Arial", '', 12); pdf.cell(0, 8, f"{role} | {email} | {phone}", align='C', ln=True)
    pdf.set_y(50); pdf.set_text_color(0,0,0)
    pdf.set_font("Arial", 'B', 14); pdf.cell(0, 10, "SKILLS", ln=True)
    pdf.set_font("Arial", '', 11); pdf.multi_cell(0, 7, skills)
    pdf.set_font("Arial", 'B', 14); pdf.cell(0, 10, "EXPERIENCE", ln=True)
    pdf.set_font("Arial", '', 11); pdf.multi_cell(0, 7, final_exp)
    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    doc = Document(); p = doc.add_paragraph(); p.alignment = 1
    run = p.add_run(f"{name}\n"); run.bold = True; run.font.size = Pt(20); run.font.color.rgb = header_rgb
    run2 = p.add_run(f"{role} | {email} | {phone}"); run2.font.size = Pt(11)
    doc.add_heading('SKILLS', 2); doc.add_paragraph(skills)
    doc.add_heading('EXPERIENCE', 2); doc.add_paragraph(final_exp)
    doc.add_heading('EDUCATION', 2); doc.add_paragraph("B.E. Computer Science - 2024")
    doc_io = io.BytesIO(); doc.save(doc_io)
    st.success("Ready da! 🔥")
    st.download_button("Download PDF", pdf_bytes, f"{name}_Resume.pdf", "application/pdf")
    st.download_button("Download DOCX", doc_io.getvalue(), f"{name}_Resume.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")