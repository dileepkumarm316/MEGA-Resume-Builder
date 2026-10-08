import streamlit as st
from fpdf import FPDF
import base64

st.set_page_config(page_title="ATS Resume Builder", page_icon="📄", layout="wide")

# --- PDF GENERATOR CLASS ---
class PDF(FPDF):
    def header(self):
        pass
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def create_smart_pdf(data):
    pdf = PDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Name
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(20, 20, 20)
    pdf.cell(0, 12, data.get('name','Your Name'), ln=True, align='C')
    
    # Contact
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(80, 80, 80)
    contact_line = f"{data.get('email','')} | {data.get('phone','')} | {data.get('linkedin','')} | {data.get('location','')}"
    pdf.cell(0, 6, contact_line, ln=True, align='C')
    pdf.ln(3)
    pdf.set_draw_color(200,200,200)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    def add_section(title, content):
        if not content or not content.strip():
            return
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_fill_color(245,245,245)
        pdf.set_text_color(0,0,0)
        pdf.cell(0, 7, f"  {title.upper()}", ln=True, fill=True)
        pdf.ln(2)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 5, content)
        pdf.ln(4)

    add_section("Professional Summary", data.get('summary',''))
    add_section("Education", data.get('education',''))
    add_section("Skills", data.get('skills',''))
    add_section("Projects", data.get('projects',''))
    add_section("Experience", data.get('experience',''))
    add_section("Certifications", data.get('certifications',''))
    add_section("Achievements", data.get('achievements',''))

    # FIXED FOR FPDF2 - NO ENCODE ERROR
    return pdf.output()

# --- UI ---
st.title("📄 Professional ATS Resume Builder")
st.markdown("Create your professional resume in 2 minutes")
st.divider()

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Full Name", placeholder="Ex: Dileepkumar.M")
    email = st.text_input("Email", placeholder="Ex: yourname@gmail.com")
    phone = st.text_input("Phone Number", placeholder="Ex: +91 9876543210")
    
with col2:
    linkedin = st.text_input("LinkedIn / GitHub / Portfolio", placeholder="Ex: linkedin.com/in/yourname")
    location = st.text_input("Location", placeholder="Ex: Udumalpet, Tamil Nadu")
    summary = st.text_area("Professional Summary", placeholder="Motivated developer passionate about...", height=100)

education = st.text_area("🎓 Education", placeholder="Ex: B.E Computer Science - XYZ College (2022-2026) - CGPA 8.5", height=100)
skills = st.text_area("💻 Skills", placeholder="Ex: Python, Streamlit, SQL, Git, Machine Learning", height=80)
projects = st.text_area("📁 Projects", placeholder="Ex: 1. Resume Builder - Built using Streamlit & FPDF2\n2. E-commerce site...", height=120)
experience = st.text_area("💼 Experience / Internship", placeholder="Ex: Intern at ABC - Developed tools...", height=100)
certifications = st.text_area("📜 Certifications", placeholder="Ex: NPTEL IoT (Elite), AWS Cloud Practitioner, ISRO", height=80)
achievements = st.text_area("🏆 Achievements", placeholder="Ex: Won hackathon, Coding contest winner", height=80)

resume_data = {
    "name": name, "email": email, "phone": phone,
    "linkedin": linkedin, "location": location,
    "summary": summary, "education": education,
    "skills": skills, "projects": projects,
    "experience": experience,
    "certifications": certifications,
    "achievements": achievements
}

st.divider()
if st.button("📥 Generate & Download Resume", type="primary", use_container_width=True):
    if not name or not email:
        st.warning("⚠️ Please enter at least Name and Email!")
    else:
        try:
            pdf_data = create_smart_pdf(resume_data)
            st.success("✅ Resume Generated Successfully!")
            
            st.download_button(
                label="⬇️ DOWNLOAD PDF NOW",
                data=pdf_data,
                file_name=f"{name.replace(' ','_')}_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
                type="primary"
            )
        except Exception as e:
            st.error(f"Error: {e}")