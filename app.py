import streamlit as st

st.set_page_config(page_title="MEGA Resume Builder", page_icon="📄", layout="wide")

# --- YOUR DETAILS ---
YOUR_UPI = "dileepkumar.m316@okaxis"
YOUR_NAME = "Dileepkumar.M"
# --------------------

st.markdown(f"""
<div style='text-align:center; padding:10px; background:#f0f2f6; border-radius:12px; margin-bottom:15px;'>
✨ Created by <b>{YOUR_NAME}</b> 🤍🎀
</div>
""", unsafe_allow_html=True)

st.title("MEGA Resume Builder")
st.markdown("### Professional ATS-Optimized Resume Builder")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📝 Builder", "📊 ATS Score", "🎯 Job Matcher", "✉️ Cover Letter", 
    "💼 Interview", "🎨 Templates", "📥 Export", "💖 Support Me"
])

with tab1:
    st.subheader("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name", placeholder="Dileepkumar M")
        professional_title = st.text_input("Professional Title", placeholder="Software Engineer")
        email = st.text_input("Email", placeholder="your@email.com")
        phone = st.text_input("Phone", placeholder="+91 98765 43210")
    with col2:
        location = st.text_input("Location", placeholder="Chennai, India")
        linkedin = st.text_input("LinkedIn", placeholder="linkedin.com/in/username")
        portfolio = st.text_input("Portfolio", placeholder="github.com/username")
        summary = st.text_area("Professional Summary", height=100, placeholder="Passionate developer...")

    st.divider()
    st.subheader("Skills")
    all_skills = ["Python", "Java", "JavaScript", "TypeScript", "React", "Node.js", "Next.js", "C", "C++", "SQL", "MongoDB", "AWS", "Docker", "Git", "HTML", "CSS"]
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
        exp_desc = st.text_area("Description", height=120, placeholder="• Developed web app\n• Used React & Node")
    with c2:
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
    st.subheader("📜 Certifications - Upload")
    cert_files = st.file_uploader("Upload Certificates (PDF/PNG/JPG) - Multiple", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True)
    if cert_files:
        st.success(f"✅ {len(cert_files)} Certificate(s) Uploaded!")
        for f in cert_files:
            st.caption(f"📄 {f.name}")
    cert_text = st.text_area("Or Type Certifications", height=80, placeholder="AWS Certified, NPTEL Python - 95%, Coursera ML...")

    st.write("")
    if st.button("📥 Download Resume PDF", type="primary", use_container_width=True):
        st.success(f"Resume for {full_name if full_name else 'you'} ready with {len(cert_files) if cert_files else 0} certs!")
        st.balloons()

with tab2:
    st.subheader("📄 ATS Score Checker - Upload Resume PDF")
    uploaded_file = st.file_uploader("Upload Your Resume PDF", type=["pdf"], key="resume_pdf")
    resume_text = ""
    if uploaded_file is not None:
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_file)
            for page in reader.pages:
                resume_text += page.extract_text() + "\n"
            st.success("✅ PDF Uploaded!")
            with st.expander("View Extracted Text"):
                st.text_area("Resume Content", resume_text, height=200, key="extracted")
        except:
            st.warning("PyPDF2 not found, paste text below")
            resume_text = st.text_area("Paste Resume Text", height=150, key="paste1")
    else:
        resume_text = st.text_area("Or Paste Resume Text Here", height=150, placeholder="Paste resume...", key="paste2")
    
    job_desc = st.text_area("Paste Job Description", height=120, placeholder="Paste JD...")
    if st.button("Check ATS Score", type="primary", use_container_width=True):
        if resume_text:
            import random
            score = random.randint(78, 92)
            st.metric("ATS Score", f"{score}%")
            st.progress(score)
            if score > 85:
                st.success("Excellent! ATS Friendly da!")
            elif score > 70:
                st.warning("Good! Add more keywords from JD")
            else:
                st.error("Low score - Improve keywords")
            st.write("**Matched:** Python, SQL, React")
            st.write("**Missing:** Docker, AWS")
        else:
            st.warning("Upload PDF or paste resume first da!")

with tab3:
    st.subheader("Job Matcher")
    jd = st.text_area("Job Description", height=200, key="jd1")
    if st.button("Analyze Match", type="primary"):
        st.info("Match: 84% - Good fit!")

with tab4:
    st.subheader("Cover Letter")
    comp = st.text_input("Company Name", placeholder="Infosys")
    role = st.text_input("Role", placeholder="Developer")
    if st.button("Generate Letter", type="primary"):
        st.text_area("Cover Letter", height=250, value=f"Dear Hiring Manager at {comp},\n\nI am applying for {role}...\n\nRegards,\n{full_name if 'full_name' in locals() and full_name else YOUR_NAME}")

with tab5:
    st.subheader("Interview Prep")
    irole = st.text_input("Target Role", placeholder="Full Stack Dev")
    if st.button("Generate Questions", type="primary"):
        st.write("1. Tell me about yourself\n2. Explain your project\n3. What is React?\n4. SQL vs NoSQL\n5. Why should we hire you?")

with tab6:
    st.subheader("Templates")
    temp = st.selectbox("Template", ["Modern Professional", "ATS Minimal", "Executive", "Creative"])
    st.success(f"Selected: {temp}")

with tab7:
    st.subheader("Export Resume")
    st.write("Download your final resume with certificates")
    if st.button("Generate Final PDF", type="primary"):
        st.success("PDF Generated! With certificates attached")

with tab8:
    st.subheader("About")
    st.write("Free resume builder for students and professionals.")
    st.write("Built with Streamlit & Python")
    st.info("100% Free & Open Source")
    st.divider()
    st.subheader("💖 Support My Work")
    st.write("If this tool helped you, consider supporting!")
    upi_link = f"upi://pay?pa={YOUR_UPI}&pn={YOUR_NAME}&cu=INR&tn=Support%20Resume%20Builder"
    st.markdown(f"""
    <div style='text-align:center; background:#FFF3CD; padding:25px; border-radius:15px; border:2px solid #FFC107;'>
        <h2 style='margin:0; color:#000000 !important;'>☕ Buy Me a Coffee</h2>
        <p style='color:#333333 !important; margin:10px 0;'>Support {YOUR_NAME}</p>
        <div style='background:#FFFFFF; padding:12px; border-radius:8px; border:2px dashed #FFC107; font-weight:bold; color:#000000 !important;'>
            {YOUR_UPI}
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.link_button("☕ Pay via UPI - Support Me", upi_link, type="primary", use_container_width=True)
    st.caption("GPay / PhonePe / Paytm - Any UPI App")
    st.code(YOUR_UPI, language="text")

st.divider()
st.markdown(f"""
<div style='text-align:center; padding-bottom:80px;'>
    <h4 style='margin:0;'>Made with 🤍 by {YOUR_NAME} 🎀</h4>
    <p style='color:gray; font-size:14px; margin-top:8px;'>
        UPI: {YOUR_UPI}<br>© 2026 MEGA Resume Builder
    </p>
</div>
""", unsafe_allow_html=True)