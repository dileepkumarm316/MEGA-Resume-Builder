import streamlit as st
from fpdf import FPDF
import re

st.set_page_config(page_title="Resume AI - Mega", page_icon="🚀", layout="centered")

# ✅ UN UPI - KASU DIRECT AH UN ACCOUNT KU VARUM
MY_UPI_ID = "dileepkumar.m316@okicici"

if 'final_exp' not in st.session_state:
    st.session_state['final_exp'] = "- Built scalable applications using Python handling 10k+ users\n- Improved system performance by 40%\n- Led development of 3+ modules in Agile team of 5"

st.title("🚀 AI Resume Builder - MEGA")
st.caption("100% FREE - 8 Features!")

t1, t2, t3, t4, t5, t6, t7, t8 = st.tabs(["Builder","ATS Score","Matcher","Cover Letter","Interview","LinkedIn","Portfolio","💰 Salary"])

with t1:
    name = st.text_input("Full Name", "Dileep Kumar M")
    role = st.text_input("Role", "Software Engineer")
    email = st.text_input("Email", "dileep@gmail.com")
    phone = st.text_input("Phone", "+91 98765 43210")
    skills = st.text_input("Skills", "Python, React, SQL, AWS, Docker")
    if st.button("✨ Enhance", type="primary"):
        fs = skills.split(',')[0]
        st.session_state['final_exp'] = f"- Built scalable applications using {fs} handling 10k+ users\n- Improved system performance by 40%\n- Led development of 3+ modules in Agile team of 5"
        st.code(st.session_state['final_exp']); st.balloons()
    final_exp = st.text_area("Final Experience", value=st.session_state['final_exp'], height=150)
    if st.button("Generate PDF"):
        pdf = FPDF(); pdf.add_page()
        pdf.set_font("Arial", 'B', 20); pdf.cell(0, 10, name, ln=True, align='C')
        pdf.set_font("Arial", '', 10); pdf.cell(0, 6, f"{role} | {email} | {phone}", ln=True, align='C'); pdf.ln(8)
        pdf.set_font("Arial", 'B', 12); pdf.cell(0, 8, "SKILLS", ln=True)
        pdf.set_font("Arial", '', 10); pdf.multi_cell(0, 6, skills); pdf.ln(4)
        pdf.set_font("Arial", 'B', 12); pdf.cell(0, 8, "EXPERIENCE", ln=True)
        pdf.set_font("Arial", '', 10); pdf.multi_cell(0, 6, final_exp)
        pdf_data = bytes(pdf.output())
        c1, c2 = st.columns(2)
        with c1: st.download_button("⬇️ Download PDF", pdf_data, "resume.pdf", "application/pdf", type="primary")
        with c2:
            wa_text = f"Hi, I'm {name} - {role}. Skills: {skills}"
            st.link_button("📱 WhatsApp Share", f"https://wa.me/?text={wa_text.replace(' ', '%20')}")
        st.success("PDF Ready! ✅")

with t2:
    st.subheader("🎯 ATS Score Checker")
    if st.button("Check ATS Score", type="primary"):
        score = 50; fb = []
        if len(skills.split(',')) >= 4: score += 15
        else: fb.append("❌ Add 5+ skills")
        if len(final_exp) > 150: score += 15
        else: fb.append("❌ Experience too short")
        if "python" in (skills+final_exp).lower(): score += 10
        if "built" in final_exp.lower(): score += 10
        else: fb.append("❌ Use action words: Built, Improved")
        score = min(95, score)
        st.metric("ATS SCORE", f"{score}/100"); st.progress(score/100)
        if score >= 80: st.success("🔥 SEMMA DA! Shortlist aayidum!")
        elif score >= 60: st.warning("Decent da")
        else: st.error("Low da")
        for f in fb: st.write(f)
        if not fb: st.write("✅ Top 10% resume!")

with t3:
    st.subheader("🎯 Job Matcher")
    jd = st.text_area("Paste JD", "Looking for Python, React, SQL...")
    if st.button("Check Match"):
        jd_w = set(re.findall(r'\w+', jd.lower())); res_w = set(re.findall(r'\w+', (skills+" "+final_exp).lower()))
        match = min(95, int(len(res_w.intersection(jd_w))/max(len(jd_w),1)*100)+45)
        st.progress(match/100); st.metric("Match", f"{match}%")

with t4:
    st.subheader("✉️ Cover Letter")
    comp = st.text_input("Company", "Google")
    if st.button("Generate Cover Letter"):
        first = final_exp.split("\n")[0].replace("-", "").strip()
        cl = f"Dear Hiring Manager at {comp},\n\nI am excited to apply for {role}. With {skills}, I {first}.\n\nBest,\n{name}"
        st.text_area("Cover Letter", cl, height=250)

with t5:
    st.subheader("🎤 10 Interview Q&A")
    if st.button("Generate 10 Q&A"):
        qa = f"Q1: Tell me about yourself?\nA: I am {name}, {role} skilled in {skills}\n\nQ2: Project?\nA: {final_exp.split(chr(10))[0]}\n\nQ3: 40% how?\nA: Caching\n\nQ4: Agile?\nA: Sprints\n\nQ5: Why hire?\nA: {skills}\n\nQ6-Q10: Ready!"
        st.text_area("10 Q&A", qa, height=400)

with t6:
    st.subheader("💼 LinkedIn Optimizer")
    if st.button("Optimize LinkedIn"):
        opt = f"🚀 {role} | {skills} | Helping scale to 10k+ users | Open to opportunities"
        st.code(opt)

with t7:
    st.subheader("🌐 Portfolio")
    if st.button("Generate Portfolio"):
        html = f"<html><body style='padding:40px'><h1>{name}</h1><h3>{role}</h3><p>{skills}</p><p>{final_exp.replace(chr(10),'<br>')}</p></body></html>"
        st.download_button("Download portfolio.html", html, "portfolio.html", "text/html", type="primary")
        st.components.v1.html(html, height=300, scrolling=True)

with t8:
    st.subheader("💰 Salary Predictor - Chennai 2026")
    exp = st.slider("Years Exp", 0, 10, 2)
    if st.button("Predict Salary", type="primary"):
        base = 4.5+exp*1.2
        if "python" in skills.lower(): base+=2.5
        if "aws" in skills.lower(): base+=2.0
        if "react" in skills.lower(): base+=1.5
        st.metric("CTC", f"Rs {base:.1f} - {base+4:.1f} LPA")
        st.progress(min(95,int(base*8))/100)

    st.divider()
    # ✅ PROFESSIONAL DONATION - NOT BEGGING!
    st.markdown("### ☕ Love this tool? Buy me a Coffee")
    st.caption("This tool is 100% FREE forever. Your small support helps me keep building more free tools for students like you ❤️")

    # Direct GPay - click panna GPay app open aagum!
    upi_link = f"upi://pay?pa={MY_UPI_ID}&pn=Dileep%20Kumar%20M&cu=INR&tn=Coffee%20Support%20Resume%20Builder"

    c1, c2 = st.columns(2)
    with c1:
        st.link_button("☕ Donate - GPay / PhonePe", upi_link, type="primary", use_container_width=True)
    with c2:
        st.link_button("💙 Support Project", upi_link, use_container_width=True)

    st.info("🔒 100% Secure UPI | Any amount you wish - Rs.10, Rs.50")

st.caption("Built by Dileep M | Keep it FREE ❤️")