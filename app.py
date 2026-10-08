import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="Resume Builder", layout="centered")
st.title("📄 Resume Builder")

class PDF(FPDF):
    pass

def create_pdf(data):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, data.get('name',''), ln=True, align='C')
    pdf.ln(3)
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(0, 5, f"{data.get('email','')} | {data.get('phone','')} | {data.get('location','')}", ln=True, align='C')
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, "PROFESSIONAL SUMMARY", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5, data.get('summary',''))
    # FIXED ERROR - NO MORE .encode ERROR
    return pdf.output()

# ========== PERSONAL INFO - 100% EMPTY ==========
st.header("Personal Information")

# ITHU THAAN MAIN FIX - value="" nu irukka paaru - un details illa!
full_name = st.text_input("Full Name *", value="", placeholder="Enter Full Name")
professional_title = st.text_input("Professional Title", value="", placeholder="Enter Professional Title")
email = st.text_input("Email Address *", value="", placeholder="Enter Email Address")
phone = st.text_input("Phone Number", value="", placeholder="Enter Phone Number")
location = st.text_input("Location", value="", placeholder="Enter Location")
linkedin = st.text_input("LinkedIn Profile URL", value="", placeholder="Enter LinkedIn URL")
github = st.text_input("Portfolio / GitHub URL", value="", placeholder="Enter GitHub URL")
summary = st.text_area("Professional Summary", value="", placeholder="Enter Professional Summary")

st.divider()
st.header("Skills")
skills = st.text_input("Additional Skills (comma separated)", value="", placeholder="e.g., PCB Design, Figma, Flutter")

st.divider()
st.header("Internships / Training")
role = st.text_input("Role / Position", value="", placeholder="e.g., Embedded Systems Intern")
org = st.text_input("Organization Name", value="", placeholder="e.g., TCS, ISRO")
duration = st.text_input("Duration", value="", placeholder="e.g., May 2024 - July 2024")
responsibilities = st.text_area("Key Responsibilities", value="", placeholder="Enter Responsibilities")

st.divider()
st.header("Education")
degree = st.text_input("Degree / Program", value="", placeholder="e.g., B.E ECE")
college = st.text_input("College / University", value="", placeholder="e.g., Vels University")
year = st.text_input("Year", value="", placeholder="e.g., 2022-2026")

st.divider()
if st.button("Generate Resume", type="primary", use_container_width=True):
    if not full_name or not email:
        st.warning("Name & Email fill pannu da!")
    else:
        data = {
            "name": full_name,
            "email": email,
            "phone": phone,
            "location": location,
            "summary": summary
        }
        pdf_bytes = create_pdf(data)
        st.success("Resume Ready!")
        st.download_button("📥 Download PDF", data=pdf_bytes, file_name="Resume.pdf", mime="application/pdf", use_container_width=True)