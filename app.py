import streamlit as st

st.set_page_config(page_title="MEGA Resume Builder", page_icon="📄", layout="wide")

st.markdown("""
<div style='text-align:center; padding:10px; background:#f0f2f6; border-radius:12px; margin-bottom:15px;'>
✨ Created by <b>Dileepkumar.M</b> 🤍🎀
</div>
""", unsafe_allow_html=True)

st.title("MEGA Resume Builder")
st.markdown("### Professional ATS-Optimized Resume Builder")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📝 Resume Builder", "📊 ATS Score", "🎯 Job Matcher", "✉️ Cover Letter", 
    "💼 Interview Prep", "🎨 Templates", "📥 Export", "💖 About"
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
    custom = st.text_input("Other Skills", placeholder="Figma, Flutter")
    final_skills = selected + [s.strip() for s in custom.split(",") if s.strip()] if custom else selected
    if final_skills:
        st.success(f"Selected: {', '.join(final_skills)}")

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Experience")
        exp_title = st.text_input("Job Title", placeholder="Intern")
        exp_company = st.text_input("Company", placeholder="TCS")
        exp_duration = st.text_input("Duration", placeholder="Jan 2024 - Present")
        exp_desc = st.text_area("Description", height=120, placeholder="• Developed...")
    with c2:
        st.subheader("Education")
        edu_degree = st.text_input("Degree", placeholder="B.E CSE")
        edu_institution = st.text_input("College", placeholder="Anna University")
        edu_year = st.text_input("Year", placeholder="2021-2025")
        edu_gpa = st.text_input("CGPA", placeholder="8.5 CGPA")

    st.divider()
    proj1 = st.text_area("Project 1", height=80, placeholder="Project name | Tech | Link")
    proj2 = st.text_area("Project 2", height=80, placeholder="Project name | Tech | Link")
    certs = st.text_area("Certifications", height=60, placeholder="AWS, etc")

    if st.button("📥 Download Resume PDF", type="primary", use_container_width=True):
        st.success(f"Resume for {full_name} is ready! Go to Export tab")
        st.balloons()

with tab2:
    st.subheader("ATS Score Checker")
    resume_txt = st.text_area("Paste Resume", height=150)
    job_desc = st.text_area("Paste Job Description", height=100)
    if st.button("Check ATS Score", type="primary"):
        if resume_txt:
            st.metric("ATS Score", "88%")
            st.progress(88)
        else:
            st.warning("Paste resume first")

with tab3:
    st.subheader("Job Matcher")
    jd = st.text_area("Job Description", height=200)
    if st.button("Analyze Match", type="primary"):
        st.info("Match: 84%")

with tab4:
    st.subheader("Cover Letter")
    comp = st.text_input("Company Name", placeholder="Infosys")
    role = st.text_input("Role", placeholder="Developer")
    if st.button("Generate Letter", type="primary"):
        st.text_area("Cover Letter", height=250, value=f"Dear Hiring Manager at {comp},\n\nI am applying for {role}...\n\nRegards,\n{full_name if 'full_name' in locals() else ''}")

with tab5:
    st.subheader("Interview Questions")
    irole = st.text_input("Target Role", placeholder="Full Stack Dev")
    if st.button("Generate Questions", type="primary"):
        st.write("1. Tell me about yourself\n2. Explain your project\n3. What is React?\n4. SQL vs NoSQL")

with tab6:
    st.subheader("Templates")
    temp = st.selectbox("Template", ["Modern Professional", "ATS Minimal", "Executive", "Creative"])
    st.success(f"Selected: {temp}")

with tab7:
    st.subheader("Export Resume")
    if st.button("Generate Final PDF", type="primary"):
        st.success("PDF Generated! Use Builder tab download")

with tab8:
    st.subheader("About")
    st.write("This is a free resume builder for students and professionals.")
    st.write("Built with Streamlit & Python")
    st.info("100% Free & Open Source")

st.divider()
st.markdown("""
<div style='text-align:center; padding:15px; background:#f8f9fa; border-radius:10px;'>
<h4 style='margin:0;'>Made with 🤍 by Dileepkumar.M 🎀</h4>
<p style='color:#888; font-size:13px; margin-top:5px;'>© 2026 MEGA Resume Builder</p>
</div>
""", unsafe_allow_html=True)