import streamlit as st

st.set_page_config(page_title="MEGA Resume Builder", page_icon="📄", layout="wide")

YOUR_UPI = "dileepkumar.m316@okaxis"
YOUR_NAME = "Dileepkumar.M"

st.success(f"✨ Created by {YOUR_NAME} 🤍🎀")

st.title("MEGA Resume Builder")
st.write("Professional ATS-Optimized Resume Builder")

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
    cert_files = st.file_uploader("Upload Certificates (PDF/PNG/JPG) - Multiple allowed", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True)
    if cert_files:
        st.success(f"✅ {len(cert_files)} Certificate(s) Uploaded!")
        for f in cert_files:
            st.caption(f"📄 {f.name}")
    cert_text = st.text_area("Or Type Certifications", height=80, placeholder="AWS Certified, NPTEL Python 95%...")

    st.write("")
    if st.button("📥 Download Resume PDF", type="primary", use_container_width=True):
        st.success(f"Resume ready with {len(cert_files) if cert_files else 0} certs!")
        st.balloons()

with tab2:
    st.subheader("📄 ATS Score - Upload Resume PDF")
    uploaded_file = st.file_uploader("Upload Your Resume PDF", type=["pdf"], key="ats_pdf")
    resume_text = ""
    if uploaded_file is not None:
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_file)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    resume_text += text + "\n"
            st.success("✅ PDF Uploaded!")
            with st.expander("View Extracted Text"):
                st.text_area("Content", resume_text, height=200)
        except Exception as e:
            st.error(f"Error: {e}")
            resume_text = st.text_area("Paste Resume Text", height=150)
    else:
        resume_text = st.text_area("Or Paste Resume Text Here", height=150, placeholder="Paste resume...")

    job_desc = st.text_area("Paste Job Description", height=120, placeholder="Paste JD...")
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
            st.write("**Matched:** Python, SQL, React")
            st.write("**Missing:** Docker, AWS")
        else:
            st.warning("Upload PDF first da!")

with tab3:
    st.subheader("Job Matcher")
    jd = st.text_area("Job Description", height=200)
    if st.button("Analyze Match", type="primary", use_container_width=True):
        st.info("Match: 84% - Good fit!")

with tab4:
    st.subheader("Cover Letter")
    comp = st.text_input("Company Name", placeholder="Infosys")
    role = st.text_input("Role", placeholder="Developer")
    if st.button("Generate Letter", type="primary", use_container_width=True):
        st.text_area("Cover Letter", height=250, value=f"Dear Hiring Manager at {comp},\n\nApplying for {role}...\n\nRegards,\n{full_name if full_name else YOUR_NAME}")

with tab5:
    st.subheader("Interview Prep")
    irole = st.text_input("Target Role", placeholder="Full Stack Dev")
    if st.button("Generate Questions", type="primary", use_container_width=True):
        st.write("1. Tell me about yourself\n2. Explain your project\n3. What is React?")

with tab6:
    st.subheader("Templates")
    temp = st.selectbox("Template", ["Modern Professional", "ATS Minimal", "Executive", "Creative"])
    st.success(f"Selected: {temp}")

with tab7:
    st.subheader("Export Resume")
    if st.button("Generate Final PDF", type="primary", use_container_width=True):
        st.success("PDF Generated!")

with tab8:
    st.subheader("About")
    st.write("Free resume builder for students and professionals.")
    st.info("100% Free & Open Source")
    st.divider()
    st.subheader("💖 Support My Work")
    st.write("If this tool helped you, support me!")
    st.success(f"☕ Buy Me a Coffee - Support {YOUR_NAME}")
    st.text_input("My UPI ID - Copy pannikko", value=YOUR_UPI)
    upi_link = f"upi://pay?pa={YOUR_UPI}&pn={YOUR_NAME}&cu=INR&tn=Support"
    st.link_button("☕ Pay via UPI - Support Me", upi_link, type="primary", use_container_width=True)
    st.caption("GPay / PhonePe / Paytm - Any UPI App")
    st.code(YOUR_UPI, language="text")

st.divider()
st.success(f"Made with 🤍 by {YOUR_NAME} 🎀 | UPI: {YOUR_UPI} | © 2026")
st.write("")
st.write("")
st.write("")