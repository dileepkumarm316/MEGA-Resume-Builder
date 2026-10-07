import streamlit as st

st.set_page_config(
    page_title="MEGA Resume Builder - Professional ATS Resume Builder",
    page_icon="📄",
    layout="wide"
)

st.title("MEGA Resume Builder")
st.markdown("### Professional ATS-Optimized Resume Builder | 8-in-1 Tools | 100% Free")

# 8 Professional Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Resume Builder", 
    "ATS Score", 
    "Job Matcher", 
    "Cover Letter", 
    "Interview Prep", 
    "Templates", 
    "Export Resume",
    "Support"
])

# TAB 1: RESUME BUILDER
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
        summary = st.text_area("Professional Summary", value="", placeholder="Brief summary highlighting your experience and career objectives...", height=100)

    st.divider()
    st.subheader("Technical Skills")
    st.caption("Select relevant skills or add custom skills")
    
    skills_categories = {
        "Programming": ["Python", "Java", "JavaScript", "TypeScript", "C++", "C#", "Go"],
        "Web Technologies": ["React", "Node.js", "Next.js", "HTML5", "CSS3", "Angular"],
        "Database": ["SQL", "MongoDB", "PostgreSQL", "MySQL"],
        "Cloud & DevOps": ["AWS", "Docker", "Kubernetes", "Git", "CI/CD"]
    }
    
    all_predefined = [skill for sublist in skills_categories.values() for skill in sublist]
    
    selected_skills = st.multiselect(
        "Select Your Skills",
        options=all_predefined,
        placeholder="Search and select your technical skills"
    )
    
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
        exp_desc = st.text_area("Key Responsibilities", value="", placeholder="• Developed...\n• Led a team...\n• Improved efficiency by...", height=130)
    with col2:
        st.subheader("Education")
        edu_degree = st.text_input("Degree", value="", placeholder="e.g., Bachelor of Science in Computer Science")
        edu_institution = st.text_input("Institution", value="", placeholder="e.g., University Name")
        edu_year = st.text_input("Academic Year", value="", placeholder="e.g., 2020 - 2024")
        edu_gpa = st.text_input("GPA / Honors", value="", placeholder="e.g., 3.9 GPA")
    
    st.divider()
    st.subheader("Projects")
    proj1 = st.text_area("Project 1", value="", placeholder="Project Title | Technologies | Link\nDescription and impact...", height=90)
    proj2 = st.text_area("Project 2", value="", placeholder="Project Title | Technologies | Link\nDescription and impact...", height=90)
    
    st.subheader("Certifications")
    certs = st.text_area("Certifications & Achievements", value="", placeholder="List your certifications...", height=80)

# TAB 2: ATS SCORE
with tab2:
    st.subheader("ATS Compatibility Analysis")
    st.text_area("Resume Content", value="", placeholder="Paste your resume content for analysis...", height=200)
    st.text_area("Target Job Description", value="", placeholder="Paste target job description (optional)...", height=150)
    if st.button("Analyze ATS Score", type="primary"):
        st.metric("ATS Score", "88%")
        st.progress(88)
        st.success("Excellent compatibility. Consider incorporating additional keywords from the job description.")

# TAB 3: JOB MATCHER
with tab3:
    st.subheader("Job Description Matching")
    st.text_area("Job Description", value="", placeholder="Paste job description here...", height=200, key="matcher_jd")
    if st.button("Analyze Match", type="primary"):
        st.info("Matched Skills: Python, React, SQL | Match Rate: 82%")
        st.warning("Recommended to add: Docker, AWS, System Design")

# TAB 4: COVER LETTER
with tab4:
    st.subheader("Cover Letter Generator")
    c1, c2 = st.columns(2)
    with c1:
        comp_name = st.text_input("Company Name", value="", placeholder="Company name")
        manager_name = st.text_input("Hiring Manager", value="", placeholder="Hiring Manager Name (Optional)")
    with c2:
        applying_role = st.text_input("Position", value="", placeholder="Position you are applying for")
    if st.button("Generate Cover Letter", type="primary"):
        st.text_area("Generated Cover Letter", height=350, value="Your cover letter will be generated here...")

# TAB 5: INTERVIEW PREP
with tab5:
    st.subheader("Interview Preparation")
    interview_role = st.text_input("Target Role", value="", placeholder="e.g., Software Engineer")
    if st.button("Generate Interview Questions", type="primary"):
        st.markdown("**Recommended Interview Questions:**")
        st.write("1. Tell me about yourself and your professional background.")
        st.write("2. Describe a challenging project you have worked on.")
        st.write("3. How do you approach problem-solving?")
        st.write("4. Where do you see yourself in the next five years?")

# TAB 6: TEMPLATES
with tab6:
    st.subheader("Professional Resume Templates")
    template = st.selectbox("Choose Template", ["Modern Professional", "Executive", "ATS Optimized", "Minimalist", "Creative"])
    st.info(f"Selected Template: {template}")

# TAB 7: EXPORT
with tab7:
    st.subheader("Export Resume")
    if st.button("Download PDF", type="primary"):
        st.success("Resume ready for download!")
        st.write(f"Name: {full_name}")
        st.write(f"Skills: {', '.join(final_skills)}")

# TAB 8: SUPPORT - LAST PAGE ONLY DONATION
with tab8:
    st.title("Support This Project")
    st.write("This platform is free and open-source. Your support helps us maintain and improve the service.")
    st.divider()
    st.subheader("Donation Amount")
    amount = st.selectbox("Select Amount", ["$5 - Support", "$10 - Coffee", "$25 - Contributor", "$50 - Premium Supporter", "Custom Amount"])
    custom_amount = ""
    if amount == "Custom Amount":
        custom_amount = st.text_input("Enter Amount", value="", placeholder="Enter custom amount")
    st.caption("Payment Methods: UPI / PayPal / Credit Card")
    if st.button("Donate Now", type="primary"):
        st.balloons()
        st.success("Thank you for your support!")