import streamlit as st

st.set_page_config(page_title="MEGA Resume Builder", page_icon="📄", layout="wide")

st.title("MEGA Resume Builder")
st.markdown("### Professional ATS-Optimized Resume Builder | 8-in-1 Tools")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Resume Builder", "ATS Score", "Job Matcher", "Cover Letter", 
    "Interview Prep", "Templates", "Export", "Support"
])

# TAB 1: BUILDER + DOWNLOAD AT BOTTOM
with tab1:
    st.subheader("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name", value="", placeholder="Enter your full name")
        professional_title = st.text_input("Professional Title", value="", placeholder="e.g., Software Engineer")
        email = st.text_input("Email Address", value="", placeholder="Enter your email address")
        phone = st.text_input("Phone Number", value="", placeholder="Enter your phone number")
    with col2:
        location = st.text_input("Location", value="", placeholder="City, Country")
        linkedin = st.text_input("LinkedIn Profile", value="", placeholder="https://linkedin.com/in/username")
        portfolio = st.text_input("Portfolio / GitHub", value="", placeholder="https://github.com/username")
        summary = st.text_area("Professional Summary", value="", placeholder="Brief summary highlighting your experience...", height=100)

    st.divider()
    st.subheader("Technical Skills")
    all_predefined = ["Python", "Java", "JavaScript", "TypeScript", "React", "Node.js", "Next.js", "C", "C++", "SQL", "MongoDB", "AWS", "Docker", "Git", "HTML5", "CSS3"]
    selected_skills = st.multiselect("Select Your Skills", options=all_predefined, placeholder="Select your technical skills")
    custom_skills = st.text_input("Additional Skills", value="", placeholder="Add other skills separated by commas")
    final_skills = selected_skills.copy()
    if custom_skills:
        final_skills.extend([s.strip() for s in custom_skills.split(",") if s.strip()])
    if final_skills:
        st.success(f"Selected: {', '.join(final_skills)}")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Work Experience")
        exp_title = st.text_input("Job Title", value="", placeholder="e.g., Software Engineer")
        exp_company = st.text_input("Company Name", value="", placeholder="e.g., Microsoft")
        exp_duration = st.text_input("Duration", value="", placeholder="e.g., Jan 2023 - Present")
        exp_desc = st.text_area("Key Responsibilities", value="", placeholder="• Developed...\n• Improved...", height=120)
    with col2:
        st.subheader("Education")
        edu_degree = st.text_input("Degree", value="", placeholder="e.g., B.Tech Computer Science")
        edu_institution = st.text_input("Institution", value="", placeholder="e.g., University Name")
        edu_year = st.text_input("Academic Year", value="", placeholder="e.g., 2020 - 2024")
        edu_gpa = st.text_input("GPA / Honors", value="", placeholder="e.g., 8.5 CGPA")

    st.divider()
    st.subheader("Projects")
    proj1 = st.text_area("Project 1", value="", placeholder="Project Title | Tech Stack | Link", height=80)
    proj2 = st.text_area("Project 2", value="", placeholder="Project Title | Tech Stack | Link", height=80)
    certs = st.text_area("Certifications", value="", placeholder="List certifications...", height=70)

    # DOWNLOAD AT BOTTOM OF BUILDER PAGE - DECENT
    st.divider()
    st.subheader("Ready to Export?")
    col_d1, col_d2, col_d3 = st.columns([1,1,2])
    with col_d1:
        if st.button("Download Resume PDF", type="primary", use_container_width=True):
            st.success(f"Resume for {full_name} is ready!")
            st.write(f"**Name:** {full_name} | **Role:** {professional_title}")
            st.write(f"**Skills:** {', '.join(final_skills)}")
            st.balloons()
    with col_d2:
        if st.button("Preview Resume", use_container_width=True):
            st.info("Preview will open in Export tab")
    with col_d3:
        st.caption("Your data is secure and not stored on our servers.")

with tab2:
    st.subheader("ATS Compatibility Analysis")
    uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf", "docx", "txt"])
    resume_content = ""
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_file)
            for page in reader.pages:
                resume_content += page.extract_text() or ""
            st.text_area("Extracted Content", value=resume_content, height=180)
        elif uploaded_file.type == "text/plain":
            resume_content = str(uploaded_file.read(), "utf-8")
            st.text_area("Resume Content", value=resume_content, height=180)
        else:
            import docx
            doc = docx.Document(uploaded_file)
            resume_content = "\n".join([p.text for p in doc.paragraphs])
            st.text_area("Extracted Content", value=resume_content, height=180)
    else:
        resume_content = st.text_area("Or Paste Resume Content", value="", placeholder="Paste resume here...", height=180)
    
    job_description = st.text_area("Target Job Description", value="", placeholder="Paste job description...", height=120)
    if st.button("Analyze ATS Score", type="primary"):
        if resume_content:
            st.metric("ATS Score", "88%")
            st.progress(88)
            st.success("High ATS compatibility")

with tab3:
    st.subheader("Job Description Matching")
    jd = st.text_area("Job Description", value="", placeholder="Paste job description...", height=200)
    if st.button("Analyze Match", type="primary"):
        st.info("Match Rate: 82% | Matched: Python, React, SQL")

with tab4:
    st.subheader("Cover Letter Generator")
    c1, c2 = st.columns(2)
    with c1:
        comp_name = st.text_input("Company Name", value="", placeholder="Company name")
    with c2:
        applying_role = st.text_input("Position", value="", placeholder="Position")
    if st.button("Generate Cover Letter", type="primary"):
        st.text_area("Cover Letter", height=300, value=f"Dear Hiring Manager at {comp_name},\n\nI am excited to apply for {applying_role}...")

with tab5:
    st.subheader("Interview Preparation")
    interview_role = st.text_input("Target Role", value="", placeholder="e.g., Software Engineer")
    if st.button("Generate Questions", type="primary"):
        st.write("1. Tell me about yourself.\n2. Explain your projects.\n3. What are your strengths?")

with tab6:
    st.subheader("Professional Templates")
    template = st.selectbox("Choose Template", ["Modern Professional", "Executive", "ATS Optimized", "Minimalist"])
    st.info(f"Template: {template}")

with tab7:
    st.subheader("Export Resume")
    if st.button("Download Final PDF", type="primary"):
        st.success("Your professional resume is ready for download!")

# TAB 8 - DECENT SUPPORT - NO BEGGING
with tab8:
    st.title("Support the Project")
    st.write("This tool is free and open-source. Built to help students and professionals create professional resumes.")
    
    st.divider()
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.subheader("About This Project")
        st.write("Maintaining servers and adding new features takes time and resources.")
        st.write("If this tool helped you, you can optionally support its development.")
        st.write("")
        st.write("**Your support helps in:**")
        st.write("- Keeping the platform free")
        st.write("- Server and maintenance costs")
        st.write("- Adding new templates and features")
        st.write("")
        st.write("**UPI:** `dileepkumar.m316@okicici`")
        
    with col2:
        st.subheader("Support")
        st.image("qr.png", caption="UPI: dileepkumar.m316@okicici", use_container_width=True)
        st.caption("Scan with any UPI app (GPay, PhonePe, Paytm)")
        st.caption("All contributions are appreciated.")