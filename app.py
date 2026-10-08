import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="MEGA Resume Builder", page_icon="🚀", layout="centered")

st.title("🚀 MEGA Resume Builder")
st.markdown("**AI-powered resume builder that creates professional ATS-friendly resumes in seconds**")
st.divider()

FIELDS = ["name", "email", "phone", "linkedin", "github",
          "location", "summary", "skills", "experience", "education"]

def clear_all():
    for k in FIELDS:
        st.session_state[k] = ""

# --- FORM ---
with st.form("resume_form"):
    st.subheader("Personal Details")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name *", key="name", placeholder="e.g. John Doe")
        email = st.text_input("Email *", key="email", placeholder="you@example.com")
        phone = st.text_input("Phone", key="phone", placeholder="+91 XXXXXXXXXX")
    with col2:
        linkedin = st.text_input("LinkedIn", key="linkedin", placeholder="linkedin.com/in/username")
        github = st.text_input("GitHub", key="github", placeholder="github.com/username")
        location = st.text_input("Location", key="location", placeholder="City, State")

    st.subheader("Professional Summary")
    summary = st.text_area("Summary", key="summary", height=100,
                           placeholder="2-3 lines about your skills and goals")

    st.subheader("Skills (comma separated)")
    skills = st.text_input("Skills", key="skills",
                           placeholder="Python, SQL, Embedded C, MATLAB")

    st.subheader("Experience / Projects")
    experience = st.text_area("Experience", key="experience", height=150,
                              placeholder="Project name - what you built\n- Key result 1\n- Key result 2")

    st.subheader("Education")
    education = st.text_area("Education", key="education", height=80,
                             placeholder="Degree - College (Years)\nCGPA: X/10")

    c1, c2 = st.columns(2)
    submit = c1.form_submit_button("🔥 GENERATE RESUME")
    c2.form_submit_button("🗑️ Clear All", on_click=clear_all)

# --- PDF ---
def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", 'B', 24)
    pdf.cell(0, 12, name.upper(), ln=True, align='C')
    pdf.ln(2)

    pdf.set_font("Arial", '', 10)
    contact1 = " | ".join(x for x in [email, phone, location] if x)
    contact2 = " | ".join(x for x in [linkedin, github] if x)
    pdf.cell(0, 6, contact1, ln=True, align='C')
    if contact2:
        pdf.cell(0, 6, contact2, ln=True, align='C')
    pdf.ln(8)

    def section(title, text):
        if not text.strip():
            return
        pdf.set_font("Arial", 'B', 12)
        pdf.set_fill_color(240, 240, 240)
        pdf.cell(0, 8, f"  {title}", ln=True, fill=True)
        pdf.set_font("Arial", '', 10)
        pdf.multi_cell(0, 6, text)
        pdf.ln(4)

    section("PROFESSIONAL SUMMARY", summary)
    section("SKILLS", skills)
    section("EXPERIENCE & PROJECTS", experience)
    section("EDUCATION", education)

    output = pdf.output(dest='S')
    return output.encode('latin-1') if isinstance(output, str) else bytes(output)

if submit:
    if not name.strip() or not email.strip():
        st.warning("Please fill in the required fields (*)")
    else:
        try:
            pdf_bytes = create_pdf()
            st.success("✅ Resume generated successfully!")
            st.download_button(
                label="📥 DOWNLOAD YOUR MEGA RESUME",
                data=pdf_bytes,
                file_name=f"{name.strip().replace(' ', '_')}_Resume.pdf",
                mime="application/pdf",
            )
        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.caption("Made with ❤️ by Dileep Kumar M | MEGA Resume Builder")
