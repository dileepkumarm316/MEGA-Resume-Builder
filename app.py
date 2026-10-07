import streamlit as st
from fpdf import FPDF
import re

st.set_page_config(page_title="Resume AI - MEGA", page_icon="🚀", layout="centered")

if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'final_exp' not in st.session_state: st.session_state['final_exp'] = "• Built scalable apps using Python handling 10k+ users\n• Improved performance by 40% and reduced latency by 25%"

# SIDEBAR
with st.sidebar:
    st.title("🔐 Login")
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
    if st.button("💳 Unlock Pro ₹99"):
        st.balloons()
        st.success("Pro Unlocked!")

if theme == "Dark":
    st.markdown("<style>.stApp{background:#0e1117}</style>", unsafe_allow_html=True)

st.title("🚀 AI Resume Builder - MEGA ULTRA")
st.caption("Builder | Parser | Grammar Fix | Templates | Job Matcher | Cover Letter | Interview | Portfolio | Salary")

t1, t2, t3, t4, t5, t6 = st.tabs(["Builder", "Parser", "Matcher", "Cover Letter", "Interview", "Portfolio & Salary"])

with t1:
    api = st.text_input("OpenAI Key (Optional)", type="password", placeholder="sk-... - illana dummy AI")
    name = st.text_input("Full Name", "Dileep Kumar M")
    role = st.text_input("Role", "Software Engineer")
    email = st.text_input("Email", "dileep@gmail.com")
    phone = st.text_input("Phone", "+91 98765 43210")
    skills = st.text_input("Skills", "Python, React, SQL, AWS")
    linkedin = st.text_input("LinkedIn", "linkedin.com/in/dileep")
    raw = st.text_area("Your Experience Rough", "worked on python project made app faster")

    if st.button("✨ Enhance + Grammar Fix", type="primary"):
        fixed = raw.replace("i ", "I ").replace("python","Python").strip().capitalize()
        fs = skills.split(',')[0]
        enhanced = f"• Built scalable applications using {fs} handling 10k+ users\n• Improved system performance by 40% and reduced latency by 25%\n• Led development of 3+ modules in Agile team of 5"
        st.session_state['final_exp'] = enhanced
        st.code(f"Fixed: {fixed}")
        st.code(f"Enhanced: {enhanced}")
        st.balloons()

    final_exp = st.text_area("Final Experience", value=st.session_state['final_exp'], height=150)

    if st.button("Generate PDF"):
        pdf = FPDF(); pdf.add_page()
        pdf.set_font("Arial",'B',20); pdf.cell(0,10,name,ln=True,align='C')
        pdf.set_font("Arial",'',10); pdf.cell(0,6,f"{role} | {email} | {phone}",ln=True,align='C')
        pdf.ln(8); pdf.set_font("Arial",'B',12); pdf.cell(0,8,"SKILLS",ln=True)
        pdf.set_font("Arial",'',10); pdf.multi_cell(0,6,skills)
        pdf.set_font("Arial",'B',12); pdf.cell(0,8,"EXPERIENCE",ln=True)
        pdf.set_font("Arial",'',10); pdf.multi_cell(0,6,final_exp)
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        st.download_button("⬇️ Download PDF", pdf_bytes, "resume.pdf", "application/pdf", type="primary")

with t2:
    st.subheader("📄 Parser - Old Resume Upload")
    up = st.file_uploader("Upload PDF/TXT", type=['pdf','txt'])
    if up:
        txt = up.read().decode('utf-8', errors='ignore')[:1000]
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', txt)
        if emails: st.write(f"Email: {emails[0]}")
        st.text_area("Parsed", txt, height=150)
        if st.button("Auto Fill"):
            st.session_state['final_exp'] = txt[:200]
            st.success("Filled!")

    st.divider()
    sent = st.text_input("Grammar Test", "i worked on python project")
    if st.button("Fix Grammar"):
        fixed = sent.replace("i ","I ").replace("python","Python").capitalize() + "."
        st.success(fixed)

with t3:
    st.subheader("🎯 Job Matcher")
    jd = st.text_area("Paste JD", "Looking for Python, React, SQL...")
    if st.button("Check Match"):
        jd_w = set(re.findall(r'\w+', jd.lower()))
        res_w = set(re.findall(r'\w+', (skills + " " + final_exp).lower()))
        common = jd_w.intersection(res_w)
        match = min(95, int(len(common)/max(len(jd_w),1)*100)+45)
        st.progress(match/100); st.metric("Match", f"{match}%")
        miss = list(jd_w - res_w)[:8]
        if miss: st.warning(f"Add: {', '.join(miss)}")

with t4:
    st.subheader("✉️ Cover Letter + Cold Email")
    comp = st.text_input("Company", "Google")
    recruiter = st.text_input("Recruiter", "Hiring Manager")
    if st.button("Generate Cover Letter & Email"):
        cl = f"Dear Hiring Manager at {comp},\n\nI am excited to apply for {role}. With expertise in {skills}, I {final_exp.split(chr(10))[0].replace('•','').strip()}.\n\nEager to contribute to {comp}.\n\nBest,\n{name}\n{email} | {phone}"
        ce = f"Subject: {role} at {comp} - {name}\n\nHi {recruiter},\n\nSaw opening for {role} at {comp}. I have skills in {skills} and {final_exp.split(chr(10))[0].replace('•','').strip().lower()}.\n\nResume attached (ATS 100/100). Portfolio: {linkedin}\n\nBest,\n{name}"
        st.text_area("Cover Letter", cl, height=200)
        st.text_area("Cold Email", ce, height=200)

with t5:
    st.subheader("🎤 Interview Q&A")
    if st.button("Generate Questions"):
        qa = f"""Q1: Tell me about {skills.split(',')[0]} project handling 10k users?
Ans: Use STAR method, mention {final_exp.split(chr(10))[0]}

Q2: How did you improve performance by 40%?
Ans: Profiling, caching, indexing

Q3: Why {comp if 'comp' in locals() else 'this company'}?
Ans: Align your {role} skills with company mission"""
        st.text_area("Q&A", qa, height=250)

with t6:
    st.subheader("🌐 Portfolio Website")
    if st.button("Generate Portfolio"):
        html = f"<html><body style='font-family:Arial; padding:40px'><h1>{name}</h1><h3>{role}</h3><p>{email} | {phone}</p><p>{skills}</p><p>{final_exp.replace(chr(10),'<br>')}</p></body></html>"
        st.download_button("Download portfolio.html", html, "portfolio.html", "text/html", type="primary")

    st.divider()
    st.subheader("💰 Salary Predictor Chennai 2026")
    if st.button("Predict Salary"):
        base = 4.5
        if "python" in skills.lower(): base+=2.5
        if "react" in skills.lower(): base+=1.5
        if "aws" in skills.lower(): base+=2
        st.metric("CTC", f"₹ {base:.1f} - {base+3.5:.1f} LPA")
        st.progress(min(90, int(base*8))/100)

st.caption("Built by Dileep | MEGA ULTRA | All Features Included")