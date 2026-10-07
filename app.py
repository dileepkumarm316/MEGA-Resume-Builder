import streamlit as st
from fpdf import FPDF
import io
import re

st.set_page_config(page_title="AI Resume Builder - ULTRA", page_icon="🚀", layout="centered")

st.title("🚀 AI Resume Builder - ULTRA PRO MAX")
st.caption("Builder | Job Matcher | Cover Letter | Interview Q&A | Portfolio | Cold Email | Salary")

if 'final_exp' not in st.session_state:
    st.session_state['final_exp'] = "• Built scalable applications using Python handling 10k+ users\n• Improved system performance by 40% and reduced latency by 25%\n• Led development of 3+ core modules in Agile team of 5"

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📝 Builder", "🎯 Matcher", "✉️ Cover Letter", "🎤 Interview", "🌐 Portfolio", "💰 Salary"])

# TAB 1 - BUILDER
with tab1:
    template = st.selectbox("Select Template:", ["Modern Blue", "Classic Black"])
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name", "Dileep Kumar M", key="name")
        role = st.text_input("Target Role", "Software Engineer", key="role")
        email = st.text_input("Email", "dileep@gmail.com")
    with col2:
        phone = st.text_input("Phone", "+91 98765 43210")
        linkedin_url = st.text_input("LinkedIn URL", "https://linkedin.com/in/dileep")
        skills = st.text_input("Skills (comma separated)", "Python, Java, React, SQL")

    raw_exp = st.text_area("Experience in your own words", "Worked on Python projects, improved app performance")

    if st.button("✨ Enhance with AI - Make PRO", type="primary"):
        fs = skills.split(',')[0].strip() if ',' in skills else skills.strip()
        r = role.lower()
        if "software" in r or "developer" in r or "engineer" in r:
            new_exp = f"• Built scalable applications using {fs} handling 10k+ users\n• Improved system performance by 40% and reduced latency by 25%\n• Led development of 3+ core modules in Agile team of 5"
        elif "data" in r or "analyst" in r:
            new_exp = f"• Analyzed 1M+ records using {fs} & SQL, built interactive dashboards\n• Built predictive models improving accuracy by 25%\n• Automated reporting workflows saving 15 hours/week"
        elif "marketing" in r:
            new_exp = f"• Increased social media engagement by 150% in 3 months\n• Managed campaigns with 200K+ budget, achieved 3.5x ROI\n• Created content strategy boosting qualified leads by 60%"
        else:
            new_exp = f"• Delivered high-quality results as {role} using {fs}\n• Improved process efficiency by 30% through optimization\n• Collaborated with cross-functional teams to achieve project goals"
        st.session_state['final_exp'] = new_exp
        st.success(f"Enhanced for {role}!"); st.balloons()

    final_exp = st.text_area("Final Experience (You can edit)", value=st.session_state['final_exp'], height=170)

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("📊 Check ATS Score"):
            score = 0
            if "@" in email: score+=20
            if len(phone)>=10: score+=10
            if len(skills.split(','))>=3: score+=20
            if any(c in final_exp for c in ["%", "10k", "1M"]): score+=20
            if len(final_exp)>100: score+=30
            st.progress(score/100)
            st.metric("ATS Score", f"{score}/100")
            if score>=80: st.success("Excellent! Ready to apply")
            else: st.warning("Add metrics like % and numbers")
    with col_b:
        if st.button("📄 Generate PDF"):
            hc = (0,102,204) if "Blue" in template else (0,0,0)
            pdf = FPDF(); pdf.add_page()
            pdf.set_fill_color(hc[0],hc[1],hc[2]); pdf.rect(0,0,210,40,'F')
            pdf.set_y(10); pdf.set_text_color(255,255,255)
            pdf.set_font("Arial",'B',22); pdf.cell(0,10,name,align='C',ln=True)
            pdf.set_font("Arial",'',9); pdf.cell(0,6,f"{role} | {email} | {phone}",align='C',ln=True)
            pdf.set_font("Arial",'',7); pdf.cell(0,5,linkedin_url,align='C',ln=True)
            pdf.set_y(48); pdf.set_text_color(0,0,0)
            pdf.set_font("Arial",'B',12); pdf.cell(0,10,"SKILLS",ln=True)
            pdf.set_font("Arial",'',10); pdf.multi_cell(0,6,skills)
            pdf.set_font("Arial",'B',12); pdf.cell(0,10,"EXPERIENCE",ln=True)
            pdf.set_font("Arial",'',10); pdf.multi_cell(0,6,final_exp)
            pdf.set_font("Arial",'B',12); pdf.cell(0,10,"EDUCATION",ln=True)
            pdf.set_font("Arial",'',10); pdf.cell(0,6,"B.E. Computer Science - 2024",ln=True)
            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            st.download_button("⬇️ Download Resume PDF", pdf_bytes, f"{name}_Resume.pdf", "application/pdf", type="primary")

# TAB 2 - MATCHER
with tab2:
    st.subheader("🎯 Job Description Matcher")
    jd = st.text_area("Paste Job Description here", "Looking for Python developer with React, SQL, Agile, AWS experience. Must have built scalable apps...", height=150)
    if st.button("Check Match %"):
        jd_words = set(re.findall(r'\w+', jd.lower()))
        resume_words = set(re.findall(r'\w+', (skills + " " + final_exp).lower()))
        common = {w for w in jd_words.intersection(resume_words) if len(w)>3}
        jd_f = {w for w in jd_words if len(w)>3}
        match = min(95, int(len(common)/max(len(jd_f),1)*100)+40)
        st.progress(match/100); st.metric("Compatibility Score", f"{match}%")
        missing = list(jd_f - resume_words)[:10]
        if match>=75: st.success("🔥 High match! Apply immediately")
        else: st.warning(f"⚠️ Add these keywords: {', '.join(missing)}")

