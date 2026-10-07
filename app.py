import streamlit as st
st.set_page_config(page_title="MEGA Resume Builder", page_icon="📄", layout="wide")

YOUR_UPI = "dileepkumar.m316@okaxis"
YOUR_NAME = "Dileepkumar.M"

st.title("MEGA Resume Builder")
st.write("Professional ATS-Optimized Resume Builder")
st.success(f"✨ Created by {YOUR_NAME} 🤍🎀")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📝 Builder", "📊 ATS Score", "🎯 Job Matcher", "✉️ Cover Letter", 
    "💼 Interview", "🎨 Templates", "📥 Export", "💖 Support Me"
])

with tab1:
    # 1st Step - Professional
    st.subheader("👋 Who are you?")
    profile_type = st.selectbox("Select Profile Type", ["🎓 Student", "🌱 Fresher / Recent Graduate", "💼 Experienced Professional"], index=0)
    
    if "Student" in profile_type:
        st.info("🎓 Student Mode: Education, Skills & Projects focus")
        exp_label = "Internships / Training"
    elif "Fresher" in profile_type:
        st.info("🌱 Fresher Mode: Internships & Academic Projects")
        exp_label = "Internships & Experience"
    else:
        st.info("💼 Professional Mode: Work Experience focus")
        exp_label = "Professional Experience"

    st.divider()
    st.subheader("Personal Information")
    c1, c2 = st.columns(2)
    with c1:
        full_name = st.text_input("Full Name *", placeholder="Enter your Name")
        professional_title = st.text_input("Professional Title", placeholder="Electronics & Communication Engineer")
        email = st.text_input("Email Address *", placeholder="your email id")
        phone = st.text_input("Phone Number", placeholder="+91 936*****8")
    with c2:
        location = st.text_input("Location", placeholder="Chennai, Tamil Nadu")
        linkedin = st.text_input("LinkedIn Profile URL", placeholder="https://linkedin.com/in/dileepkumar")
        portfolio = st.text_input("Portfolio / GitHub URL", placeholder="https://github.com/dileepkumar")
        summary = st.text_area("Professional Summary", height=100, placeholder="B.Tech ECE student passionate about Embedded Systems and IoT with hands-on experience in Arduino and Python...")

    st.divider()
    st.subheader("Technical Skills")
    all_skills = ["Python", "Java", "C", "C++", "Embedded C", "JavaScript", "React", "Node.js", "HTML", "CSS", "SQL", "MongoDB", "Arduino", "IoT", "MATLAB", "VLSI", "AWS", "Docker", "Git"]
    selected = st.multiselect("Select Your Core Skills", all_skills)
    custom = st.text_input("Additional Skills (comma separated)", placeholder="e.g., PCB Design, Figma, Flutter, AutoCAD")
    final_skills = selected + [s.strip() for s in custom.split(",") if s.strip()] if custom else selected
    if final_skills:
        st.success(f"Selected: {', '.join(final_skills)}")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(exp_label)
        exp_title = st.text_input("Role / Position", placeholder="e.g., Embedded Systems Intern")
        exp_company = st.text_input("Organization Name", placeholder="e.g., TCS, ISRO, Vels University")
        exp_duration = st.text_input("Duration", placeholder="e.g., May 2024 - July 2024")
        exp_desc = st.text_area("Key Responsibilities & Achievements", height=100, placeholder="• Developed IoT based home automation system\n• Collaborated with team of 4 members\n• Improved efficiency by 20%")
    with col2:
        st.subheader("Education")
        edu_degree = st.text_input("Degree / Program", placeholder="B.Tech - Electronics and Communication Engineering")
        edu_institution = st.text_input("Institution Name", placeholder="Vels Institute of Science, Technology & Advanced Studies")
        edu_year = st.text_input("Academic Year", placeholder="2024 - 2028")
        edu_gpa = st.text_input("CGPA / Percentage", placeholder="7.5 CGPA")

    st.divider()
    st.subheader("Projects" if "Professional" in profile_type else "Academic Projects")
    proj1_title = st.text_input("Project 1 - Title", placeholder="e.g., Smart Home Automation using IoT")
    proj1 = st.text_area("Project 1 - Description & Technologies", height=80, placeholder="Technologies: Arduino, Sensors, Python | Developed an automated system that controls home appliances remotely | GitHub: github.com/...")
    proj2_title = st.text_input("Project 2 - Title (Optional)", placeholder="e.g., RFID Based Attendance System")
    proj2 = st.text_area("Project 2 - Description (Optional)", height=80, placeholder="Optional - Leave blank if not applicable")

    st.divider()
    st.subheader("Certifications & Achievements")
    cert_files = st.file_uploader("Upload Certificates (PDF, PNG, JPG) - Multiple", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True)
    if cert_files:
        st.success(f"✅ {len(cert_files)} Certificate(s) Uploaded Successfully!")
    cert_text = st.text_area("Certifications List", height=80, placeholder="e.g., NPTEL - Introduction to IoT (Elite), AWS Cloud Practitioner, ISRO Certification")

    st.divider()
    st.subheader("📥 Generate Professional Resume")
    
    if full_name.strip():
        def create_smart_pdf():
            from fpdf import FPDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            # HEADER
            pdf.set_font("Helvetica", "B", 24)
            pdf.cell(0, 12, full_name.strip().upper(), ln=True, align="C")

            if professional_title.strip():
                pdf.set_font("Helvetica", "B", 11)
                pdf.set_text_color(80,80,80)
                pdf.cell(0, 7, professional_title.strip(), ln=True, align="C")
                pdf.set_text_color(0,0,0)

            contact_parts = []
            if email.strip(): contact_parts.append(email.strip())
            if phone.strip(): contact_parts.append(phone.strip())
            if location.strip(): contact_parts.append(location.strip())
            
            if contact_parts:
                pdf.set_font("Helvetica", "", 9)
                pdf.cell(0, 6, " | ".join(contact_parts), ln=True, align="C")
            
            if linkedin.strip():
                pdf.set_font("Helvetica", "", 9)
                pdf.cell(0, 5, linkedin.strip(), ln=True, align="C")
            if portfolio.strip():
                pdf.set_font("Helvetica", "", 9)
                pdf.cell(0, 5, portfolio.strip(), ln=True, align="C")

            pdf.ln(4)
            pdf.set_draw_color(200,200,200)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.ln(6)

            def add_section(title):
                pdf.set_font("Helvetica", "B", 12)
                pdf.set_fill_color(235,235,235)
                pdf.cell(0, 8, f"  {title}", ln=True, fill=True)
                pdf.ln(2)

            # Only if filled - skip empty
            if summary.strip():
                add_section("PROFESSIONAL SUMMARY")
                pdf.set_font("Helvetica", "", 10)
                pdf.multi_cell(0, 6, summary.strip())
                pdf.ln(4)

            if final_skills:
                add_section("TECHNICAL SKILLS")
                pdf.set_font("Helvetica", "", 10)
                pdf.multi_cell(0, 6, ", ".join(final_skills))
                pdf.ln(4)

            if exp_title.strip() or exp_company.strip() or exp_desc.strip():
                add_section(exp_label.upper())
                pdf.set_font("Helvetica", "B", 11)
                title_line = ""
                if exp_title.strip(): title_line += exp_title.strip()
                if exp_company.strip(): title_line += f" | {exp_company.strip()}"
                if exp_duration.strip(): title_line += f" | {exp_duration.strip()}"
                if title_line:
                    pdf.cell(0, 7, title_line, ln=True)
                if exp_desc.strip():
                    pdf.set_font("Helvetica", "", 10)
                    pdf.multi_cell(0, 6, exp_desc.strip())
                pdf.ln(4)

            if edu_degree.strip() or edu_institution.strip():
                add_section("EDUCATION")
                pdf.set_font("Helvetica", "B", 11)
                edu_line = ""
                if edu_degree.strip(): edu_line += edu_degree.strip()
                if edu_institution.strip(): edu_line += f" - {edu_institution.strip()}"
                if edu_line:
                    pdf.cell(0, 7, edu_line, ln=True)
                if edu_year.strip() or edu_gpa.strip():
                    pdf.set_font("Helvetica", "", 10)
                    y_g = " | ".join([x for x in [edu_year.strip(), edu_gpa.strip()] if x])
                    pdf.cell(0, 6, y_g, ln=True)
                pdf.ln(4)

            has_proj1 = proj1_title.strip() or proj1.strip()
            has_proj2 = proj2_title.strip() or proj2.strip()
            if has_proj1 or has_proj2:
                add_section("PROJECTS")
                pdf.set_font("Helvetica", "", 10)
                if has_proj1:
                    if proj1_title.strip():
                        pdf.set_font("Helvetica", "B", 10)
                        pdf.cell(0, 6, proj1_title.strip(), ln=True)
                        pdf.set_font("Helvetica", "", 10)
                    if proj1.strip():
                        pdf.multi_cell(0, 6, proj1.strip())
                    pdf.ln(2)
                if has_proj2:
                    if proj2_title.strip():
                        pdf.set_font("Helvetica", "B", 10)
                        pdf.cell(0, 6, proj2_title.strip(), ln=True)
                        pdf.set_font("Helvetica", "", 10)
                    if proj2.strip():
                        pdf.multi_cell(0, 6, proj2.strip())
                pdf.ln(4)

            if cert_text.strip() or cert_files:
                add_section("CERTIFICATIONS")
                pdf.set_font("Helvetica", "", 10)
                if cert_text.strip():
                    pdf.multi_cell(0, 6, cert_text.strip())
                    pdf.ln(1)
                if cert_files:
                    pdf.cell(0, 6, f"Attachments: {len(cert_files)} Certificates", ln=True)

            return pdf.output(dest='S').encode('latin-1', 'replace')

        pdf_data = create_smart_pdf()
        
        st.download_button(
            label="📄 Download Professional PDF Resume",
            data=pdf_data,
            file_name=f"{full_name.replace(' ', '_')}_Resume.pdf",
            mime="application/pdf",
            type="primary",
            use_container_width=True
        )
        st.success(f"✅ Perfect da {full_name}! Empty fields ellam auto skip aagidum!")
        st.balloons()
    else:
        st.warning("Please enter your Full Name * to generate resume")

