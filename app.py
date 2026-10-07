import streamlit as st
from fpdf import FPDF
import re

st.set_page_config(page_title="Resume AI - Mega", page_icon="🚀", layout="centered")

if 'final_exp' not in st.session_state:
    st.session_state['final_exp'] = "- Built scalable applications using Python handling 10k+ users\n- Improved system performance by 40%\n- Led development of 3+ modules in Agile team of 5"

st.title("🚀 AI Resume Builder - MEGA")
st.caption("100% FREE - 8 Features!")

t1, t2, t3, t4, t5, t6, t7, t8 = st.tabs([
    "Builder", "ATS Score", "Matcher", "Cover Letter",
    "Interview", "LinkedIn", "Portfolio", "💰 Salary"
])

with t1:
    name = st.text_input("Full Name", "Dileep Kumar M")
    role = st.text_input("Role", "Software Engineer")
    email = st.text_input("Email", "dileep@gmail.com")
    phone = st.text_input("Phone", "+91 98765 43210")
    skills = st.text_input("Skills", "Python, React, SQL, AWS, Docker")
    raw = st.text_area("Your Experience Rough", "worked on python project made app faster")

    if st.button("✨ Enhance + Grammar Fix", type="primary"):
        fs = skills.split(',')[0] if skills else "Python"
        enhanced = f"- Built scalable applications using {fs} handling 10k+ users\n- Improved system performance by 40% and reduced latency by 25%\n- Led development of 3+ modules in Agile team of 5 using {skills}\n- Implemented CI/CD pipeline and automated testing"
        st.session_state['final_exp'] = enhanced
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
        pdf.set_font("Arial", 'B', 12); pdf.cell(0, 8, "SKILLS", ln=True)
        pdf.set_font("Arial", '', 10); pdf.multi_cell(0, 6, skills)
        pdf.ln(4)
        pdf.set_font("Arial", 'B', 12); pdf.cell(0, 8, "EXPERIENCE", ln=True)
        pdf.set_font("Arial", '', 10); pdf.multi_cell(0, 6, final_exp)
        pdf_data = bytes(pdf.output())

        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download PDF", pdf_data, "resume.pdf", "application/pdf", type="primary")
        with c2:
            wa_text = f"Hi, I'm {name} - {role}. My resume: Skills {skills}. Interested?"
            wa_link = f"https://wa.me/?text={wa_text.replace(' ', '%20')}"
            st.link_button("📱 WhatsApp Share", wa_link)
        st.success("PDF Ready! ✅")

with t2:
    st.subheader("🎯 ATS Score Checker - KILLER FEATURE!")
    if st.button("Check ATS Score", type="primary"):
        score = 50
        feedback = []
        if len(skills.split(',')) >= 4: score += 15
        else: feedback.append("❌ Add 5+ skills da")
        if len(final_exp) > 150: score += 15
        else: feedback.append("❌ Experience too short")
        if "python" in (skills+final_exp).lower(): score += 10
        if "built" in final_exp.lower() or "improved" in final_exp.lower(): score += 10
        else: feedback.append("❌ Use action words: Built, Improved, Led")

        score = min(95, score)
        st.metric("ATS SCORE", f"{score}/100")
        st.progress(score/100)

        if score >= 80:
            st.success("🔥 SEMMA DA! Recruiter shortlist panniduvan!")
        elif score >= 60:
            st.warning("Decent da, konjam improve pannalam")
        else:
            st.error("Low da - skills add pannu!")

        for f in feedback:
            st.write(f)
        if not feedback:
            st.write("✅ All good da! Top 10% resume!")

with t3:
    st.subheader("🎯 Job Matcher")
    jd = st.text_area("Paste JD", "Looking for Python, React, SQL...")
    if st.button("Check Match"):
        jd_w = set(re.findall(r'\w+', jd.lower()))
        res_w = set(re.findall(r'\w+', (skills + " " + final_exp).lower()))
        match = min(95, int(len(res_w.intersection(jd_w))/max(len(jd_w),1)*100)+45)
        st.progress(match/100)
        st.metric("Match", f"{match}%")

