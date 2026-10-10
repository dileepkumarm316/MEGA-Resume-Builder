import streamlit as st
from fpdf import FPDF
import base64

st.set_page_config(page_title="Resume Builder - Dileepkumar.M", page_icon="📄", layout="wide")

# --- PDF CLASS ---
class PDF(FPDF):
    def header(self):
        pass
    def footer(self):
        pass

def create_smart_pdf(data):
    pdf = PDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Name
    pdf.set_font("Helvetica", "B", 22)
    pdf.cell(0, 10, data.get('name','Dileepkumar.M'), ln=True, align='C')
    
    # Contact
    pdf.set_font("Helvetica", "", 10)
    contact = f"{data.get('email','')} | {data.get('phone','')} | {data.get('linkedin','')} | {data.get('location','')}"
    pdf.cell(0, 6, contact, ln=True, align='C')
    pdf.ln(4)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(4)

    # Helper
    def add_section(title, content):
        if not content:
            return
        pdf.set_font("Helvetica", "B", 12)
        pdf.set_fill_color(240,240,240)
        pdf.cell(0, 7, f" {title.upper()}", ln=True, fill=True)
        pdf.ln(2)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 5, content)
        pdf.ln(3)

    add_section("Professional Summary", data.get('summary',''))
    add_section("Education", data.get('education',''))
    add_section("Skills", data.get('skills',''))
    add_section("Projects", data.get('projects',''))
    add_section("Experience", data.get('experience',''))
    add_section("Certifications", data.get('certifications',''))
    add_section("Achievements", data.get('achievements',''))

    # --- IMPORTANT FIX FOR NEW FPDF2 ---
    # Old: pdf.output(dest='S').encode('latin-1') -> Error
    # New: pdf.output() returns bytes directly
    return pdf.output()

# --- STREAMLIT UI ---
st.markdown("## Builder")
st.markdown("### Professional ATS-Optimized Resume Builder")
st.success("✨ Created by Dileepkumar.M 🤍🎀")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["👤 Personal", "🎓 Education", "💻 Skills", "📁 Projects", "📜 Certs & Export"])

with tab1:
    name = st.text_input("Full Name", "Dileepkumar.M")
    email = st.text_input("Email", "dileep@example.com")
    phone = st.text_input("Phone", "+91 9876543210")
    linkedin = st.text_input("LinkedIn / GitHub", "linkedin.com/in/dileepkumar")
    location = st.text_input("Location", "Udumalpet, Tamil Nadu")
    summary = st.text_area("Professional Summary", "Motivated and detail-oriented developer passionate about building ATS-optimized solutions...")

with tab2:
    education = st.text_area("Education Details", "B.E Computer Science - XYZ College (2022-2026) - CGPA 8.5")

with tab3:
    skills = st.text_area("Skills (comma separated)", "Python, Streamlit, FPDF, Git, GitHub, Machine Learning, SQL")

with tab4:
    projects = st.text_area("Projects", "1. Resume Builder - Built ATS resume generator using Streamlit & FPDF2\n2. My First Project - Professional portfolio")

with tab5:
    experience = st.text_area("Experience / Internship", "Intern at ABC Company - Developed internal tools")
    certifications = st.text_area("Certifications List", "e.g., NPTEL - Introduction to IoT (Elite), AWS Cloud Practitioner, ISRO Certification")
    achievements = st.text_area("Achievements", "Won coding contest, etc.")

# Collect data
resume_data = {
    "name": name,
    "email": email,
    "phone": phone,
    "linkedin": linkedin,
    "location": location,
    "summary": summary,
    "education": education,
    "skills": skills,
    "projects": projects,
    "experience": experience,
    "certifications": certifications,
    "achievements": achievements
}

st.divider()
if st.button("📥 Generate Professional Resume", type="primary", use_container_width=True):
    try:
        pdf_data = create_smart_pdf(resume_data)
        st.success("Resume Generated Successfully! ✅")
        
        b64 = base64.b64encode(pdf_data).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{name}_Resume.pdf" style="text-decoration:none;"><button style="background:#ff4b4b;color:white;border:none;padding:12px 24px;border-radius:8px;width:100%;font-weight:bold;cursor:pointer;">⬇️ Download PDF Resume</button></a>'
        st.markdown(href, unsafe_allow_html=True)
        
        st.download_button(
            label="📄 Download Resume (Alternative)",
            data=pdf_data,
            file_name=f"{name}_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    except Exception as e:
        st.error(f"Error: {e}")
        st.info("Tip: Make sure requirements.txt has 'fpdf2' not 'fpdf'")