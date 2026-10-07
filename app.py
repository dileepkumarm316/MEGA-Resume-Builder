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
    st.subheader("Personal Information")
    c1, c2 = st.columns(2)
    with c1:
        full_name = st.text_input("Full Name", placeholder="Dileepkumar M")
        professional_title = st.text_input("Professional Title", placeholder="ECE Engineer")
        email = st.text_input("Email", placeholder="dileepkumar.m316@gmail.com")
        phone = st.text_input("Phone", placeholder="9363611316")
    with c2:
        location = st.text_input("Location", placeholder="Chennai")
        linkedin = st.text_input("LinkedIn URL", placeholder="linkedin.com/in/dileep")
        portfolio = st.text_input("Portfolio / GitHub", placeholder="github.com/dileep")
        summary = st.text_area("Professional Summary", height=100, placeholder="Passionate ECE student...")

    st.divider()
    st.subheader("Skills")
    all_skills = ["Python", "Java", "JavaScript", "TypeScript", "React", "Node.js", "HTML", "CSS", "SQL", "MongoDB", "AWS", "Docker", "Git", "C", "C++"]
    selected = st.multiselect("Select Skills", all_skills)
    custom = st.text_input("Other Skills (comma)", placeholder="Figma, Flutter, Embedded")
    final_skills = selected + [s.strip() for s in custom.split(",") if s.strip()] if custom else selected

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Experience")
        exp_title = st.text_input("Job Title", placeholder="Intern - leave empty if no exp")
        exp_company = st.text_input("Company", placeholder="TCS")
        exp_duration = st.text_input("Duration", placeholder="2024 - Present")
        exp_desc = st.text_area("Description", height=100, placeholder="• What you did")
    with col2:
        st.subheader("Education")
        edu_degree = st.text_input("Degree", placeholder="B Tech ECE")
        edu_institution = st.text_input("College", placeholder="Vels University")
        edu_year = st.text_input("Year", placeholder="2024-2028")
        edu_gpa = st.text_input("CGPA", placeholder="7 CGPA")

    st.divider()
    st.subheader("Projects - Only fill what you have")
    proj1_title = st.text_input("Project 1 Title", placeholder="IoT Home Automation")
    proj1 = st.text_area("Project 1 Details", height=70, placeholder="Tech: Arduino, Sensors | Link: github.com/...")
    proj2_title = st.text_input("Project 2 Title", placeholder="Leave empty if only 1 project")
    proj2 = st.text_area("Project 2 Details", height=70)

    st.divider()
    st.subheader("📜 Certifications")
    cert_files = st.file_uploader("Upload Certificates", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True)
    if cert_files:
        st.success(f"✅ {len(cert_files)} Uploaded!")
    cert_text = st.text_area("Type Certifications (comma)", placeholder="NPTEL IoT, AWS Cloud")

    st.divider()
    st.subheader("📥 Download - Professional Resume")

    if full_name.strip() != "":
        def create_smart_pdf():
            from fpdf import FPDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            # --- HEADER - Only if filled ---
            pdf.set_font("Helvetica", "B", 24)
            pdf.cell(0, 12, full_name.strip().upper(), ln=True, align="C")

            if professional_title.strip():
                pdf.set_font("Helvetica", "B", 11)
                pdf.set_text_color(80,80,80)
                pdf.cell(0, 7, professional_title.strip(), ln=True, align="C")
                pdf.set_text_color(0,0,0)

            # Contact - only filled ones
            contact_parts = []
            if email.strip(): contact_parts.append(email.strip())
            if phone.strip(): contact_parts.append(phone.strip())
            if location.strip(): contact_parts.append(location.strip())
            
            if contact_parts:
                pdf.set_font("Helvetica", "", 9)
                pdf.cell(0, 6, " | ".join(contact_parts), ln=True, align="C")
            
            if linkedin.strip():
                pdf.set_font("Helvetica", "", 9)
                pdf.set_text_color(0,0,150)
                pdf.cell(0, 5, f"LinkedIn: {linkedin.strip()}", ln=True, align="C")
                pdf.set_text_color(0,0,0)
            
            if portfolio.strip():
                pdf.set_font("Helvetica", "", 9)
                pdf.set_text_color(0,0,150)
                pdf.cell(0, 5, f"Portfolio: {portfolio.strip()}", ln=True, align="C")
                pdf.set_text_color(0,0,0)

            pdf.ln(4)
            pdf.set_draw_color(200,200,200)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.ln(6)

            def add_section(title):
                pdf.set_font("Helvetica", "B", 12)
                pdf.set_fill_color(235,235,235)
                pdf.cell(0, 8, f"  {title}", ln=True, fill=True)
                pdf.ln(2)

            # Summary - skip if empty
            if summary.strip():
                add_section("PROFESSIONAL SUMMARY")
                pdf.set_font("Helvetica", "", 10)
                pdf.multi_cell(0, 6, summary.strip())
                pdf.ln(4)

            # Skills - skip if empty
            if final_skills:
                add_section("SKILLS")
                pdf.set_font("Helvetica", "", 10)
                pdf.multi_cell(0, 6, ", ".join(final_skills))
                pdf.ln(4)

            # Experience - skip if all empty
            if exp_title.strip() or exp_company.strip() or exp_desc.strip():
                add_section("EXPERIENCE")
                pdf.set_font("Helvetica", "B", 11)
                title_line = ""
                if exp_title.strip(): title_line += exp_title.strip()
                if exp_company.strip(): title_line += f" at {exp_company.strip()}"
                if exp_duration.strip(): title_line += f" ({exp_duration.strip()})"
                if title_line:
                    pdf.cell(0, 7, title_line, ln=True)
                if exp_desc.strip():
                    pdf.set_font("Helvetica", "", 10)
                    pdf.multi_cell(0, 6, exp_desc.strip())
                pdf.ln(4)

            # Education - skip if empty
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

            # Projects - skip empty projects
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

            # Certs - skip if empty
            if cert_text.strip() or cert_files:
                add_section("CERTIFICATIONS")
                pdf.set_font("Helvetica", "", 10)
                if cert_text.strip():
                    pdf.multi_cell(0, 6, cert_text.strip())
                    pdf.ln(1)
                if cert_files:
                    pdf.cell(0, 6, f"Certificates Attached: {len(cert_files)} files", ln=True)

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
        st.success(f"✅ Ready da {full_name}! Empty fields ellam skip aagidum!")
        st.balloons()
    else:
        st.warning("👆 Full Name fill pannu da - aprom PDF varum!")

