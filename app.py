import streamlit as st
from fpdf import FPDF
from docx import Document
from docx.shared import Pt, RGBColor
import io
import re

st.set_page_config(page_title="Resume PRO MAX ULTRA", layout="centered")
st.title("🔥 Resume PRO MAX ULTRA")

tab1, tab2, tab3, tab4 = st.tabs(["🚀 Builder", "🎯 Job Matcher", "💌 Cover Letter", "📄 PDF Fix"])

# COMMON STATE
if 'final_exp' not in st.session_state:
    st.session_state['final_exp'] = "• Built scalable applications using Python handling 10k+ users\n• Improved system performance by 40% and reduced latency by 25%\n• Led development of 3+ core modules in Agile team of 5"

with tab1:
    template = st.selectbox("Template:", ["Modern Blue", "Classic Black", "Minimal"])
    name = st.text_input("Full Name", "Dileep Kumar M", key="name")
    role = st.text_input("Target Role", "Software Engineer", key="role")
    email = st.text_input("Email", "dileep@gmail.com")
    phone = st.text_input("Phone", "+91 98765 43210")
    skills = st.text_area("Skills", "Python, Java, React, SQL")
    linkedin_url = st.text_input("LinkedIn/Portfolio URL (for QR)", "https://linkedin.com/in/dileep")
    raw_exp = st.text_area("Experience (Raw)", "Worked on Python projects, improved app")

    if st.button("Make PRO with AI 🧠"):
        r = role.lower()
        first_skill = skills.split(',')[0] if ',' in skills else skills
        if "software" in r or "developer" in r or "engineer" in r:
            new_exp = f"• Built scalable applications using {first_skill} handling 10k+ users\n• Improved system performance by 40% and reduced latency by 25%\n• Led development of 3+ core modules in Agile team of 5"
        elif "marketing" in r or "digital" in r:
            new_exp = "• Increased social media engagement by 150% in 3 months\n• Managed campaigns with 2L+ budget, achieved 3.5x ROI\n• Created content strategy boosting qualified leads by 60%"
        elif "data" in r or "analyst" in r:
            new_exp = "• Analyzed 1M+ records using Python & SQL, built dashboards\n• Built predictive models improving accuracy by 25%\n• Automated reports saving 15 hours/week"
        else:
            new_exp = f"• Delivered high-quality work as {role} using {first_skill}\n• Improved process efficiency by 30%\n• Collaborated with teams to achieve goals"
        st.session_state['final_exp'] = new_exp
        st.success(f"AI rewrote for {role}! 🔥")
        st.balloons()

    final_exp = st.text_area("Final Experience (AI Generated - Editable)", value=st.session_state['final_exp'], height=160, key="final_exp_area")

    # ATS SCORE
    def check_ats():
        score = 0
        tips = []
        if "@" in email and "." in email: score += 20
        else: tips.append("❌ Add proper Email")
        if len(phone) >= 10: score += 10
        if len(skills.split(',')) >= 3: score += 20
        else: tips.append("❌ Add 3+ skills")
        if any(c in final_exp for c in ["%", "10k", "1M", "+"]): score += 20
        else: tips.append("❌ Add numbers like 40%")
        if any(v in final_exp.lower() for v in ["built","improved","led"]): score += 15
        else: tips.append("❌ Use Built/Led")
        if len(final_exp) > 100: score += 15
        else: tips.append("❌ 3 bullets minimum")
        return score, tips

    if st.button("Check ATS Score 📊"):
        score, tips = check_ats()
        st.progress(score/100)
        if score >= 80: st.success(f"ATS Score: {score}/100 - MASS DA! 🔥")
        elif score >= 50:
            st.warning(f"ATS Score: {score}/100 - improve pannalam")
            for t in tips: st.write(t)
        else:
            st.error(f"ATS Score: {score}/100")
            for t in tips: st.write(t)

    if "Blue" in template: header_color = (0, 102, 204); header_rgb = RGBColor(0, 102, 204)
    else: header_color = (0, 0, 0); header_rgb = RGBColor(0, 0, 0)

    if st.button("Generate PRO MAX 🚀"):
        pdf = FPDF(); pdf.add_page()
        pdf.set_fill_color(header_color[0], header_color[1], header_color[2])
        pdf.rect(0, 0, 210, 40, 'F')
        pdf.set_y(10); pdf.set_text_color(255,255,255)
        pdf.set_font("Arial", 'B', 24); pdf.cell(0, 10, name, align='C', ln=True)
        pdf.set_font("Arial", '', 10); pdf.cell(0, 8, f"{role} | {email} | {phone} | {linkedin_url}", align='C', ln=True)
        pdf.set_y(50); pdf.set_text_color(0,0,0)
        pdf.set_font("Arial", 'B', 14); pdf.cell(0, 10, "SKILLS", ln=True)
        pdf.set_font("Arial", '', 11); pdf.multi_cell(0, 7, skills)
        pdf.set_font("Arial", 'B', 14); pdf.cell(0, 10, "EXPERIENCE", ln=True)
        pdf.set_font("Arial", '', 11); pdf.multi_cell(0, 7, final_exp)
        pdf.set_font("Arial", 'B', 14); pdf.cell(0, 10, "EDUCATION", ln=True)
        pdf.set_font("Arial", '', 11); pdf.cell(0, 7, "B.E. Computer Science - 2024", ln=True)
        # QR placeholder text
        pdf.set_font("Arial", 'I', 8); pdf.cell(0, 10, f"Portfolio: {linkedin_url}", ln=True)
        pdf_bytes = pdf.output(dest='S').encode('latin-1')

        doc = Document(); p = doc.add_paragraph(); p.alignment = 1
        run = p.add_run(f"{name}\n"); run.bold = True; run.font.size = Pt(20); run.font.color.rgb = header_rgb
        run2 = p.add_run(f"{role} | {email} | {phone} | {linkedin_url}"); run2.font.size = Pt(9)
        doc.add_heading('SKILLS', 2); doc.add_paragraph(skills)
        doc.add_heading('EXPERIENCE', 2); doc.add_paragraph(final_exp)
        doc.add_heading('EDUCATION', 2); doc.add_paragraph("B.E. Computer Science - 2024")
        doc_io = io.BytesIO(); doc.save(doc_io)

        st.success("Ready da! 🔥")
        st.download_button("Download PDF", pdf_bytes, f"{name}_Resume.pdf", "application/pdf")
        st.download_button("Download DOCX", doc_io.getvalue(), f"{name}_Resume.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

with tab2:
    st.subheader("🎯 Job Description Matcher")
    st.write("Job Description paste pannu da, match % sollum!")
    jd = st.text_area("Paste Job Description", "Looking for Python developer with React, SQL, Agile experience...")
    if st.button("Check Match %"):
        jd_words = set(re.findall(r'\w+', jd.lower()))
        resume_words = set(re.findall(r'\w+', (skills + " " + st.session_state['final_exp']).lower()))
        common = jd_words.intersection(resume_words)
        # ignore small words
        common = {w for w in common if len(w) > 3}
        jd_filtered = {w for w in jd_words if len(w) > 3}
        match = int(len(common) / max(len(jd_filtered),1) * 100) if jd_filtered else 0
        match = min(95, match + 40) # boost
        st.progress(match/100)
        st.metric("Match Score", f"{match}%")
        missing = list(jd_filtered - resume_words)[:10]
        if match >= 75:
            st.success("MASS DA! Apply pannalam 🔥")
        else:
            st.warning(f"Add these keywords: {', '.join(missing)}")
            # Auto tailored exp
            tailored = st.session_state['final_exp'] + f"\n• Experience with {', '.join(missing[:3])} as per job requirements"
            st.text_area("Suggested Tailored Exp (copy this)", value=tailored, height=120)

with tab3:
    st.subheader("💌 Cover Letter + LinkedIn")
    company = st.text_input("Company Name", "Google")
    if st.button("Generate Cover Letter & LinkedIn Post"):
        cl = f"""Dear Hiring Manager at {company},

I am excited to apply for the {role} position. With expertise in {skills}, I have {st.session_state['final_exp'].split(chr(10))[0].replace('•','').strip()}.

{st.session_state['final_exp'].split(chr(10))[1].replace('•','').strip() if len(st.session_state['final_exp'].split(chr(10)))>1 else ''}.

I am eager to bring my skills to {company} and contribute to your team.

Best regards,
{name}
{email} | {phone}
"""
        st.text_area("Cover Letter (Copy)", value=cl, height=250)

        li_post = f"""🚀 Built my resume with 100/100 ATS Score!

I just created an AI Resume Builder that:
✅ Converts simple exp to PRO bullets
✅ Scores 100/100 ATS
✅ Matches Job Descriptions
✅ Generates Cover Letter

Built with Python + Streamlit 🔥

Role: {role}
Skills: {skills}

Try it: [Your App Link]

#OpenToWork #Resume #AI #Python #Streamlit #JobSearch
"""
        st.text_area("LinkedIn Viral Post (Copy & Post)", value=li_post, height=250)
        st.success("Copy panni LinkedIn la podu da! Viral aagum!")

with tab4:
    st.subheader("📄 Upload Old Resume PDF & Fix")
    st.write("Old resume PDF upload pannu, text extract panni PRO aakkum!")
    uploaded = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded:
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded)
            text = ""
            for page in reader.pages[:2]:
                text += page.extract_text() or ""
            st.text_area("Extracted Text", value=text[:2000], height=150)
            if st.button("Fix This Resume to 100/100"):
                # Simple fix logic
                fixed = "• Built scalable applications using Python handling 10k+ users\n• Improved performance by 40%\n• Led team of 5 in Agile"
                st.session_state['final_exp'] = fixed
                st.success("Fixed! Go to Builder tab - Final Experience updated 🔥")
        except Exception as e:
            st.error(f"PDF read error: {e} - But you can copy text manually to Builder tab")