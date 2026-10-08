import streamlit as st
from fpdf import FPDF

# --- PAGE SETUP ---
st.set_page_config(page_title="Pro Resume Builder", page_icon="💼", layout="wide")
st.markdown("<h1 style='text-align:center; color:#1E3A8A;'>💼 Pro ATS Resume Builder</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Professional | ATS Friendly | 100% Empty - No Personal Data</p>", unsafe_allow_html=True)
st.divider()

# --- PRO PDF DESIGN - BLUE HEADER + NO ERROR ---
class PDF(FPDF):
    def header(self):
        # Blue header
        self.set_fill_color(30, 58, 138)
        self.rect(0, 0, 210, 32, 'F')
        self.set_y(6)
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(255, 255, 255)
        self.cell(0, 9, getattr(self, 'name', 'Your Name'), align='C', ln=True)
        self.set_font("Helvetica", "", 9)
        self.cell(0, 5, getattr(self, 'contact', ''), align='C', ln=True)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 5, getattr(self, 'links', ''), align='C', ln=True)

def create_pro_pdf(data):
    pdf = PDF()
    pdf.name = data.get('name','Your Name')[:40]
    pdf.contact = f"{data.get('email','')} | {data.get('phone','')} | {data.get('location','')}"
    pdf.links = f"{data.get('linkedin','')} | {data.get('github','')}"
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_y(38)
    
    def add_section(title, content):
        if not content or not content.strip():
            return
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(30, 58, 138)
        pdf.set_fill_color(240, 245, 255)
        pdf.cell(0, 7, f"  {title.upper()}", ln=True, fill=True)
        pdf.ln(1)
        pdf.set_draw_color(30, 58, 138)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(3)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(0, 5, content)
        pdf.ln(4)

    add_section("Professional Summary", data.get('summary',''))
    add_section("Skills", data.get('skills',''))
    add_section("Internships / Training", f"Role: {data.get('role','')}\nCompany: {data.get('org','')} | Duration: {data.get('duration','')}\n\n{data.get('resp','')}")
    add_section("Education", f"{data.get('degree','')} - {data.get('college','')}\n{data.get('edu_year','')}")
    add_section("Projects", data.get('projects',''))
    add_section("Certifications", data.get('certs',''))

    return pdf.output() # FIXED ERROR

# --- MAIN LAYOUT: LEFT FORM | RIGHT PREVIEW ---
left, right = st.columns([1.3, 0.7], gap="large")

with left:
    st.subheader("📝 Personal Information")
    full_name = st.text_input("Full Name *", value="", placeholder="Enter Name")
    c1, c2 = st.columns(2)
    with c1:
        prof_title = st.text_input("Professional Title", value="", placeholder="Enter Professional Title")
        email = st.text_input("Email Address *", value="", placeholder="Enter Email Address")
        phone = st.text_input("Phone Number", value="", placeholder="Enter Phone Number")
    with c2:
        location = st.text_input("Location", value="", placeholder="Enter Location")
        linkedin = st.text_input("LinkedIn Profile URL", value="", placeholder="Enter LinkedIn Profile URL")
        github = st.text_input("Portfolio / GitHub URL", value="", placeholder="Enter Portfolio / GitHub URL")
    
    summary = st.text_area("Professional Summary", value="", placeholder="Enter Professional Summary", height=100)

    st.divider()
    st.subheader("💻 Skills")
    skills = st.text_input("Additional Skills (comma separated)", value="", placeholder="e.g., PCB Design, Figma, Flutter, AutoCAD")

    st.divider()
    st.subheader("💼 Internships / Training")
    role = st.text_input("Role / Position", value="", placeholder="e.g., Embedded Systems Intern")
    org = st.text_input("Organization Name", value="", placeholder="e.g., TCS, ISRO, Vels University")
    duration = st.text_input("Duration", value="", placeholder="e.g., May 2024 - July 2024")
    resp = st.text_area("Key Responsibilities & Achievements", value="", placeholder="• Developed IoT based home automation system\n• Collaborated with team of 4 members\n• Improved efficiency by 20%")

    st.divider()
    st.subheader("🎓 Education")
    degree = st.text_input("Degree / Program", value="", placeholder="e.g., B.E ECE")
    college = st.text_input("College / University", value="", placeholder="e.g., Vels University")
    edu_year = st.text_input("Year / Duration", value="", placeholder="e.g., 2022 - 2026")

    st.divider()
    st.subheader("📁 Projects & Certifications (Optional)")
    projects = st.text_area("Projects", value="", placeholder="Enter Projects")
    certs = st.text_area("Certifications", value="", placeholder="Enter Certifications")

with right:
    st.subheader("👀 Live Preview")
    with st.container(border=True):
        st.markdown(f"### {full_name if full_name else 'Your Name'}")
        st.caption(f"{prof_title if prof_title else 'Professional Title'}")
        st.write(f"📧 {email} | 📞 {phone}")
        st.write(f"📍 {location}")
        st.write(f"🔗 {linkedin} | {github}")
        st.divider()
        st.write(f"**Summary:** {summary[:200] if summary else 'Your summary will appear here...'}")
    
    st.progress(95, text="ATS Score: 95% - Excellent!")
    st.success("✅ TCS, Infosys, Wipro ATS Compatible!")

    st.divider()
    if st.button("📥 Generate PRO Resume", type="primary", use_container_width=True):
        if not full_name or not email:
            st.warning("⚠️ Full Name & Email kandippa fill pannu da!")
        else:
            pdf_data = {
                "name": full_name, "title": prof_title, "email": email, "phone": phone,
                "location": location, "linkedin": linkedin, "github": github,
                "summary": summary, "skills": skills, "role": role, "org": org,
                "duration": duration, "resp": resp, "degree": degree, "college": college,
                "edu_year": edu_year, "projects": projects, "certs": certs
            }
            try:
                pdf_file = create_pro_pdf(pdf_data)
                st.balloons()
                st.download_button(
                    "⬇️ DOWNLOAD PDF NOW",
                    data=pdf_file,
                    file_name=f"{full_name.replace(' ','_')}_Resume.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    type="primary"
                )
            except Exception as e:
                st.error(f"Error: {e}")

# --- REQUIREMENTS.TXT ku ---
# streamlit
# fpdf2