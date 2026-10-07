import streamlit as st
from fpdf import FPDF
import base64

st.set_page_config(
    page_title="Mega Resume Builder",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Mega Resume Builder")
st.caption("Professional Resume Builder - No personal data stored")

# 5 Tabs - Apdiye irukku
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👤 Personal", 
    "🎓 Education", 
    "💼 Internship", 
    "📝 Projects", 
    "📄 Preview & Download"
])

# --- TAB 1: PERSONAL (UN NAME ILLA) ---
with tab1:
    st.header("Personal Information")
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Full Name *", key="full_name", value="", placeholder="e.g., Enter your full name")
        email = st.text_input("Email Address *", key="email_id", value="", placeholder="e.g., your.email@example.com")
        location = st.text_input("Location", key="loc", value="", placeholder="e.g., Chennai, Tamil Nadu")
        linkedin = st.text_input("LinkedIn URL", key="linkedin_url", value="", placeholder="e.g., https://linkedin.com/in/yourname")
    with c2:
        pro_title = st.text_input("Professional Title", key="pro_title", value="", placeholder="e.g., Electronics & Communication Engineer")
        phone = st.text_input("Phone Number", key="phone_num", value="", placeholder="e.g., +91 9876543210")
        github = st.text_input("GitHub / Portfolio", key="github_url", value="", placeholder="e.g., https://github.com/yourname")
        summary = st.text_area("Professional Summary", key="summary", value="", placeholder="e.g., Passionate engineer with skills in Embedded Systems, IoT...")

# --- TAB 2: EDUCATION (UN COLLEGE NAME ILLA) ---
with tab2:
    st.header("Education")
    st.markdown("From your screenshot - same fields, but no personal data")
    degree = st.text_input("Degree / Program", key="deg", value="", placeholder="e.g., B.Tech - Electronics and Communication Engineering")
    college = st.text_input("College / University", key="clg", value="", placeholder="e.g., Vels University, Anna University")
    year = st.text_input("Year of Study", key="year", value="", placeholder="e.g., 2022-2026")
    cgpa = st.text_input("CGPA / Marks", key="cgpa", value="", placeholder="e.g., 8.5 CGPA")
    edu_details = st.text_area("Additional Details", key="edu_det", value="", placeholder="e.g., Relevant Coursework: VLSI, Embedded Systems")

# --- TAB 3: INTERNSHIP (UN SCREENSHOT LA IRUKURA SECTION - SAME BUT CLEAN) ---
with tab3:
    st.header("Internships / Training")
    st.info("Screenshot la iruntha same 4 fields than - ippo personal data illa")
    role = st.text_input("Role / Position", key="intern_role", value="", placeholder="e.g., Embedded Systems Intern")
    org = st.text_input("Organization Name", key="intern_org", value="", placeholder="e.g., TCS, ISRO, Vels University")
    duration = st.text_input("Duration", key="intern_dur", value="", placeholder="e.g., May 2024 - July 2024")
    work_desc = st.text_area("Key Responsibilities", key="intern_work", value="", placeholder="• Developed IoT based projects\n• Worked with Embedded C, Arduino\n• Team collaboration")

# --- TAB 4: PROJECTS (SAME AS BEFORE) ---
with tab4:
    st.header("Projects & Skills")
    proj1 = st.text_input("Project 1 Title", key="p1_title", value="", placeholder="e.g., IoT Based Home Automation")
    proj1_desc = st.text_area("Project 1 Description", key="p1_desc", value="", placeholder="e.g., Built using ESP32, sensors...")
    skills = st.text_area("Technical Skills", key="skills", value="", placeholder="e.g., C, Python, Embedded C, Arduino, IoT, PCB Design")

# --- TAB 5: PREVIEW (BALANCE ELLAM APDIYE IRUKKU) ---
with tab5:
    st.header("Preview & Export")
    if name and email:
        st.success("Preview Ready")
        with st.container(border=True):
            st.subheader(name if name else "Your Name")
            st.write(f"**{pro_title}**")
            st.write(f"📧 {email} | 📞 {phone} | 📍 {location}")
            st.write(f"🔗 {linkedin} | 💻 {github}")
            if summary:
                st.divider()
                st.write(f"**Summary:** {summary}")
            st.divider()
            st.write(f"**Education:** {degree} | {college} | {year} | {cgpa}")
            st.write(edu_details)
            st.divider()
            st.write(f"**Internship:** {role} at {org} ({duration})")
            st.write(work_desc)
            st.divider()
            st.write(f"**Projects:** {proj1} - {proj1_desc}")
            st.write(f"**Skills:** {skills}")

        if st.button("📥 Download PDF", type="primary", use_container_width=True):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", "B", 18)
            pdf.cell(0, 10, name, ln=True, align='C')
            pdf.set_font("Arial", "", 11)
            pdf.cell(0, 7, f"{pro_title}", ln=True, align='C')
            pdf.cell(0, 7, f"{email} | {phone} | {location}", ln=True, align='C')
            pdf.cell(0, 7, f"{linkedin} | {github}", ln=True, align='C')
            pdf.ln(5)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 8, "Education", ln=True)
            pdf.set_font("Arial", "", 10)
            pdf.multi_cell(0, 6, f"{degree} - {college} - {year} - {cgpa}\n{edu_details}")
            pdf.ln(3)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 8, "Internship / Training", ln=True)
            pdf.set_font("Arial", "", 10)
            pdf.multi_cell(0, 6, f"{role} at {org} ({duration})\n{work_desc}")
            pdf.ln(3)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 8, "Projects & Skills", ln=True)
            pdf.set_font("Arial", "", 10)
            pdf.multi_cell(0, 6, f"{proj1}\n{proj1_desc}\n\nSkills: {skills}")
            
            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            b64 = base64.b64encode(pdf_bytes).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="{name.replace(" ","_")}_Resume.pdf">Click Here to Download PDF</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.balloons()
    else:
        st.warning("Full Name and Email fill panna than preview varum")

st.divider()
st.caption("Mega Resume Builder - Clean Version | No personal data hardcoded")