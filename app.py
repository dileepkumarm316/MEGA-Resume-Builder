import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="Resume Builder", layout="centered")
st.title("Personal Information")

# --- PDF CREATE ---
class PDF(FPDF):
    pass

def create_pdf(data):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 10, data['name'], ln=True, align='C')
    
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 6, f"{data['title']}", ln=True, align='C')
    pdf.cell(0, 6, f"{data['email']} | {data['phone']} | {data['location']}", ln=True, align='C')
    pdf.cell(0, 6, f"{data['linkedin']} | {data['github']}", ln=True, align='C')
    pdf.ln(5)
    
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Professional Summary", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5, data['summary'])
    
    # --- FIXED ERROR (No encode) ---
    return pdf.output()

# --- FORM - ITHUTHAN NE KETTA MAATRAM ---
# Value = "" (empty), placeholder la "Enter Name" varum

full_name = st.text_input("Full Name *", value="", placeholder="Enter Name")
professional_title = st.text_input("Professional Title", value="", placeholder="Enter Professional Title")
email = st.text_input("Email Address *", value="", placeholder="Enter Email Address")
phone = st.text_input("Phone Number", value="", placeholder="Enter Phone Number")
location = st.text_input("Location", value="", placeholder="Enter Location")
linkedin = st.text_input("LinkedIn Profile URL", value="", placeholder="Enter LinkedIn URL")
github = st.text_input("Portfolio / GitHub URL", value="", placeholder="Enter GitHub / Portfolio URL")
summary = st.text_area("Professional Summary", value="", placeholder="Enter Professional Summary", height=120)

st.divider()

if st.button("Generate Resume", type="primary", use_container_width=True):
    if not full_name or not email:
        st.warning("Full Name & Email kandippa fill pannu da!")
    else:
        data = {
            "name": full_name,
            "title": professional_title,
            "email": email,
            "phone": phone,
            "location": location,
            "linkedin": linkedin,
            "github": github,
            "summary": summary
        }
        try:
            pdf_file = create_pdf(data)
            st.success("Ready da!")
            st.download_button(
                "📥 Download Resume PDF",
                data=pdf_file,
                file_name=f"{full_name}_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Error: {e}")