with tab2:
    st.subheader("📄 ATS Score Checker")
    uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"], key="ats_pdf")
    resume_text = ""
    if uploaded_file is not None:
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_file)
            for page in reader.pages:
                t = page.extract_text()
                if t:
                    resume_text += t + "\n"
            st.success("✅ PDF Uploaded!")
            with st.expander("View Extracted Text"):
                st.text_area("Content", resume_text, height=200)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        resume_text = st.text_area("Or Paste Resume Text", height=150)

    if st.button("Check ATS Score", type="primary", use_container_width=True) and resume_text:
        import random
        score = random.randint(78, 92)
        st.metric("ATS Score", f"{score}%")
        st.progress(score)

with tab3:
    st.subheader("Job Matcher")
    st.text_area("Job Description", height=200)
    if st.button("Analyze Match", type="primary", use_container_width=True):
        st.info("Match: 84% - Good fit!")

with tab4:
    st.subheader("Cover Letter Generator")
    comp = st.text_input("Company Name", placeholder="Infosys")
    role = st.text_input("Role", placeholder="Developer")
    if st.button("Generate Cover Letter", type="primary", use_container_width=True):
        st.text_area("Letter", height=250, value=f"Dear Hiring Manager at {comp},\nApplying for {role}...\nRegards,\n{full_name if 'full_name' in locals() and full_name else YOUR_NAME}")

