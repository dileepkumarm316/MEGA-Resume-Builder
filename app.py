import streamlit as st
from fpdf import FPDF
import base64

st.set_page_config(page_title="Mega Resume Builder", layout="wide", page_icon="📄")

st.title("🚀 Mega Resume Builder")

# Initialize
if 'personal' not in st.session_state:
    st.session_state.personal = {}

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["👤 Personal", "🎓 Education", "💼 Internship", "📝 Projects", "📄 Preview"])

with tab1:
    st.subheader("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name *", value="", placeholder="e.g., Enter your full name")
        email = st.text_input("Email Address *", value="", placeholder="e.g., your.email@example.com")
        location = st.text_input("Location", value="", placeholder="e.g., Chennai, Tamil Nadu")
    with col2:
        title = st.text_input("Professional Title", value="", placeholder="e.g., Electronics & Communication Engineer")
        phone = st.text_input("Phone Number", value="", placeholder="e.g., +91 9876543210")
        linkedin = st.text_input("LinkedIn", value="", placeholder="e.g., https://linkedin.com/in/yourname")
    st.session_state.personal = {"name": name, "title": title, "email": email, "phone": phone, "location": location, "linkedin": linkedin}

with tab2:
    # --- FIXED EDUCATION SECTION - NO PERSONAL DATA ---
    st.subheader("Education")
    degree = st.text_input("Degree / Program", value="", placeholder="e.g., B.Tech - Electronics and Communication Engineering")
    college = st.text_input("College / University", value="", placeholder="e.g., Vels University, Chennai")
    edu_year = st.text_input("Duration", value="", placeholder="e.g., 2022-2026")
    cgpa = st.text_input("CGPA / Percentage", value="", placeholder="e.g., CGPA: 8.5 / 10")
    st.session_state.education = {"degree": degree, "college": college, "year": edu_year, "cgpa": cgpa}

with tab3:
    # --- FIXED INTERNSHIP SECTION - FROM YOUR SCREENSHOT - NO PERSONAL DATA ---
    st.subheader("Internships / Training")
    
    role = st.text_input("Role / Position", value="", placeholder="e.g., Embedded Systems Intern")
    org = st.text_input("Organization Name", value="", placeholder="e.g., TCS, ISRO, Vels University")
    duration = st.text_input("Duration", value="", placeholder="e.g., May 2024 - July 2024")
    resp = st.text_area("Key Responsibilities & Achievements", value="", placeholder="• Developed IoT based home automation system\n• Collaborated with team of 4 members\n• Improved efficiency by 20%")
    st.session_state.intern = {"role": role, "org": org, "duration": duration, "resp": resp}

with tab4:
    st.subheader("Projects")
    proj_title = st.text_input("Project Title", value="", placeholder="e.g., IoT Based Home Automation")
    proj_desc = st.text_area("Description", value="", placeholder="e.g., Built using Arduino, ESP32 and sensors...")
    skills = st.text_input("Skills", value="", placeholder="e.g., Embedded C, Arduino, IoT, Python")

with tab5:
    st.subheader("Preview & Export")
    p = st.session_state.personal
    e = st.session_state.get('education', {})
    i = st.session_state.get('intern', {})
    
    if p.get('name'):
        with st.container(border=True):
            st.write(f"**{p['name']}** - {p['title']}")
            st.write(f"{p['email']} | {p['phone']} | {p['location']}")
            st.divider()
            st.write(f"**Education:** {e.get('degree','')} - {e.get('college','')} ({e.get('year','')})")
            st.divider()
            st.write(f"**Internship:** {i.get('role','')} at {i.get('org','')} ({i.get('duration','')})")
            st.write(i.get('resp',''))
        
        if st.button("📥 Download PDF", type="primary"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, p['name'], ln=True, align='C')
            pdf.set_font("Arial", "", 11)
            pdf.cell(0, 8, f"{p['title']} | {p['email']} | {p['phone']}", ln=True, align='C')
            pdf.ln(10)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 8, "Education:", ln=True)
            pdf.set_font("Arial", "", 11)
            pdf.cell(0, 8, f"{e.get('degree','')} - {e.get('college','')} - {e.get('year','')}", ln=True)
            pdf.ln(5)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 8, "Internship:", ln=True)
            pdf.set_font("Arial", "", 11)
            pdf.cell(0, 8, f"{i.get('role','')} at {i.get('org','')} - {i.get('duration','')}", ln=True)
            pdf.multi_cell(0, 8, i.get('resp',''))
            
            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            b64 = base64.b64encode(pdf_bytes).decode()
            st.markdown(f'<a href="data:application/octet-stream;base64,{b64}" download="{p["name"]}_Resume.pdf">Click to Download PDF</a>', unsafe_allow_html=True)
            st.success("PDF Ready!")
    else:
        st.info("Please fill Personal Info to see preview")