# TAB 3 - COVER LETTER
with tab3:
    st.subheader("✉️ Cover Letter & LinkedIn Generator")
    company = st.text_input("Company Name", "Google", key="company")
    if st.button("Generate Cover Letter"):
        cl = f"""Dear Hiring Manager at {company},

I am excited to apply for the {role} position. With proven expertise in {skills}, I have {final_exp.split(chr(10))[0].replace('•','').strip().lower()}.

My background in building scalable solutions and improving performance by 40% aligns perfectly with {company}'s mission.

I am eager to bring my skills to {company} and contribute to your team's success.

Best regards,
{name}
{email} | {phone}
{linkedin_url}
"""
        st.text_area("Cover Letter - Copy this", cl, height=280)
        st.success("Cover letter ready for " + company)

# TAB 4 - INTERVIEW
with tab4:
    st.subheader("🎤 Interview Q&A Generator")
    st.info("Based on your resume, interviewer will ask these:")
    if st.button("Generate Interview Questions + Answers"):
        q_a = f"""Q1: Tell me about your project where you {final_exp.split(chr(10))[0].replace('•','').strip().lower()}?
ANSWER: Use STAR method. Situation: Project needed scalable app. Task: Build with {skills.split(',')[0]}. Action: Implemented caching, optimized DB. Result: Handled 10k+ users, 40% performance boost.

Q2: How did you improve system performance by 40%?
ANSWER: Talk about profiling, identifying bottlenecks, using indexing, caching with Redis, code optimization.

Q3: Explain your experience leading a team of 5 in Agile?
ANSWER: Daily standups, sprint planning, code reviews, conflict resolution, delivered 3 modules on time.

Q4: Why {company if 'company' in locals() else 'this company'}?
ANSWER: Research company products, align your {role} skills with their tech stack, show passion.

Q5: What are your strengths in {skills}?
ANSWER: Mention {skills} projects, 2+ years experience, quick learner, built production apps.
"""
        st.text_area("Interview Prep", q_a, height=400)

# TAB 5 - PORTFOLIO
with tab5:
    st.subheader("🌐 Portfolio Website Generator")
    if st.button("Generate Portfolio HTML"):
        html_code = f"""
<html>
<head><title>{name} - {role}</title>
<style>body{{font-family:Arial; max-width:800px; margin:auto; padding:40px;}} h1{{color:#0066cc}}.card{{border:1px solid #ddd; padding:20px; border-radius:10px; margin:20px 0;}}</style>
</head>
<body>
<h1>{name}</h1>
<h3>{role}</h3>
<p>📧 {email} | 📞 {phone} | 🔗 {linkedin_url}</p>
<div class="card"><h2>Skills</h2><p>{skills}</p></div>
<div class="card"><h2>Experience</h2><p>{final_exp.replace(chr(10), '<br>')}</p></div>
<div class="card"><h2>Contact Me</h2><p>Open to opportunities in {role}</p></div>
</body>
</html>
"""
        st.download_button("⬇️ Download portfolio.html", html_code, "portfolio.html", "text/html", type="primary")
        st.code(html_code[:500]+"...", language="html")

    st.divider()
    st.subheader("📧 Cold Email Generator")
    recruiter_name = st.text_input("Recruiter Name", "Hiring Manager")
    if st.button("Generate Cold Email to Recruiter"):
        email_text = f"""Subject: Application for {role} at {company if 'company' in locals() else 'Your Company'} | {name} | {skills.split(',')[0]}

Hi {recruiter_name},

I came across your opening for {role} at {company if 'company' in locals() else 'your company'} and was excited to apply.

With expertise in {skills}, I have {final_exp.split(chr(10))[0].replace('•','').strip().lower()}. I have improved system performance by 40% and handled 10k+ users in production.

Resume attached (ATS Score: 100/100). Portfolio: {linkedin_url}

Would love to discuss how I can contribute to {company if 'company' in locals() else 'your company'}'s team.

Best regards,
{name}
{phone} | {email}
"""
        st.text_area("Cold Email - Copy & Send", email_text, height=300)

# TAB 6 - SALARY
with tab6:
    st.subheader("💰 Chennai Salary Predictor 2026")
    st.write("Based on your skills and role")
    if st.button("Predict My Salary"):
        base = 4.5
        if "python" in skills.lower(): base+=2.5
        if "react" in skills.lower(): base+=1.5
        if "java" in skills.lower(): base+=1.2
        if "sql" in skills.lower(): base+=1.0
        if "aws" in skills.lower() or "cloud" in skills.lower(): base+=2.0
        st.metric("Estimated CTC Range", f"₹ {base:.1f} - {base+3.5:.1f} LPA", f"+ {len(skills.split(','))} skills")
        st.progress(min(95, int(base*8))/100)
        st.info(f"For {role} in Chennai. Top skills: {skills}. Tip: Add AWS/Cloud to increase by 2 LPA")

    st.divider()
    st.subheader("🔧 Tools")
    st.write("Requirements.txt for your app:")
    st.code("streamlit\nfpdf\npython-docx\nPyPDF2", language="text")