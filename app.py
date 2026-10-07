import streamlit as st
from fpdf import FPDF
import io

MY_UPI_ID = "dileepkumar.m316@okicici"

st.set_page_config(page_title="Dileep Resume Builder", layout="centered")

st.title("🚀 AI Resume Builder - Chennai")
st.caption("Free ATS, JD Match, Cover Letter & More")

# --- INPUTS - Un screenshot maari ---
full_name = st.text_input("Full Name", "Dileep Kumar M")
role = st.text_input("Role", "Software Engineer")
email = st.text_input("Email", "dileep@gmail.com")
phone = st.text_input("Phone", "+91 98765 43210")
skills = st.text_input("Skills", "Python, React, SQL, AWS")
linkedin = st.text_input("LinkedIn", "linkedin.com/in/dileep")
about = st.text_area("About You", "Chennai based Software Engineer building AI tools")

st.divider()

tabs = st.tabs(["Resume", "ATS", "JD Match", "Cover Letter", "Portfolio", "Salary", "☕ Support"])

with tabs[0]:
    st.subheader("📄 Resume Preview")
    st.write(f"**{full_name}** - {role}")
    st.write(f"📧 {email} | 📞 {phone}")
    st.write(f"💻 {skills}")
    st.write(f"🔗 {linkedin}")
    st.write(f"👨‍💻 {about}")

    if st.button("Generate PDF", type="primary"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, txt=f"{full_name} - {role}", ln=True)
        pdf.multi_cell(0, 10, txt=f"Email: {email}\nPhone: {phone}\nLinkedIn: {linkedin}\n\nSkills: {skills}\n\nAbout: {about}")
        data = pdf.output(dest='S').encode('latin1')
        st.download_button("📥 Download Resume PDF", data, f"{full_name}_Resume.pdf", type="primary")

with tabs[1]:
    st.subheader("✅ ATS Score Checker")
    score = 70 + len(skills) % 30
    st.metric("Your ATS Score", f"{score}%")
    st.progress(score)
    if score < 80:
        st.warning("Add more keywords from Job Description da!")
    else:
        st.success("Super da! Resume ready for ATS!")

with tabs[2]:
    st.subheader("🎯 JD Matcher")
    jd = st.text_area("Paste Job Description here")
    if st.button("Check Match %"):
        match = len(set(skills.lower().split(',')) & set(jd.lower().split())) * 15
        st.metric("Match", f"{min(95, match+50)}%")
        st.info("Tip: Add missing skills to increase match!")

with tabs[3]:
    st.subheader("✉️ Cover Letter Generator")
    if st.button("Generate Cover Letter"):
        letter = f"""Dear Hiring Manager,

I am {full_name}, a passionate {role} with skills in {skills}.

{about}

I am excited to apply and contribute to your team.

Best Regards,
{full_name}
{email} | {phone}
{linkedin}
"""
        st.code(letter)

with tabs[4]:
    st.subheader("🌐 Portfolio Link")
    link = f"https://{full_name.lower().replace(' ','')}.vercel.app"
    st.code(link)
    st.link_button("Open Portfolio (Demo)", "https://vercel.com")

with tabs[5]:
    st.subheader("💰 Salary Predictor - Chennai 2026")
    exp = st.slider("Years of Experience", 0, 10, 2)
    if st.button("Predict Salary", type="primary"):
        base = 4.5 + exp*1.2
        if "python" in skills.lower(): base += 2.5
        if "aws" in skills.lower(): base += 2.0
        if "react" in skills.lower(): base += 1.5
        st.metric("Estimated CTC", f"Rs {base:.1f} - {base+4:.1f} LPA")
        st.progress(min(95, int(base*8))/100)

    st.divider()
    st.markdown("### ☕ Love this tool? Buy me a Coffee")
    st.caption("100% FREE forever. Your support helps me build more free tools ❤️")

    upi_link = f"upi://pay?pa={MY_UPI_ID}&pn=Dileep%20Kumar%20M&cu=INR&tn=Coffee%20Support"

    c1, c2 = st.columns(2)
    with c1:
        st.link_button("📱 GPay / PhonePe", upi_link, type="primary", use_container_width=True)
    with c2:
        st.code(MY_UPI_ID, language=None)

    st.write("👇 **GPay open aagalana QR scan pannu da!**")
    try:
        import qrcode
        qr = qrcode.make(upi_link)
        buf = io.BytesIO()
        qr.save(buf, format="PNG")
        st.image(buf.getvalue(), caption=f"Scan to Pay - {MY_UPI_ID}", width=250)
    except:
        st.info(f"UPI: {MY_UPI_ID} - Copy panni GPay la paste pannu")

    st.success("🔒 Any amount Rs.10, Rs.50 - un wish da! Direct to account!")

with tabs[6]:
    st.subheader("☕ Support Keeps it FREE")
    upi_link = f"upi://pay?pa={MY_UPI_ID}&pn=Dileep%20Kumar%20M&cu=INR&am=50&tn=Thanks"
    st.link_button("📱 Donate via GPay/PhonePe - Rs.50", upi_link, type="primary", use_container_width=True)
    st.code(MY_UPI_ID)
    try:
        import qrcode
        buf = io.BytesIO()
        qrcode.make(upi_link).save(buf, format="PNG")
        st.image(buf.getvalue(), width=200, caption="Scan & Support")
    except:
        pass
    st.caption("Secure UPI - 2 sec la support pannalam!")