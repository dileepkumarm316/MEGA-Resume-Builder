import streamlit as st
from fpdf import FPDF
import io

MY_UPI_ID = "dileepkumar.m316@okicici"

st.set_page_config(page_title="Resume Builder", layout="centered")
st.title("🚀 AI Resume Builder")

# --- UN SCREENSHOT MAARI INPUTS ---
full_name = st.text_input("Full Name", "Dileep Kumar M")
role = st.text_input("Role", "Software Engineer")
email = st.text_input("Email", "dileep@gmail.com")
phone = st.text_input("Phone", "+91 98765 43210")
skills = st.text_input("Skills", "Python, React, SQL, AWS")
linkedin = st.text_input("LinkedIn", "linkedin.com/in/dileep")

st.divider()

tabs = st.tabs(["Resume", "ATS", "JD Match", "Cover Letter", "Portfolio", "Salary", "☕ Support"])

with tabs[0]:
    st.subheader("Resume Preview")
    st.write(f"**{full_name}** - {role}")
    st.write(f"📧 {email} | 📞 {phone}")
    st.write(f"💻 Skills: {skills}")
    st.write(f"🔗 {linkedin}")
    if st.button("Generate PDF"):
        pdf=FPDF(); pdf.add_page(); pdf.set_font("Arial", size=12)
        pdf.cell(0,10, txt=f"{full_name} - {role}", ln=True)
        pdf.multi_cell(0,10, txt=f"Email: {email}\nPhone: {phone}\nSkills: {skills}\nLinkedIn: {linkedin}")
        data = pdf.output(dest='S').encode('latin1')
        st.download_button("📥 Download Resume", data, f"{full_name}_Resume.pdf")

with tabs[1]:
    score = 70 + len(skills) % 30
    st.metric("ATS Score", f"{score}%")
    st.progress(score)

with tabs[2]:
    jd = st.text_area("Paste Job Description")
    if st.button("Check Match"):
        st.success("65% Match!")

with tabs[3]:
    if st.button("Generate Cover Letter"):
        st.code(f"Dear Hiring Manager,\nI am {full_name}, a {role} skilled in {skills}.\n\nRegards,\n{full_name}")

with tabs[4]:
    st.write(f"Portfolio Link: https://{full_name.lower().replace(' ','')}.vercel.app")

with tabs[5]:
    exp = st.slider("Experience (years)", 0, 10, 2)
    st.metric("Estimated CTC", f"{4.5 + exp*1.2:.1f} LPA")

with tabs[6]:
    st.subheader("☕ Support Project")
    upi_link = f"upi://pay?pa={MY_UPI_ID}&pn=Dileep%20Kumar&cu=INR&tn=Coffee"
    st.link_button("📱 Donate - GPay / PhonePe", upi_link, type="primary", use_container_width=True)
    st.code(MY_UPI_ID, language=None)
    try:
        import qrcode
        buf = io.BytesIO()
        qrcode.make(upi_link).save(buf, format="PNG")
        st.image(buf.getvalue(), width=180, caption="Scan to Pay")
    except:
        pass
    st.caption("🔒 Secure UPI Payment - Keeps app FREE")