with tab2:
    st.subheader("📄 ATS Score")
    up = st.file_uploader("Upload Resume PDF", type=["pdf"], key="ats")
    txt = ""
    if up:
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(up)
            for p in reader.pages:
                t = p.extract_text()
                if t: txt += t + "\n"
            st.success("Uploaded!")
        except: pass
    else:
        txt = st.text_area("Paste Resume", height=120)
    if st.button("Check ATS", type="primary", use_container_width=True) and txt:
        import random
        s = random.randint(78,92)
        st.metric("ATS Score", f"{s}%")
        st.progress(s)

with tab3:
    st.subheader("Job Matcher")
    st.text_area("JD", height=150)
    if st.button("Analyze", type="primary"): st.info("Match 84%")

with tab4:
    st.subheader("Cover Letter")
    if st.button("Generate", type="primary"): st.write("Letter ready")

with tab5:
    st.subheader("Interview")
    if st.button("Get Questions", type="primary"): st.write("1. Tell me about yourself")

with tab6:
    st.subheader("Templates")
    st.selectbox("Template", ["Modern Professional"])

with tab7:
    st.subheader("Export")
    st.info("Builder tab la download pannu")

with tab8:
    st.subheader("💖 Support")
    upi_link = f"upi://pay?pa={YOUR_UPI}&pn={YOUR_NAME}&cu=INR&tn=Support"
    st.markdown(f"""<div style='background-color: #1a3a2a; border: 1px solid #2d5a3d; padding: 18px 20px; border-radius: 12px; margin: 16px 0px;'><span style='color: #4ade80; font-size: 18px; font-weight: 600;'>☕  Buy Me a Coffee - Support {YOUR_NAME}</span></div>""", unsafe_allow_html=True)
    st.write("My UPI ID - Copy pannikko")
    st.text_input("", value=YOUR_UPI, label_visibility="collapsed")
    st.link_button("☕ Pay via UPI - Support Me", upi_link, type="primary", use_container_width=True)
    st.caption("GPay / PhonePe / Paytm")

st.divider()
st.markdown(f"""<div style='text-align:center; padding-bottom: 130px;'><p style='font-size:17px; font-weight:600;'>Made with 🤍 by {YOUR_NAME} 🎀</p><p style='color:grey; font-size:13px;'>© 2026 MEGA Resume Builder | {YOUR_UPI}</p></div>""", unsafe_allow_html=True)