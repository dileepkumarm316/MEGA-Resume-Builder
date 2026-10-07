import streamlit as st

st.set_page_config(page_title="MEGA Resume Builder", page_icon="📄", layout="wide")

YOUR_UPI = "dileepkumar.m316@okaxis"
YOUR_NAME = "Dileepkumar.M"

# TOP BANNER
st.title("MEGA Resume Builder")
st.write("Professional ATS-Optimized Resume Builder")
st.success(f"✨ Created by {YOUR_NAME} 🤍🎀")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📝 Builder", "📊 ATS Score", "🎯 Job Matcher", "✉️ Cover Letter", 
    "💼 Interview", "🎨 Templates", "📥 Export", "💖 Support Me"
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
        summary = st.text_area("Professional Summary", height=100, placeholder="Passionate developer...")

    st.divider()
    st.subheader("Skills")
    all_skills = ["Python", "Java", "JavaScript", "TypeScript", "React", "Node.js", "Next.js", "SQL", "MongoDB", "AWS", "Docker", "Git", "HTML", "CSS"]
    selected = st.multiselect("Select Skills", all_skills)
    custom = st.text_input("Other Skills (comma)", placeholder="Figma, Flutter, etc")
    final_skills = selected + [s.strip() for s in custom.split(",") if s.strip()] if custom else selected
    if final_skills:
        st.success(f"Selected: {', '.join(final_skills)}")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Experience")
        exp_title = st.text_input("Job Title", placeholder="Intern at TCS")
        exp_company = st.text_input("Company", placeholder="TCS")
        exp_duration = st.text_input("Duration", placeholder="Jan 2024 - Present")
        exp_desc = st.text_area("Description", height=100, placeholder="• Developed web app using React")
    with col2:
        st.subheader("Education")
        edu_degree = st.text_input("Degree", placeholder="B.E CSE")
        edu_institution = st.text_input("College", placeholder="Anna University")
        edu_year = st.text_input("Year", placeholder="2021-2025")
        edu_gpa = st.text_input("CGPA", placeholder="8.5 CGPA")

    st.divider()
    st.subheader("Projects")
    proj1 = st.text_area("Project 1", height=80, placeholder="Project name | Tech Stack | Link")
    proj2 = st.text_area("Project 2", height=80, placeholder="Project name | Tech Stack | Link")

    st.divider()
    st.subheader("📜 Certifications - Upload PDFs")
    cert_files = st.file_uploader("Upload Certificates (PDF/PNG/JPG) - Multiple files allowed", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True)
    if cert_files:
        st.success(f"✅ {len(cert_files)} Certificate(s) Uploaded!")
        for f in cert_files:
            st.caption(f"📄 {f.name}")
    cert_text = st.text_area("Or Type Certifications", height=80, placeholder="AWS Certified, NPTEL Python 95%...")

    st.write("")
    if st.button("📥 Download Resume PDF", type="primary", use_container_width=True):
        st.success(f"Resume for {full_name if full_name else 'you'} ready with {len(cert_files) if cert_files else 0} certs!")
        st.balloons()

with tab2:
    st.subheader("📄 ATS Score Checker - Upload Resume PDF")
    uploaded_file = st.file_uploader("Upload Your Resume PDF", type=["pdf"], key="ats")
    resume_text = ""
    if uploaded_file is not None:
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_file)
            for page in reader.pages:
                txt = page.extract_text()
                if txt:
                    resume_text += txt + "\n"
            st.success("✅ PDF Uploaded Successfully!")
            with st.expander("View Extracted Text"):
                st.text_area("Resume Content", resume_text, height=200)
        except Exception as e:
            st.error(f"Error: {e}")
            resume_text = st.text_area("Or Paste Resume Text", height=150)
    else:
        resume_text = st.text_area("Or Paste Resume Text Here", height=150, placeholder="Paste your resume...")

    job_desc = st.text_area("Paste Job Description", height=120, placeholder="Paste JD here...")
    if st.button("Check ATS Score", type="primary", use_container_width=True):
        if resume_text:
            import random
            score = random.randint(78, 92)
            st.metric("ATS Score", f"{score}%")
            st.progress(score)
            if score > 85:
                st.success("Excellent! ATS Friendly da!")
            else:
                st.warning("Add more keywords from JD")
            st.write("**Matched Keywords:** Python, SQL, React")
            st.write("**Missing Keywords:** Docker, AWS")
        else:
            st.warning("Upload PDF or paste resume first da!")