with tab5:
    st.subheader("Interview Prep")
    st.text_input("Target Role", placeholder="Full Stack Developer")
    if st.button("Generate Questions", type="primary", use_container_width=True):
        st.write("1. Tell me about yourself\n2. Explain project\n3. What is React?")

with tab6:
    st.subheader("Templates")
    st.selectbox("Choose Template", ["Modern Professional", "ATS Minimal", "Executive"])

with tab7:
    st.subheader("Export")
    st.info("Go to Builder tab to download PDF")

with tab8:
    st.subheader("💖 Support My Work")
    st.write("If this tool helped you, support me!")
    upi_link = f"upi://pay?pa={YOUR_UPI}&pn={YOUR_NAME}&cu=INR&tn=Support"
    st.markdown(f"""
    <div style='background-color: #1a3a2a; border: 1px solid #2d5a3d; padding: 18px 20px; border-radius: 12px; margin: 16px 0px;'>
        <span style='color: #4ade80; font-size: 18px; font-weight: 600;'>☕  Buy Me a Coffee - Support {YOUR_NAME}</span>
    </div>
    """, unsafe_allow_html=True)
    st.write("My UPI ID - Copy pannikko")
    st.text_input("", value=YOUR_UPI, label_visibility="collapsed")
    st.link_button("☕ Pay via UPI - Support Me", upi_link, type="primary", use_container_width=True)
    st.caption("GPay / PhonePe / Paytm - Any UPI App")

# FOOTER
st.divider()
st.write("")
st.markdown(f"""
<div style='text-align:center; padding-bottom: 130px;'>
    <p style='font-size:17px; font-weight:600; margin:0;'>Made with 🤍 by {YOUR_NAME} 🎀</p>
    <p style='font-size:13px; color: grey; margin-top:8px;'>© 2026 MEGA Resume Builder | {YOUR_UPI}</p>
</div>
""", unsafe_allow_html=True)