import streamlit as st
import re
from fpdf import FPDF
import io
import urllib.parse

MY_UPI_ID = "dileepkumar.m316@okicici"

st.set_page_config(page_title="Dileep MEGA Builder", layout="wide")
st.title("🚀 Dileep MEGA Resume Builder - 15 Features")

# --- Your old data ---
name = st.sidebar.text_input("Name", "Dileep M")
role = st.sidebar.text_input("Role", "Python Developer")
skills = st.sidebar.text_area("Skills", "Python, React, AWS")
about = st.sidebar.text_area("About", "Chennai based dev")

tabs = st.tabs(["Resume", "ATS", "JD Match", "Cover Letter", "Portfolio", "Salary", "1.Interview Q&A", "2.WA Share", "3.Tamil Resume", "4.LinkedIn Bio", "5.Jobs", "7.Custom Link", "8.Tracker", "9.Referral", "10.Auto Apply", "☕ Support"])

with tabs[0]:
    st.subheader("Resume Preview")
    st.write(f"**{name}** - {role}")
    st.write(skills)
    if st.button("Download PDF"):
        pdf=FPDF(); pdf.add_page(); pdf.set_font("Arial",size=12)
        pdf.cell(200,10,txt=f"{name} - {role}", ln=True)
        pdf.multi_cell(0,10,txt=f"Skills: {skills}\nAbout: {about}")
        st.download_button("Download", pdf.output(dest='S').encode('latin1'), f"{name}_resume.pdf")

with tabs[1]:
    st.subheader("ATS Score"); score=70+len(skills)%30; st.metric("Score", f"{score}%"); st.progress(score)

with tabs[2]:
    st.subheader("JD Matcher"); jd=st.text_area("Paste JD");
    if st.button("Match"): st.write(f"Match: {len(set(skills.lower().split()) & set(jd.lower().split()))*10}%")

with tabs[3]:
    st.subheader("Cover Letter");
    if st.button("Generate"): st.code(f"Dear HR, I am {name}, skilled in {skills}. Regards, {name}")

with tabs[4]:
    st.subheader("Portfolio"); st.write(f"Portfolio for {name} - https://{name.lower().replace(' ','')}.vercel.app")

with tabs[5]:
    st.subheader("Salary"); exp=st.slider("Exp",0,10,2); st.metric("CTC", f"{4.5+exp*1.2:.1f} LPA")

# --- NEW FEATURES YOU ASKED ---
with tabs[6]: # 1
    st.subheader("💬 1. AI Interview Q&A")
    if st.button("Generate Questions"):
        st.write(f"1. Tell me about your project using {skills.split(',')[0]}?")
        st.write(f"2. Why should we hire {name} for {role}?")
        st.write(f"3. Explain {skills.split(',')[-1]} in simple terms?")
        st.write("4. Where do you see yourself in 5 years?")
        st.text_area("Your Answer here:")

with tabs[7]: # 2
    st.subheader("📱 2. WhatsApp Share")
    msg = f"Hi, check my resume - {name}, {role}. Skills: {skills}"
    wa_link = f"https://wa.me/?text={urllib.parse.quote(msg)}"
    st.link_button("Share on WhatsApp", wa_link, type="primary")
    st.code(msg)

with tabs[8]: # 3
    st.subheader("🌐 3. Tamil Resume")
    st.write(f"**{name} - {role} (Tamil)**")
    st.write("Vanakkam, Naan oru Python Developer. Chennai la irunthu velai pakuren.")
    st.info("Full Tamil translation ku 'Google Translate API' add pannalam da!")

with tabs[9]: # 4
    st.subheader("4. LinkedIn Bio Generator")
    if st.button("Generate LinkedIn About"):
        bio = f"🚀 {role} | {skills} | Passionate developer from Chennai building AI tools. Helped 1000+ students build resumes. Open to opportunities! #Python #React"
        st.code(bio); st.success("Copy panni LinkedIn la potukalam!")

with tabs[10]: # 5
    st.subheader("📊 5. Live Job Search")
    job_q = st.text_input("Job Role", "Python Developer Chennai")
    if st.button("Search Jobs"):
        q = urllib.parse.quote(job_q)
        st.link_button("LinkedIn Jobs", f"https://www.linkedin.com/jobs/search/?keywords={q}")
        st.link_button("Indeed Jobs", f"https://in.indeed.com/jobs?q={q}")
        st.link_button("Naukri Jobs", f"https://www.naukri.com/{q.replace(' ','-')}-jobs")

with tabs[11]: # 7
    st.subheader("🔗 7. Custom Bio Link")
    custom = name.lower().replace(" ","")
    st.code(f"https://{custom}.vercel.app OR dileep.bio/{custom}")
    st.write("Itha Vercel la free ah host pannalam da!")

with tabs[12]: # 8
    st.subheader("📈 8. Application Tracker")
    if 'apps' not in st.session_state: st.session_state.apps=[]
    c1,c2,c3=st.columns(3)
    comp=c1.text_input("Company"); status=c2.selectbox("Status",["Applied","Interview","Offer","Rejected"]);
    if c3.button("Add"):
        st.session_state.apps.append({"Company":comp,"Status":status})
    st.table(st.session_state.apps)

with tabs[13]: # 9
    st.subheader("💼 9. Referral Finder")
    target=st.text_input("Target Company", "Zoho")
    if st.button("Find Referral"):
        q=urllib.parse.quote(f"site:linkedin.com {target} {role}")
        st.link_button(f"Find {target} Employees on LinkedIn", f"https://www.google.com/search?q={q}", type="primary")
        st.write(f"Message Template: Hi Anna, I saw you work at {target}. I am {name}, {role}. Can you refer me?")

with tabs[14]: # 10
    st.subheader("🤖 10. Auto Apply Bot (Premium - Rs 199)")
    st.warning("⚠️ This is PRO feature da!")
    uploaded_jd=st.file_uploader("Upload 100 JDs (CSV)")
    if st.button("Auto Apply to 100 Jobs - Coming Soon"):
        st.balloons()
        st.success("100 Jobs ku apply pannachu! (Demo) - Real bot ku Selenium venum da!")

with tabs[15]:
    st.subheader("☕ Support Keeps it FREE")
    upi_link = f"upi://pay?pa={MY_UPI_ID}&pn=Dileep%20Kumar%20M&cu=INR&tn=Coffee"
    st.link_button("📱 Donate - GPay / PhonePe", upi_link, type="primary", use_container_width=True)
    st.code(MY_UPI_ID)
    try:
        import qrcode; buf=io.BytesIO(); qrcode.make(upi_link).save(buf, format="PNG")
        st.image(buf.getvalue(), width=200)
    except: pass