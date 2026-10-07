import streamlit as st
from fpdf import FPDF
import base64
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Mega Resume Builder",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
   .main-header {
        text-align: center;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
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

if 'education' not in st.session_state:
    st.session_state.education = []

if 'experience' not in st.session_state:
    st.session_state.experience = []

# Sidebar
with st.sidebar:
    st.title("📄 Resume Builder")
    st.markdown("---")
    st.info(
        "**How to use:**\n\n"
        "1. Fill Personal Info\n"
        "2. Add Education\n"
        "3. Add Experience\n"
        "4. Preview & Download"
    )
    st.markdown("---")
    st.caption(f"© {datetime.now().year} Mega Resume Builder")

# Main Title
st.title("🚀 Mega Resume Builder")
st.markdown("Create a professional resume with example-guided inputs")
st.divider()

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "👤 Personal Information",
    "🎓 Education",
    "💼 Experience & Projects",
    "📄 Preview & Export"
])

# TAB 1: Personal Info
with tab1:
    st.header("Personal Information")
    st.markdown("Fields marked with * are required")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Full Name *",
            value=st.session_state.personal["name"],
            placeholder="e.g., Enter your full name"
        )
        email = st.text_input(
            "Email Address *",
            value=st.session_state.personal["email"],
            placeholder="e.g., your.email@example.com"
        )
        location = st.text_input(
            "Location",
            value=st.session_state.personal["location"],
            placeholder="e.g., Chennai, Tamil Nadu"
        )
        linkedin = st.text_input(
            "LinkedIn Profile URL",
            value=st.session_state.personal["linkedin"],
            placeholder="e.g., https://linkedin.com/in/yourname"
        )

    with col2:
        title = st.text_input(
            "Professional Title",
            value=st.session_state.personal["title"],
            placeholder="e.g., Electronics & Communication Engineer"
        )
        phone = st.text_input(
            "Phone Number",
            value=st.session_state.personal["phone"],
            placeholder="e.g., +91 9876543210"
        )
        github = st.text_input(
            "Portfolio / GitHub URL",
            value=st.session_state.personal["github"],
            placeholder="e.g., https://github.com/yourname"
        )
        summary = st.text_area(
            "Professional Summary",
            value="",
            placeholder="e.g., Passionate ECE engineer with experience in Embedded Systems and IoT..."
        )

    # Save to session
    st.session_state.personal.update({
        "name": name,
        "title": title,
        "email": email,
        "phone": phone,
        "location": location,
        "linkedin": linkedin,
        "github": github,
        "summary": summary
    })

# TAB 2: Education
with tab2:
    st.header("Education Details")

    col1, col2 = st.columns(2)
    with col1:
        college = st.text_input(
            "College / University Name",
            value="",
            placeholder="e.g., Anna University"
        )
        degree = st.text_input(
            "Degree / Course",
            value="",
            placeholder="e.g., B.E Electronics and Communication Engineering"
        )
    with col2:
        year = st.text_input(
            "Year of Study",
            value="",
            placeholder="e.g., 2022-2026"
        )
        cgpa = st.text_input(
            "CGPA / Percentage",
            value="",
            placeholder="e.g., CGPA: 8.5 / 10"
        )

    edu_details = st.text_area(
        "Additional Details",
        value="",
        placeholder="e.g., Relevant Coursework: Embedded Systems, VLSI, IoT. Achievements:..."
    )

# TAB 3: Experience
with tab3:
    st.header("Experience & Projects")

    exp_title = st.text_input(
        "Company / Project Name",
        value="",
        placeholder="e.g., Embedded Systems Intern at ABC Technologies"
    )

    col1, col2 = st.columns(2)
    with col1:
        exp_role = st.text_input(
            "Role",
            value="",
            placeholder="e.g., Intern - Embedded Developer"
        )
    with col2:
        exp_duration = st.text_input(
            "Duration",
            value="",
            placeholder="e.g., Jan 2024 - Mar 2024"
        )

    exp_desc = st.text_area(
        "Description",
        value="",
        placeholder="e.g., Developed IoT based home automation system using Arduino and ESP32. Implemented..."
    )

    skills = st.text_input(
        "Skills Used",
        value="",
        placeholder="e.g., Embedded C, Arduino, ESP32, IoT, PCB Design, Python"
    )

    st.divider()
    st.subheader("Additional Skills")
    tech_skills = st.text_area(
        "Technical Skills",
        value="",
        placeholder="e.g., Programming: C, C++, Python, Embedded C\nTools: Arduino IDE, KiCad, MATLAB"
    )

