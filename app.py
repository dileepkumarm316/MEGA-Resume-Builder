import streamlit as st
from fpdf import FPDF
import base64

st.set_page_config(page_title="Mega Resume Builder", layout="wide", page_icon="📄")

st.markdown("""
<style>
    .stTextInput>div>div>input {
        background-color: #262730 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 Mega Resume Builder")

if 'personal' not in st.session_state:
    st.session_state.personal = {
        "name": "",
        "title": "",
        "email": "",
        "phone": "",
        "location": "",
        "linkedin": "",
        "github": ""
    }

tab1, tab2, tab3, tab4 = st.tabs(["👤 Personal Info", "🎓 Education", "💼 Experience", "📄 Preview & Export"])

with tab1:
    st.header("Personal Information")
    
    st.session_state.personal["name"] = st.text_input(
        "Full Name *", 
        value="",
        placeholder="e.g., Enter your full name"
    )
    
    st.session_state.personal["title"] = st.text_input(
        "Professional Title", 
        value="",
        placeholder="e.g., Electronics & Communication Engineer"
    )
    
    st.session_state.personal["email"] = st.text_input(
        "Email Address *", 
        value="",
        placeholder="e.g., your.email@example.com"
    )
    
    st.session_state.personal["phone"] = st.text_input(
        "Phone Number", 
        value="",
        placeholder="e.g., +91 9876543210"
    )
    
    st.session_state.personal["location"] = st.text_input(
        "Location", 
        value="",
        placeholder="e.g., Chennai, Tamil Nadu"
    )
    
    st.session_state.personal["linkedin"] = st.text_input(
        "LinkedIn Profile URL", 
        value="",
        placeholder="e.g., https://linkedin.com/in/yourname"
    )
    
    st.session_state.personal["github"] = st.text_input(
        "Portfolio / GitHub URL", 
        value="",
        placeholder="e.g., https://github.com/yourname"
    )

with tab2:
    st.header("Education")
    st.text_input("College Name", value="", placeholder="e.g., Anna University")
    st.text_input("Degree", value="", placeholder="e.g., B.E ECE")
    st.text_input("Year", value="", placeholder="e.g., 2022-2026")
    st.text_area("Additional Details", value="", placeholder="e.g., CGPA 8.5, Relevant Coursework")

with tab3:
    st.header("Experience / Projects")
    st.text_input("Company / Project Name", value="", placeholder="e.g., Embedded Systems Intern")
    st.text_area("Description", value="", placeholder="e.g., Worked on IoT based...")

with tab4:
    st.header("Preview")
    p = st.session_state.personal
    if p['name']:
        st.markdown(f"""
        **{p['name']}**
        {p['title']}
        
        📧 {p['email']} | 📞 {p['phone']} | 📍 {p['location']}
        
        🔗 {p['linkedin']}
        💻 {p['github']}
        """)
        
        if st.button("📥 Download PDF"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, p['name'], ln=True)
            pdf.set_font("Arial", "", 12)
            pdf.cell(0, 10, f"{p['title']} | {p['email']} | {p['phone']}", ln=True)
            pdf.cell(0, 10, f"{p['location']} | {p['linkedin']}", ln=True)
            
            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            b64 = base64.b64encode(pdf_bytes).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="{p["name"]}_Resume.pdf">Download Resume PDF</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.success("PDF Ready da! ✅")
    else:
        st.info("👆 Personal Info fill pannu da, aprom preview varum")