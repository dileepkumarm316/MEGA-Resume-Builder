import streamlit as st
from fpdf import FPDF
import base64

st.set_page_config(page_title="Mega Resume Builder", layout="wide", page_icon="📄")

st.title("🚀 Mega Resume Builder")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Personal", "Education", "Internship", "Projects", "Preview"])

with tab1:
    st.subheader("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name *", key="name", placeholder="e.g., Enter your full name")
        email = st.text_input("Email Address *", key="email", placeholder="e.g., your.email@example.com")
        location = st.text_input("Location", key="location", placeholder="e.g., Chennai, Tamil Nadu")
    with col2:
        title = st.text_input("Professional Title", key="title", placeholder="e.g., Electronics & Communication Engineer")
        phone = st.text_input("Phone Number", key="phone", placeholder="e.g., +91 9876543210")
        linkedin = st.text_input("LinkedIn Profile", key="linkedin", placeholder="e.g., https://linkedin.com/in/yourname")

with tab2:
    st.subheader("Education")
    degree = st.text_input("Degree / Program", key="degree", placeholder="e.g., B.Tech - Electronics and Communication Engineering")
    college = st.text_input("College / University", key="college", placeholder="e.g., Vels University, Chennai")
    edu_year = st.text_input("Duration", key="edu_year", placeholder="e.g., 2022-2026")
    cgpa = st.text_input("CGPA / Percentage", key="cgpa", placeholder="e.g., CGPA: 8.5 / 10")

with tab3:
    st.subheader("Internships / Training")
    role = st.text_input("Role / Position", key="role", placeholder="e.g., Embedded Systems Intern")
    org = st.text_input("Organization Name", key="org", placeholder="e.g., TCS, ISRO, Vels University")
    duration = st.text_input("Internship Duration", key="duration", placeholder="e.g., May 2024 - July 2024")
    resp = st.text_area("Key Responsibilities & Achievements", key="resp", placeholder="• Developed IoT based home automation system\n• Collaborated with team of 4 members\n• Improved efficiency by 20%")

with tab4:
    st.subheader("Projects")
    proj_title = st.text_input("Project Title", key="proj_title", placeholder="e.g., IoT Based Home Automation")
    proj_desc = st.text_area("Project Description", key="proj_desc", placeholder="e.g., Built using Arduino, ESP32 and sensors...")
    skills = st.text_input("Skills Used", key="skills", placeholder="e.g., Embedded C, Arduino, IoT, Python")

with tab5:
    st.subheader("Preview & Export")
    if name and email:
        with st.container(border=True):
            st.write(f"**{name}** - {title}")
            st.write(f"📧 {email} | 📞 {phone} | 📍 {location}")
            st.write(f"🔗 {linkedin}")
            st.divider()
            st.write(f"**Education:** {degree} - {college} ({edu_year}) - {cgpa}")
            st.divider()
            st.write(f"**Internship:** {role} at {org} ({duration})")
            st.write(resp)
            st.divider()
            st.write(f"**Project:** {proj_title}")
            st.write(proj_desc)
        
        if st.button("📥 Download PDF", type="primary", use_container_width=True):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, name, ln=True, align='C')
            pdf.set_font("Arial", "", 11)
            pdf.cell(0, 8, f"{title} | {email} | {phone}", ln=True, align='C')
            pdf.cell(0, 8, f"{location} | {linkedin}", ln=True, align='C')
            pdf.ln(10)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 8, f"Education: {degree} - {college} - {edu_year}", ln=True)
            pdf.set_font("Arial", "", 11)
            pdf.multi_cell(0, 8, f"Internship: {role} at {org} - {duration}\n{resp}\n\nProject: {proj_title}\n{proj_desc}")
            
            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            b64 = base64.b64encode(pdf_bytes).decode()
            st.markdown(f'<a href="data:application/octet-stream;base64,{b64}" download="{name}_Resume.pdf">Click to Download PDF</a>', unsafe_allow_html=True)
            st.success("PDF Ready! ✅")
    else:
        st.info("Please fill Full Name and Email in Personal tab to see preview")