import streamlit as st
from fpdf import FPDF
import re

st.set_page_config(page_title="Resume AI - MEGA", page_icon="🚀", layout="centered")

if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'final_exp' not in st.session_state:
    st.session_state['final_exp'] = "- Built scalable applications using Python handling 10k+ users\n- Improved system performance by 40% and reduced latency by 25%\n- Led development of 3+ modules in Agile team of 5"

# SIDEBAR - CLEAN
with st.sidebar:
    st.title("Login")
    if not st.session_state['logged_in']:
        u = st.text_input("Username", "dileep")
        p = st.text_input("Password", type="password", value="1234")
        if st.button("Login"):
            st.session_state['logged_in'] = True
            st.rerun()
    else:
        st.success("Welcome Dileep 👋")
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()
    st.divider()
    theme = st.radio("Theme", ["Light", "Dark"])
    st.divider()
    st.caption("100% Free & Open Source ❤️")

if theme == "Dark":
    st.markdown("<style>.stApp{background:#0e1117}</style>", unsafe_allow_html=True)

st.title("🚀 AI Resume Builder")
st.caption("100% FREE - No API Key Needed")

t1, t2, t3, t4, t5, t6 = st.tabs(["Builder", "Parser", "Matcher", "Cover Letter", "Interview", "Portfolio"])

with t1:
    name = st.text_input("Full Name", "Dileep Kumar M")
    role = st.text_input("Role", "Software Engineer")
    email = st.text_input("Email", "dileep@gmail.com")
    phone = st.text_input("Phone", "+91 98765 43210")
    skills = st.text_input("Skills", "Python, React, SQL, AWS")
    linkedin = st.text_input("LinkedIn", "linkedin.com/in/dileep")
    raw = st.text_area("Your Experience Rough", "worked on python project made app faster")

    if st.button("✨ Enhance + Grammar Fix", type="primary"):
        fixed = raw.replace("i ", "I ").replace("python","Python").strip().capitalize()
        fs = skills.split(',')[0] if skills else "Python"
        enhanced = f"- Built scalable applications using {fs} handling 10k+ users\n- Improved system performance by 40% and reduced latency by 25%\n- Led development of 3+ modules in Agile team of 5"
        st.session_state['final_exp'] = enhanced
        st.success(f"Fixed: {fixed}")
        st.code(f"Enhanced: {enhanced}")
        st.balloons()

    final_exp = st.text_area("Final Experience", value=st.session_state['final_exp'], height=150)

    if st.button("Generate PDF"):
        safe_exp = final_exp.replace("•", "-").encode('latin-1', 'ignore').decode('latin-1')
        safe_name = name.encode('latin-1', 'ignore').decode('latin-1')
        safe_role = role.encode('latin-1', 'ignore').decode('latin-1')
        safe_skills = skills.encode('latin-1', 'ignore').decode('latin-1')

        pdf = FPDF(); pdf.add_page()
        pdf.set_font("Arial",'B',20); pdf.cell(0,10,safe_name,ln=True,align='C')
        pdf.set_font("Arial",'',10); pdf.cell(0,6,f"{safe_role} | {email} | {phone}",ln=True,align='C')
        pdf.ln(8); pdf.set_font("Arial",'B',12); pdf.cell(0,8,"SKILLS",ln=True)
        pdf.set_font("Arial",'',10); pdf.multi_cell(0,6,safe_skills)
        pdf.set_font("Arial",'B',12); pdf.cell(0,8,"EXPERIENCE",ln=True)
        pdf.set_font("Arial",'',10); pdf.multi_cell(0,6,safe_exp)
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        st.download_button("⬇️ Download PDF", pdf_bytes, "resume.pdf", "application/pdf", type="primary")

with t2:
    st.subheader("📄 Parser")
    up = st.file_uploader("Upload PDF/TXT", type=['pdf','txt'])
    if up:
        txt = up.read().decode('utf-8', errors='ignore')[:1000]
        st.text_area("Parsed", txt, height=150)

with t3:
    st.subheader("🎯 Job Matcher")
    jd = st.text_area("Paste JD", "Looking for Python, React, SQL...")
    if st.button("Check Match"):
        jd_w = set(re.findall(r'\w+', jd.lower()))
        res_w = set(re.findall(r'\w+', (skills + " " + final_exp).lower()))
        match = min(95, int(len(res_w.intersection(jd_w))/max(len(jd_w),1)*100)+45)
        st.progress(match/100); st.metric("Match", f"{match}%")

with t4:
    st.subheader("✉️ Cover Letter")
    comp = st.text_input("Company", "Google")
    if st.button("Generate Cover Letter"):
        first = final_exp.split("\n")[0].replace("-","").strip()
        cl = f"Dear Hiring Manager at {comp},\n\nI am excited to apply for {role}. With expertise in {skills}, I {first}.\n\nBest,\n{name}"
        st.text_area("Cover Letter", cl, height=200)

with t5:
    st.subheader("🎤 Interview Q&A")
    if st.button("Generate Questions"):
        st.text_area("Q&A", f"Q: Tell me about {skills.split(',')[0]}?\nA: {final_exp.split(chr(10))[0]}", height=200)

with t6:
    st.subheader("🌐 Portfolio & Salary")
    if st.button("Generate Portfolio"):
        html = f"<html><body style='padding:40px'><h1>{name}</h1><h3>{role}</h3><p>{skills}</p><p>{final_exp.replace(chr(10),'<br>')}</p></body></html>"
        st.download_button("Download portfolio.html", html, "portfolio.html", "text/html", type="primary")
    if st.button("Predict Salary"):
        base = 4.5 + (2.5 if "python" in skills.lower() else 0)
        st.metric("CTC", f"Rs {base:.1f} - {base+3.5:.1f} LPA")

st.caption("Built by Dileep | 100% FREE")