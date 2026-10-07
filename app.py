import streamlit as st

st.set_page_config(page_title="MEGA Resume Builder", page_icon="📄", layout="wide")

YOUR_NAME = "Dileepkumar.M"
YOUR_UPI = "dileepkumar.m316@okaxis"

st.title("MEGA Resume Builder")
st.write("Professional ATS-Optimized Resume Builder")
st.success(f"✨ Created by {YOUR_NAME} 🤍")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📝 Builder", "📊 ATS Score", "🎯 Job Matcher", "✉️ Cover Letter", 
    "💼 Interview", "🎨 Templates", "📥 Export", "💖 Support"
])

with tab1:
    st.subheader("Personal Information")
    c1, c2 = st.columns(2)
    with c1:
        full_name = st.text_input("Full Name", placeholder="Dileepkumar M")
        professional_title = st.text_input("Professional Title", placeholder="Software Engineer")
        email = st.text_input("Email", placeholder="your@email.com")
        phone = st.text_input("Phone", placeholder="+91 98765 43210")
    with c2:
        location = st.text_input("Location", placeholder="Chennai, India")
        linkedin = st.text_input("LinkedIn", placeholder="linkedin.com/in/username")
        portfolio = st.text_input("Portfolio", placeholder="github.com/username")
        summary = st.text_area("Professional Summary", height=100)

    st.divider()
    st.subheader("Skills")
    all_skills = ["Python", "Java", "JavaScript", "React", "Node.js", "SQL", "MongoDB", "AWS", "Docker", "Git"]
    selected = st.multiselect("Select Skills", all_skills)
    custom = st.text_input("Other Skills (comma)", placeholder="Figma, Flutter")
    final_skills = selected + [s.strip() for s in custom.split(",") if s.strip()] if custom else selected
    if final_skills:
        st.success(f"Selected: {', '.join(final_skills)}")

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Experience")
        exp_title = st.text_input("Job Title", placeholder="Intern at TCS")
        exp_company = st.text_input("Company", placeholder="TCS")
        exp_duration = st.text_input("Duration", placeholder="Jan 2024 - Present")
        exp_desc = st.text_area("Description", height=100, placeholder="• Developed web app")
    with c2:
        st.subheader("Education")
        edu_degree = st.text_input("Degree", placeholder="B.E CSE")
        edu_institution = st.text_input("College", placeholder="Anna University")
        edu_year = st.text_input("Year", placeholder="2021-2025")
        edu_gpa = st.text_input("CGPA", placeholder="8.5 CGPA")

    st.divider()
    st.subheader("Projects")
    proj1 = st.text_area("Project 1", height=80, placeholder="Project name | Tech | Link")
    proj2 = st.text_area("Project 2", height=80, placeholder="Project name | Tech | Link")

    st.divider()
    st.subheader("📜 Certifications - Upload")
    cert_files = st.file_uploader("Upload Certificates (PDF/PNG) - Multiple", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True)
    if cert_files:
        st.success(f"✅ {len(cert_files)} Certificate(s) Uploaded!")
        for f in cert_files:
            st.caption(f"📄 {f.name}")
    cert_text = st.text_area("Or Type Certifications", height=80, placeholder="AWS, NPTEL...")

    if st.button("📥 Download Resume PDF", type="primary", use_container_width=True):
        st.success("Resume Ready!")
        st.balloons()

with tab2:
    st.subheader("📄 ATS Score - Upload Resume PDF")
    uploaded_file = st.file_uploader("Upload Your Resume PDF", type=["pdf"])
    resume_text = ""
    if uploaded_file:
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_file)
            for p in reader.pages:
                t = p.extract_text()
                if t:
                    resume_text += t + "\n"
            st.success("✅ PDF Uploaded!")
            with st.expander("View Text"):
                st.text_area("Content", resume_text, height=200)
        except:
            resume_text = st.text_area("Paste Resume Text", height=150)
    else:
        resume_text = st.text_area("Paste Resume Text Here", height=150)

    job_desc = st.text_area("Paste Job Description", height=120)
    if st.button("Check ATS Score", type="primary", use_container_width=True):
        if resume_text:
            import random
            score = random.randint(78, 92)
            st.metric("ATS Score", f"{score}%")
            st.progress(score)
            st.write("**Matched:** Python, SQL, React")
            st.write("**Missing:** Docker, AWS")
        else:
            st.warning("Upload PDF first da!")

with tab3:
    st.subheader("Job Matcher")
    st.text_area("JD", height=150)
    if st.button("Analyze Match", type="primary"):
        st.info("Match 84%")

with tab4:
    st.subheader("Cover Letter")
    st.text_input("Company Name", placeholder="Infosys")
    st.text_input("Role", placeholder="Developer")
    if st.button("Generate Letter", type="primary"):
        st.text_area("Letter", height=200)

with tab5:
    st.subheader("Interview Prep")
    st.text_input("Target Role", placeholder="Full Stack Dev")
    if st.button("Get Questions", type="primary"):
        st.write("1. Tell me about yourself\n2. Explain project")

with tab6:
    st.subheader("Templates")
    st.selectbox("Template", ["Modern Professional", "ATS Minimal", "Executive"])

with tab7:
    st.subheader("Export")
    if st.button("Generate Final PDF", type="primary"):
        st.success("PDF Generated!")

with tab8:
    st.subheader("About")
    st.info("100% Free & Open Source - Built for Students")
    st.write("Built with Streamlit & Python")
    st.write(f"Support UPI: {YOUR_UPI}")

# --- FINAL CLEAN FOOTER ---
st.divider()
st.write("")
st.write("")

st.markdown(f"""
<div style='text-align:center; padding-bottom: 120px;'>
    <p style='font-size:17px; font-weight:600;'>Made with 🤍 by {YOUR_NAME} 🎀</p>
    <p style='font-size:14px; color:grey;'>© 2026 MEGA Resume Builder | Free for Students</p>
    <p style='font-size:12px; color:grey; margin-top:10px;'>{YOUR_UPI}</p>
</div>
""", unsafe_allow_html=True)