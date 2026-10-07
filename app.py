import streamlit as st
from fpdf import FPDF
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="MEGA Resume Builder", page_icon="🚀", layout="centered")

st.title("🚀 MEGA Resume Builder")
st.markdown("**AI-powered resume builder that creates professional ATS-friendly resumes in seconds**")
st.divider()

# --- FORM ---
with st.form("resume_form"):
    st.subheader("Personal Details")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name", "Dileep Kumar M")
        email = st.text_input("Email", "dileep@example.com")
        phone = st.text_input("Phone", "+91 98765 43210")
    with col2:
        linkedin = st.text_input("LinkedIn", "linkedin.com/in/dileepkumarm316")
        github = st.text_input("GitHub", "github.com/dileepkumarm316")
        location = st.text_input("Location", "Chennai, India")

    st.subheader("Professional Summary")
    summary = st.text_area("Summary", "Passionate Computer Science student with strong skills in Python, AI, and Full Stack Development. Built MEGA Resume Builder to help students create ATS-friendly resumes.", height=100)

    st.subheader("Skills (comma separated)")
    skills = st.text_input("Skills", "Python, Java, Streamlit, GitHub, AI, Machine Learning, SQL, HTML, CSS")

    st.subheader("Experience / Projects")
    experience = st.text_area("Experience", "MEGA Resume Builder - AI-powered resume builder that creates professional ATS-friendly resumes in seconds. Tech Stack: Python, Streamlit, FPDF. Live at resume-30.streamlit.app\n\n- Built automated PDF generation system\n- ATS score 95%+", height=150)

    st.subheader("Education")
    education = st.text_area("Education", "B.E Computer Science - Anna University (2022-2026)\nCGPA: 8.5/10", height=80)

    submit = st.form_submit_button("🔥 GENERATE RESUME")

# --- PDF CREATION - FIXED CODE ---
class PDF(FPDF):
    def header(self):
        pass

def create_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Name
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(0, 12, name.upper(), ln=True, align='C')
    pdf.ln(2)
    
    # Contact
    pdf.set_font("Arial", '', 10)
    pdf.cell(0, 6, f"{email} | {phone} | {location}", ln=True, align='C')
    pdf.cell(0, 6, f"{linkedin} | {github}", ln=True, align='C')
    pdf.ln(8)
    
    # Summary
    pdf.set_font("Arial", 'B', 12)
    pdf.set_fill_color(240,240,240)
    pdf.cell(0, 8, "  PROFESSIONAL SUMMARY", ln=True, fill=True)
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(0, 6, summary)
    pdf.ln(4)

    # Skills
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, "  SKILLS", ln=True, fill=True)
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(0, 6, skills)
    pdf.ln(4)

    # Experience
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, "  EXPERIENCE & PROJECTS", ln=True, fill=True)
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(0, 6, experience)
    pdf.ln(4)

    # Education
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, "  EDUCATION", ln=True, fill=True)
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(0, 6, education)

    # --- MAIN FIX IS HERE DA ---
    # Old code: pdf.output(dest='S').encode('latin-1') -> ERROR
    # New code:
    output = pdf.output(dest='S')
    # FPDF2 returns bytearray/str based on version, so we handle both
    if isinstance(output, str):
        return output.encode('latin-1')
    else:
        return bytes(output)

if submit:
    try:
        pdf_bytes = create_pdf()
        st.success("✅ Resume Generated Successfully da! 🔥")
        st.download_button(
            label="📥 DOWNLOAD YOUR MEGA RESUME",
            data=pdf_bytes,
            file_name=f"{name.replace(' ','_')}_Resume.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.error(f"Error: {e}")

st.divider()
st.caption("Made with ❤️ by Dileep Kumar M | MEGA Resume Builder")