# TAB 4: Preview & Export
with tab4:
    st.header("Preview & Export")
    p = st.session_state.personal

    if p["name"] and p["email"]:
        st.success("Preview generated based on your inputs")
        st.divider()

        # Preview Container
        with st.container(border=True):
            st.subheader(p["name"])
            st.markdown(f"**{p['title']}**")
            st.markdown(f"📧 {p['email']} | 📞 {p['phone']} | 📍 {p['location']}")
            st.markdown(f"🔗 {p['linkedin']} | 💻 {p['github']}")

            if p.get("summary"):
                st.divider()
                st.markdown("**Professional Summary**")
                st.write(p["summary"])

            if college:
                st.divider()
                st.markdown("**Education**")
                st.write(f"**{degree}** - {college} ({year})")
                st.write(f"{cgpa}")
                if edu_details:
                    st.write(edu_details)

            if exp_title:
                st.divider()
                st.markdown("**Experience / Projects**")
                st.write(f"**{exp_title}** | {exp_role} | {exp_duration}")
                st.write(exp_desc)
                if skills:
                    st.write(f"*Skills: {skills}*")

        st.divider()

        # PDF Generation
        if st.button("📥 Download Resume as PDF", type="primary", use_container_width=True):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            # Name
            pdf.set_font("Arial", "B", 20)
            pdf.cell(0, 12, p["name"], ln=True, align='C')

            # Title
            pdf.set_font("Arial", "", 12)
            pdf.cell(0, 8, p["title"], ln=True, align='C')

            # Contact
            pdf.set_font("Arial", "", 10)
            pdf.cell(0, 6, f"{p['email']} | {p['phone']} | {p['location']}", ln=True, align='C')
            pdf.cell(0, 6, f"{p['linkedin']} | {p['github']}", ln=True, align='C')
            pdf.ln(8)

            # Summary
            if p.get("summary"):
                pdf.set_font("Arial", "B", 12)
                pdf.cell(0, 8, "Professional Summary", ln=True)
                pdf.set_font("Arial", "", 10)
                pdf.multi_cell(0, 6, p["summary"])
                pdf.ln(4)

            # Education
            if college:
                pdf.set_font("Arial", "B", 12)
                pdf.cell(0, 8, "Education", ln=True)
                pdf.set_font("Arial", "", 10)
                pdf.cell(0, 6, f"{degree} - {college} ({year})", ln=True)
                pdf.cell(0, 6, f"{cgpa}", ln=True)
                if edu_details:
                    pdf.multi_cell(0, 6, edu_details)
                pdf.ln(4)

            # Experience
            if exp_title:
                pdf.set_font("Arial", "B", 12)
                pdf.cell(0, 8, "Experience & Projects", ln=True)
                pdf.set_font("Arial", "B", 10)
                pdf.cell(0, 6, f"{exp_title} | {exp_role} | {exp_duration}", ln=True)
                pdf.set_font("Arial", "", 10)
                pdf.multi_cell(0, 6, exp_desc)
                if skills:
                    pdf.cell(0, 6, f"Skills: {skills}", ln=True)

            # Generate download link
            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            b64 = base64.b64encode(pdf_bytes).decode()
            file_name = f"{p['name'].replace(' ', '_')}_Resume.pdf"

            href = f'''
            <a href="data:application/octet-stream;base64,{b64}"
               download="{file_name}"
               style="text-decoration:none;">
               <button style="width:100%; padding:10px; background-color:#FF4B4B;
               color:white; border:none; border-radius:5px; cursor:pointer;">
               Click here if download does not start automatically
               </button>
            </a>
            '''
            st.markdown(href, unsafe_allow_html=True)
            st.balloons()
            st.success(f"Resume PDF generated successfully: {file_name}")

    else:
        st.warning("Please complete Personal Information to enable preview")
        st.info(
            "**Steps to generate resume:**\n"
            "1. Go to Personal Information tab\n"
            "2. Enter Full Name and Email Address (required)\n"
            "3. Fill other sections as needed\n"
            "4. Return to this tab to preview and download"
        )

# Footer
st.divider()
st.caption("Mega Resume Builder v2.0 | Professional Resume Creation Tool")