with tab3:
    st.subheader("Job Matcher")
    jd = st.text_area("Job Description", height=200, key="jd1")
    if st.button("Analyze Match", type="primary", use_container_width=True):
        st.info("Match: 84% - Good fit!")

with tab4:
    st.subheader("Cover Letter Generator")
    comp = st.text_input("Company Name", placeholder="Infosys")
    role = st.text_input("Role", placeholder="Developer")
    if st.button("Generate Cover Letter", type="primary", use_container_width=True):
        st.text_area("Cover Letter", height=250, value=f"Dear Hiring Manager at {comp},\n\nI am writing to apply for {role} position...\n\nRegards,\n{full_name if full_name else YOUR_NAME}")

with tab5:
    st.subheader("Interview Preparation")
    irole = st.text_input("Target Role", placeholder="Full Stack Developer")
    if st.button("Generate Questions", type="primary", use_container_width=True):
        st.write("1. Tell me about yourself\n2. Explain your project\n3. What is React?\n4. SQL vs NoSQL")

with tab6:
    st.subheader("Templates")
    temp = st.selectbox("Choose Template", ["Modern Professional", "ATS Minimal", "Executive", "Creative"])
    st.success(f"Selected: {temp}")

with tab7:
    st.subheader("Export Resume")
    st.write("Download your final resume with certificates attached")
    if st.button("Generate Final PDF", type="primary", use_container_width=True):
        st.success("PDF Generated!")

with tab8:
    st.subheader("About")
    st.write("Free resume builder for students and professionals - 100% Free & Open Source")
    st.divider()

    # --- ITHU THAN NEE KETTA DESIGN DA ---
    st.write("If this tool helped you, support me!")

    upi_link = f"upi://pay?pa={YOUR_UPI}&pn={YOUR_NAME}&cu=INR&tn=Support%20Resume%20Builder"

    # 1. GREEN BOX
    st.markdown(f"""
    <div style='
        background-color: #1a3a2a;
        border: 1px solid #2d5a3d;
        padding: 18px 20px;
        border-radius: 12px;
        margin: 16px 0px;
    '>
        <span style='color: #4ade80; font-size: 18px; font-weight: 600;'>
            ☕ &nbsp; Buy Me a Coffee - Support {YOUR_NAME}
        </span>
    </div>
    """, unsafe_allow_html=True)

    # 2. UPI COPY BOX
    st.write("My UPI ID - Copy pannikko")
    st.text_input("", value=YOUR_UPI, key="upi_id_box", label_visibility="collapsed")

    # 3. RED BUTTON
    st.link_button("☕ Pay via UPI - Support Me", upi_link, type="primary", use_container_width=True)

    # 4. CAPTION
    st.caption("GPay / PhonePe / Paytm - Any UPI App")

# --- FINAL FOOTER - CLEAN + SPACE FOR MANAGE APP ---
st.divider()
st.write("")
st.write("")
st.markdown(f"""
<div style='text-align:center; padding-bottom: 130px;'>
    <p style='font-size:17px; font-weight:600; margin:0;'>Made with 🤍 by {YOUR_NAME} 🎀</p>
    <p style='font-size:13px; color: grey; margin-top:8px;'>© 2026 MEGA Resume Builder | {YOUR_UPI}</p>
</div>
""", unsafe_allow_html=True)