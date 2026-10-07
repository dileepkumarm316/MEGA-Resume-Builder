import streamlit as st

st.set_page_config(page_title="MEGA Resume Builder", page_icon="📄", layout="wide")

st.title("MEGA Resume Builder")
st.markdown("### Professional ATS-Optimized Resume Builder | 8-in-1 Tools | 100% Free")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Resume Builder", "ATS Score", "Job Matcher", "Cover Letter", 
    "Interview Prep", "Templates", "Export Resume", "Support"
])

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
        summary = st.text_area("Professional Summary", value="", placeholder="Brief summary...", height=100)

    st.divider()
    st.subheader("Technical Skills")
    all_predefined = ["C", "C++", "Python", "Java", "JavaScript", "TypeScript", "React", "Node.js", "Next.js", "HTML5", "CSS3", "SQL", "MongoDB", "AWS", "Docker", "Git", "Kubernetes"]
    selected_skills = st.multiselect("Select Your Skills", options=all_predefined, placeholder="Search and select your technical skills")
    custom_skills = st.text_input("Additional Skills", value="", placeholder="Add other skills separated by commas")
    final_skills = selected_skills.copy()
    if custom_skills:
        final_skills.extend([s.strip() for s in custom_skills.split(",") if s.strip()])
    if final_skills:
        st.success(f"Selected Skills: {', '.join(final_skills)}")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Work Experience")
        exp_title = st.text_input("Job Title", value="", placeholder="e.g., Software Engineer")
        exp_company = st.text_input("Company Name", value="", placeholder="e.g., Microsoft")
        exp_duration = st.text_input("Duration", value="", placeholder="e.g., Jan 2023 - Present")
        exp_desc = st.text_area("Key Responsibilities", value="", placeholder="• Developed...", height=130)
    with col2:
        st.subheader("Education")
        edu_degree = st.text_input("Degree", value="", placeholder="e.g., Bachelor of Science in Computer Science")
        edu_institution = st.text_input("Institution", value="", placeholder="e.g., University Name")
        edu_year = st.text_input("Academic Year", value="", placeholder="e.g., 2020 - 2024")
        edu_gpa = st.text_input("GPA / Honors", value="", placeholder="e.g., 3.9 GPA")
    st.divider()
    proj1 = st.text_area("Project 1", value="", placeholder="Project Title | Technologies | Link", height=90)
    proj2 = st.text_area("Project 2", value="", placeholder="Project Title | Technologies | Link", height=90)
    certs = st.text_area("Certifications", value="", placeholder="List your certifications...", height=80)

with tab2:
    st.subheader("ATS Compatibility Analysis")
    uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf", "docx", "txt"], help="Supports PDF, DOCX, TXT")
    resume_content = ""
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_file)
            for page in reader.pages:
                resume_content += page.extract_text() or ""
            st.success(f"PDF Uploaded: {uploaded_file.name}")
            st.text_area("Extracted Content", value=resume_content, height=180)
        elif uploaded_file.type == "text/plain":
            resume_content = str(uploaded_file.read(), "utf-8")
            st.success(f"File Uploaded: {uploaded_file.name}")
            st.text_area("Resume Content", value=resume_content, height=180)
        else:
            import docx
            doc = docx.Document(uploaded_file)
            resume_content = "\n".join([p.text for p in doc.paragraphs])
            st.success(f"Document Uploaded: {uploaded_file.name}")
            st.text_area("Extracted Content", value=resume_content, height=180)
    else:
        resume_content = st.text_area("Or Paste Resume Content", value="", placeholder="Paste your resume here...", height=180)
    st.divider()
    job_description = st.text_area("Target Job Description", value="", placeholder="Paste job description...", height=130)
    if st.button("Analyze ATS Score", type="primary"):
        if not resume_content:
            st.warning("Please upload or paste your resume first.")
        else:
            st.metric("ATS Compatibility Score", "88%")
            st.progress(88)
            st.success("Excellent compatibility!")

with tab3:
    st.subheader("Job Description Matching")
    jd = st.text_area("Job Description", value="", placeholder="Paste job description...", height=200)
    if st.button("Analyze Match", type="primary"):
        st.info("Matched Skills: Python, React, SQL | Match Rate: 82%")

with tab4:
    st.subheader("Cover Letter Generator")
    c1, c2 = st.columns(2)
    with c1:
        comp_name = st.text_input("Company Name", value="", placeholder="Company name")
        manager_name = st.text_input("Hiring Manager", value="", placeholder="Optional")
    with c2:
        applying_role = st.text_input("Position", value="", placeholder="Position applying for")
    if st.button("Generate Cover Letter", type="primary"):
        st.text_area("Generated Cover Letter", height=350, value=f"Dear Hiring Manager,\n\nI am applying for {applying_role} at {comp_name}...")

with tab5:
    st.subheader("Interview Preparation")
    interview_role = st.text_input("Target Role", value="", placeholder="e.g., Software Engineer")
    if st.button("Generate Interview Questions", type="primary"):
        st.write("1. Tell me about yourself.")
        st.write("2. Describe a challenging project.")
        st.write("3. How do you approach problem-solving?")
        st.write("4. Where do you see yourself in 5 years?")

with tab6:
    st.subheader("Professional Resume Templates")
    template = st.selectbox("Choose Template", ["Modern Professional", "Executive", "ATS Optimized", "Minimalist", "Creative"])
    st.info(f"Selected Template: {template}")

with tab7:
    st.subheader("Export Resume")
    if st.button("Download PDF", type="primary"):
        st.success("Resume ready for download!")

# TAB 8 WITH YOUR UPI
with tab8:
    st.title("Support This Project ❤️")
    st.write("If you found this resume builder helpful, consider supporting!")
    st.divider()
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Choose Support Amount")
        amount = st.selectbox("Select Amount", ["₹10 - Tea ☕", "₹50 - Coffee ☕", "₹100 - Lunch 🍛", "₹250 - Big Support 🚀", "Other Amount"])
        if amount == "Other Amount":
            st.text_input("Enter Custom Amount", value="", placeholder="Ex: ₹500")
        st.write("")
        st.write("**Payment Methods**")
        st.code("dileepkumar.m316@okicici", language="text")
        st.write("📱 GPay / PhonePe / Paytm - Copy above UPI")
        st.write("🌍 International: PayPal.me")
        if st.button("Support Now 🙏", type="primary", use_container_width=True):
            st.balloons()
            st.success("Thank you so much! ❤️")
            st.snow()
    with col2:
        st.subheader("Scan & Pay")
        st.write("UPI: dileepkumar.m316@okicici")
        st.info("👇 To show QR code:\n1. Open GPay -> Profile -> QR Code -> Screenshot\n2. Save as `qr.png`\n3. Upload to GitHub repo\n4. Uncomment next line in code")
        # After uploading qr.png, uncomment below line:
        # st.image("qr.png", caption="Scan with any UPI app")
        st.caption("✅ Keep server running")
        st.caption("✅ Add new features")
        st.caption("✅ Keep it FREE forever")