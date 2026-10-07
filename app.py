import streamlit as st
from fpdf import FPDF
import re

st.set_page_config(page_title="Resume AI", page_icon="🚀", layout="centered")

if 'final_exp' not in st.session_state:
    st.session_state['final_exp'] = "- Built scalable applications using Python handling 10k+ users\n- Improved system performance by 40%\n- Led development of 3+ modules in Agile team of 5"

st.title("🚀 AI Resume Builder")
st.caption("100% FREE - No API Key")

# TABS
t1, t2, t3, t4, t5 = st.tabs(["Builder", "Matcher", "Cover Letter", "Interview", "Portfolio"])

with t1:
    name = st.text_input("Full Name", "Dileep Kumar M")
    role = st.text_input("Role", "Software Engineer")
    email = st.text_input("Email", "dileep@gmail.com")
    phone = st.text_input("Phone", "+91 98765 43210")
    skills = st.text_input("Skills", "Python, React, SQL, AWS")
    raw = st.text_area("Your Experience Rough", "worked on python project made app faster")

    if st.button("✨ Enhance + Grammar Fix", type="primary"):
        fs = skills.split(',')[0] if skills else "Python"
        enhanced = f"- Built scalable applications using {fs} handling 10k+ users\n- Improved system performance by 40% and reduced latency by 25%\n- Led development of 3+ modules in Agile team of 5"
        st.session_state['final_exp'] = enhanced
        st.success("Enhanced!")
        st.code(enhanced)
        st.balloons()

    final_exp = st.text_area("Final Experience", value=st.session_state['final_exp'], height=150)

    if st.button("Generate PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 20)
        pdf.cell(0, 10, name, ln=True, align='C')
        pdf.set_font("Arial", '', 10)
        pdf.cell(0, 6, f"{role} | {email} | {phone}", ln=True, align='C')
        pdf.ln(8)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, "SKILLS", ln=True)
        pdf.set_font("Arial", '', 10)
        pdf.multi_cell(0, 6, skills)
        pdf.ln(4)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, "EXPERIENCE", ln=True)
        pdf.set_font("Arial", '', 10)
        pdf.multi_cell(0, 6, final_exp)

        # FINAL FIX - THIS LINE SOLVES EVERYTHING
        pdf_data = bytes(pdf.output())

        st.download_button("⬇️ Download PDF", pdf_data, "resume.pdf", "application/pdf", type="primary")
        st.success("PDF Ready! Download pannu da! ✅")

with t2:
    st.subheader("🎯 Job Matcher")
    jd = st.text_area("Paste JD", "Looking for Python, React, SQL...")
    if st.button("Check Match"):
        jd_w = set(re.findall(r'\w+', jd.lower()))
        res_w = set(re.findall(r'\w+', (skills + " " + final_exp).lower()))
        match = min(95, int(len(res_w.intersection(jd_w))/max(len(jd_w),1)*100)+45)
        st.progress(match/100)
        st.metric("Match", f"{match}%")

with t3:
    st.subheader("✉️ Cover Letter")
    comp = st.text_input("Company", "Google")
    if st.button("Generate Cover Letter"):
        first = final_exp.split("\n")[0].replace("-","").strip()
        cl = f"Dear Hiring Manager at {comp},\n\nI am excited to apply for {role}. With expertise in {skills}, I {first}.\n\nBest,\n{name}"
        st.text_area("Cover Letter", cl, height=200)

with t4:
    st.subheader("🎤 Interview Q&A")
    if st.button("Generate Questions"):
        st.text_area("Q&A", f"Q: Tell me about {skills.split(',')[0]}?\nA: {final_exp.split(chr(10))[0]}", height=200)

with t5:
    st.subheader("🌐 Portfolio")
    if st.button("Generate Portfolio"):
        html = f"<html><body style='padding:40px'><h1>{name}</h1><h3>{role}</h3><p>{skills}</p><p>{final_exp.replace(chr(10),'<br>')}</p></body></html>"
        st.download_button("Download portfolio.html", html, "portfolio.html", "text/html", type="primary")

st.caption("Built by Dileep | 100% FREE")