import streamlit as st

st.set_page_config(page_title="MEGA Resume Builder", page_icon="📄", layout="wide")

st.title("MEGA Resume Builder")
st.markdown("### Professional ATS-Optimized Resume Builder | 8-in-1 Tools")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Resume Builder", "ATS Score", "Job Matcher", "Cover Letter", 
    "Interview Prep", "Templates", "Export", "Support"
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
        exp_desc = st.text_area("Key Responsibilities", value="", placeholder="• Developed...", height=120)
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

    # DOWNLOAD AT BOTTOM - AS YOU ASKED
    st.divider()
    st.subheader("Ready to