with t4:
    st.subheader("✉️ Cover Letter")
    comp = st.text_input("Company", "Google")
    if st.button("Generate Cover Letter"):
        first = final_exp.split("\n")[0].replace("-","").strip()
        cl = f"Dear Hiring Manager at {comp},\n\nI am excited to apply for {role}. With expertise in {skills}, I {first}.\n\nI improved performance by 40% and led team of 5. Eager to bring same impact to {comp}.\n\nBest,\n{name}"
        st.text_area("Cover Letter", cl, height=250)
        wa_cl = f"Hi {comp} team, applying for {role}. {first}"
        st.link_button("📱 Send via WhatsApp", f"https://wa.me/?text={wa_cl.replace(' ', '%20')}")

with t5:
    st.subheader("🎤 Interview Q&A - 10 Questions")
    if st.button("Generate 10 Q&A"):
        s1 = skills.split(',')[0] if skills else "Python"
        qa = f"""Q1: Tell me about yourself?
A: I am {name}, {role} skilled in {skills}.

Q2: Explain {s1} project?
A: {final_exp.split(chr(10))[0].replace('-','').strip()}

Q3: How 40% improvement?
A: Profiling, caching, indexing

Q4: Agile experience?
A: Led 5 members, sprints, standups

Q5: Why hire you?
A: {skills} + proven results

Q6: Pressure handling?
A: Prioritize, communicate

Q7: {skills.split(',')[1] if len(skills.split(','))>1 else 'React'} experience?
A: Built 3 modules, API integration

Q8: 5 year goal?
A: Tech Lead

Q9: Expected CTC?
A: Market competitive

Q10: Questions for us?
A: Tech stack? Growth?
"""
        st.text_area("10 Q&A", qa, height=400)

with t6:
    st.subheader("💼 LinkedIn Optimizer")
    linkedin_bio = st.text_area("Paste your LinkedIn Bio", "Software Engineer | Python")
    if st.button("Optimize LinkedIn"):
        optimized = f"🚀 {role} | {skills} | Helping companies scale to 10k+ users | {final_exp.split(chr(10))[0].replace('-','').strip()} | Open to opportunities | Chennai"
        st.success("Optimized Bio:")
        st.code(optimized)
        st.text_area("Headline Idea", f"{role} | {skills.split(',')[0]} Expert | 40% Performance Boost | {comp if 'comp' in locals() else 'Ex-Startup'}")

with t7:
    st.subheader("🌐 Portfolio + WhatsApp")
    if st.button("Generate Portfolio"):
        html = f"""<html><head><title>{name}</title></head>
        <body style='padding:40px; font-family:Arial; max-width:800px; margin:auto'>
        <h1>{name}</h1><h3>{role}</h3><p><b>{skills}</b></p>
        <p>{final_exp.replace(chr(10),'<br>')}</p>
        <hr><a href='https://wa.me/{phone.replace('+','').replace(' ','')}'>Contact on WhatsApp</a>
        </body></html>"""
        st.download_button("Download portfolio.html", html, "portfolio.html", "text/html", type="primary")
        st.components.v1.html(html, height=400, scrolling=True)

with t8:
    st.subheader("💰 Salary Predictor - Chennai 2026")
    exp = st.slider("Years Exp", 0, 10, 2)
    if st.button("Predict Salary", type="primary"):
        base = 4.5 + exp*1.2
        if "python" in skills.lower(): base += 2.5
        if "aws" in skills.lower(): base += 2.0
        if "react" in skills.lower(): base += 1.5
        if "docker" in skills.lower(): base += 1.0

        st.metric("Estimated CTC", f"Rs {base:.1f} - {base+4:.1f} LPA")
        st.progress(min(95, int(base*8))/100)
        st.info("💡 Add AWS + System Design = +3 LPA")
        st.link_button("💸 Donate Rs.50 (Support)", "https://www.buymeacoffee.com/")

st.caption("Built by Dileep M | MEGA V2 | 8 Features ✅")