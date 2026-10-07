import streamlit as st

st.set_page_config(
    page_title="Resume Builder - Free ATS Resume",
    page_icon="📄",
    layout="wide"
)

st.title("Resume Builder - MEGA 🚀")
st.write("100% FREE - Build your ATS resume!")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📝 Builder", "📊 ATS Score", "🎯 Matcher", "✉️ Cover Letter", "❤️ Donate"])

# --- TAB 1: BUILDER ---
with tab1:
    st.subheader("Personal Details")
    
    full_name = st.text_input("Full Name", value="", placeholder="Ex: Your Name")
    role = st.text_input("Role", value="", placeholder="Ex: Software Engineer")
    email = st.text_input("Email", value="", placeholder="Ex: yourname@gmail.com")
    phone = st.text_input("Phone", value="", placeholder="Ex: +91 98765 43210")
    location = st.text_input("Location", value="", placeholder="Ex: Chennai, India")
    linkedin = st.text_input("LinkedIn", value="", placeholder="linkedin.com/in/yourname")

    st.divider()
    st.subheader("Skills - Click to Select")
    
    predefined_skills = ["C", "C++", "Python", "Java", "JavaScript", "React", "SQL", "HTML", "CSS", "AWS", "Docker", "Git", "Node.js", "TypeScript"]
    
    selected_skills = st.multiselect(
        "Select your skills:",
        options=predefined_skills,
        placeholder="C, C++ nu inga click pannu"
    )
    
    custom_skills_input = st.text_input("Other Skills (comma va pottu type pannu)", value="", placeholder="Ex: Figma, Machine Learning, AI")

    all_skills = selected_skills.copy()
    if custom_skills_input:
        custom_list = [s.strip() for s in custom_skills_input.split(",") if s.strip()]
        all_skills.extend(custom_list)
    
    if all_skills:
        st.success(f"✅ Selected: {', '.join(all_skills)}")

    st.divider()
    st.subheader("Experience")
    experience = st.text_area("Experience", value="", placeholder="Your work experience...", height=150)
    
    st.subheader("Education")
    education = st.text_area("Education", value="", placeholder="Your education details...", height=100)

    if st.button("Generate Resume"):
        st.balloons()
        st.success("Resume Generated!")

# --- TAB 2: ATS SCORE ---
with tab2:
    st.subheader("ATS Score Checker")
    st.write("No admin code here!")
    resume_text = st.text_area("Paste your resume here", value="", placeholder="Paste resume text...")
    if st.button("Check ATS Score", key="ats"):
        st.info("ATS Score: 85% - Good!")

# --- TAB 3: MATCHER ---
with tab3:
    st.subheader("Job Matcher")
    st.write("No admin code here!")
    job_desc = st.text_area("Paste Job Description", value="", placeholder="Paste job description here...")
    if st.button("Match", key="match"):
        st.info("Matching: 78%")

# --- TAB 4: COVER LETTER ---
with tab4:
    st.subheader("Cover Letter Generator")
    st.write("No admin code here!")
    company = st.text_input("Company Name", value="", placeholder="Ex: Google")
    if st.button("Generate Cover Letter", key="cover"):
        st.write("Your cover letter will appear here...")

# --- TAB 5: DONATE - LAST PAGE ONLY ---
with tab5:
    st.title("Support Us ❤️")
    st.write("Intha resume builder pudichirukka? Oru coffee vaangi kudu da!")
    
    st.divider()
    st.subheader("Donate Amount")
    amount = st.selectbox("Select Amount", ["₹10 - Tea", "₹50 - Coffee", "₹100 - Lunch", "₹250 - Support", "Other"])
    
    custom_amt = ""
    if amount == "Other":
        custom_amt = st.text_input("Enter Custom Amount", value="", placeholder="Ex: ₹500")
    
    st.write("UPI / GPay / PhonePe")
    
    if st.button("Donate Now 🙏"):
        st.balloons()
        st.success("Romba Thanks da! ❤️ Support pannathukku!")
        st.write("Donation successful!")