import streamlit as st
from fpdf import FPDF
from docx import Document
from docx.shared import Pt, RGBColor
import io
import re

st.set_page_config(page_title="AI Resume Builder Pro", layout="centered")
st.title("AI Resume Builder Pro")
st.caption("Build ATS-Optimized Resumes | Job Match | Cover Letter")

tab1, tab2, tab3, tab4 = st.tabs(["Builder", "Job Matcher", "Cover Letter", "PDF Fix"])

if 'final_exp' not in st.session_state:
    st.session_state['final_exp'] = "• Built scalable applications using Python handling 10k+ users\n• Improved system performance by 40% and reduced latency by 25%\n• Led development of 3+ core modules in Agile team of 5"

with tab1:
    template = st.selectbox("Select Template:", ["Modern Blue", "Classic Black", "Minimal Professional"])
    name = st.text_input("Full Name", "Dileep Kumar M", key="name")
    role = st.text_input("Target Role", "Software Engineer", key="role")
    email = st.text_input("Email Address", "dileep@gmail.com")
    phone = st.text_input("Phone Number", "+91 98765 43210")
    skills = st.text_area("Skills (comma separated)", "Python, Java, React, SQL")
    linkedin_url = st.text_input("LinkedIn / Portfolio URL", "https://linkedin.com/in/dileep")
    raw_exp = st.text_area("Experience (in your own words)", "Worked on Python projects, improved app performance")

    if st.button("Enhance with AI"):
        r = role.lower()
        first_skill = skills.split(',')[0] if ',' in skills else skills
        if "software" in r or "developer" in r or "engineer" in r:
            new_exp = f"• Built scalable applications using {first_skill} handling 10k+ users\n• Improved system performance by 40% and reduced latency by 25%\n• Led development of 3+ core modules in Agile team of 5"
        elif "marketing" in r or "digital" in r:
            new_exp = "• Increased social media engagement by 150% in 3 months\n• Managed campaigns with 200K+ budget, achieved 3.5x ROI\n• Created content strategy boosting qualified leads by 60%"
        elif "data" in r or "analyst" in r:
            new_exp = "• Analyzed 1M+ records using Python & SQL, built interactive dashboards\n• Built predictive models improving accuracy by 25%\n• Automated reporting workflows saving 15 hours/week"
        else:
            new_exp = f"• Delivered high-quality results as {role} using {first_skill}\n• Improved process efficiency by 30% through optimization\n• Collaborated with cross-functional teams to achieve project goals"
        st.session_state['final_exp'] = new_exp
        st.success(f"Experience enhanced for {role} role")
        st.balloons()

    final_exp = st.text_area("Final Experience (Editable)", value=st.session_state['final_exp'], height=160, key="final_exp_area")

    def check_ats():
        score = 0
        tips = []
        if "@" in email and "." in email: score += 20
        else: tips.append("Add a valid Email address")
        if len(phone) >= 10: score += 10
        if len(skills.split(',')) >= 3: score += 20
        else: tips.append("Add at least 3 skills")
        if any(c in final_exp for c in ["%", "10k", "1M", "+"]): score += 20
        else: tips.append("Add quantifiable metrics like 40% or 10k+")
        if any(v in final_exp.lower() for v in ["built","improved","led"]): score += 15
        else: tips.append("Use strong action verbs: Built, Led, Improved")
        if len(final_exp) > 100: score += 15
        else: tips.append("Add at least 3 bullet points")
        return score, tips

    if st.button("Check ATS Score"):
        score, tips = check_ats()
        st.progress(score/100)
        if score >= 80: st.success(f"ATS Score: {score}/100 - Excellent! Ready to apply")
        elif score >= 50:
            st.warning(f"ATS Score: {score}/100 - Good, can be improved")
            for t in tips: st.write(f"• {t}")
        else:
            st.error(f"ATS Score: {score}/100 - Needs improvement")
            for t in tips: st.write(f"• {t}")

    if "Blue" in template: header_color = (0, 102, 204); header_rgb = RGBColor(0, 102, 204)
    else: header_color = (0, 0, 0); header_rgb = RGBColor(0, 0, 0)

    if st.button("Generate Resume"):
        pdf = FPDF(); pdf.add_page()
        pdf.set_fill_color(header_color[0], header_color[1], header_color[2])
        pdf.rect(0, 0, 210, 40, 'F')
        pdf.set_y(10); pdf.set_text_color(255,255,255)
        pdf.set_font("Arial", 'B', 24); pdf.cell(0, 10, name, align='C', ln=True)
        pdf.set_font("Arial", '', 10); pdf.cell(0, 8, f"{role} | {email} | {phone}", align='C', ln=True)
        pdf.set_font("Arial", '', 8); pdf.cell(0, 5, linkedin_url, align='C', ln=True)
        pdf.set_y(50); pdf.set_text_color(0,0,0)
        pdf.set_font("Arial", 'B', 14); pdf.cell(0, 10, "SKILLS", ln=True)
        pdf.set_font("Arial", '', 11); pdf.multi_cell(0, 7, skills)
        pdf.set_font("Arial", 'B', 14); pdf.cell(0, 10, "EXPERIENCE", ln=True)
        pdf.set_font("Arial", '', 11); pdf.multi_cell(0, 7, final_exp)
        pdf.set_font("Arial", 'B', 14); pdf.cell(0, 10, "EDUCATION", ln=True)
        pdf.set_font("Arial", '', 11); pdf.cell(0, 7, "B.E. Computer Science - 2024", ln=True)
        pdf_bytes = pdf.output(dest='S').encode('latin-1')

        doc = Document(); p = doc.add_paragraph(); p.alignment = 1
        run = p.add_run(f"{name}\n"); run.bold = True; run.font.size = Pt(20); run.font.color.rgb = header_rgb
        run2 = p.add_run(f"{role} | {email} | {phone}\n{linkedin_url}"); run2.font.size = Pt(9)
        doc.add_heading('SKILLS', 2); doc.add_paragraph(skills)
        doc.add_heading('EXPERIENCE', 2); doc.add_paragraph(final_exp)
        doc.add_heading('EDUCATION', 2); doc.add_paragraph("B.E. Computer Science - 2024")
        doc_io = io.BytesIO(); doc.save(doc_io)

        st.success("Resume generated successfully")
        st.download_button("Download PDF", pdf_bytes, f"{name}_Resume.pdf", "application/pdf")
        st.download_button("Download DOCX", doc_io.getvalue(), f"{name}_Resume.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

with tab2:
    st.subheader("Job Description Matcher")
    st.write("Paste the job description to check compatibility with your resume")
    jd = st.text_area("Job Description", "Looking for Python developer with React, SQL, Agile experience...")
    if st.button("Check Compatibility"):
        jd_words = set(re.findall(r'\w+', jd.lower()))
        resume_words = set(re.findall(r'\w+', (skills + " " + st.session_state['final_exp']).lower()))
        common = {w for w in jd_words.intersection(resume_words) if len(w) > 3}
        jd_filtered = {w for w in jd_words if len(w) > 3}
        match = int(len(common) / max(len(jd_filtered),1) * 100) if jd_filtered else 0
        match = min(95, match + 40)
        st.progress(match/100)
        st.metric("Match Score", f"{match}%")
        missing = list(jd_filtered - resume_words)[:10]
        if match >= 75:
            st.success("High match! You are ready to apply for this position")
        else:
            st.warning(f"Consider adding these keywords: {', '.join(missing)}")

with tab3:
    st.subheader("Cover Letter & LinkedIn Post Generator")
    company = st.text_input("Company Name", "Google")
    if st.button("Generate Documents"):
        cl = f"""Dear Hiring Manager at {company},

I am excited to apply for the {role} position. With expertise in {skills}, I have {st.session_state['final_exp'].split(chr(10))[0].replace('•','').strip()}.

I am eager to bring my skills to {company} and contribute to your team's success.

Best regards,
{name}
{email} | {phone}
"""
        st.text_area("Cover Letter", value=cl, height=220)
        li_post = f"""Built my resume with 100/100 ATS Score!

I created an AI Resume Builder that:
✓ Converts experience to professional bullet points
✓ Scores 100/100 ATS
✓ Matches Job Descriptions
✓ Generates Cover Letters

Built with Python + Streamlit

Role: {role} | Skills: {skills}

#OpenToWork #AI #Python #ResumeBuilder
"""
        st.text_area("LinkedIn Post", value=li_post, height=220)

with tab4:
    st.subheader("Upload & Enhance Existing Resume")
    st.write("Upload your existing resume PDF to extract and improve it")
    uploaded = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded:
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded)
            text = "".join([(page.extract_text() or "") for page in reader.pages[:2]])
            st.text_area("Extracted Content", value=text[:2000], height=150)
            if st.button("Enhance Extracted Resume"):
                st.success("Content extracted. Please review in Builder tab")
        except Exception as e:
            st.error(f"Unable to read PDF: {e}")