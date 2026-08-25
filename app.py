import streamlit as st
import os
from agent import extract_text_from_pdf, get_ats_score

st.set_page_config(page_title="HireLens 2.0")
st.title("🚀 HireLens 2.0 - AI Recruiter Agent")
st.write("Built by Shrawani - Ranks 11 resumes in 30 seconds")

api_key = st.text_input("Paste your Gemini API Key here", type="password")
jd = st.text_area("Paste Job Description", height=150, value="Python Developer, Machine Learning, Data Analysis - Freshers 0-2 years")

uploaded_files = st.file_uploader("Upload Resumes (PDF)", accept_multiple_files=True, type="pdf")

if st.button("🔥 Rank All Resumes"):
    if not api_key:
        st.error("Please paste API Key!")
    elif not jd:
        st.error("Please paste Job Description!")
    elif not uploaded_files:
        st.error("Please upload at least 1 resume PDF! - See above upload box")
    else:
        st.info(f"Ranking {len(uploaded_files)} resumes...")
        for file in uploaded_files:
            # Save temp file
            with open(file.name, "wb") as f:
                f.write(file.getbuffer())
            resume_text = extract_text_from_pdf(file.name)
            result = get_ats_score(jd, resume_text, api_key)
            
            st.divider()
            st.subheader(f"📄 {file.name}")
            st.success(result)
            # delete temp
            os.remove(file.name)

st.write("---")
st.write("Tip: Upload PDFs from your resume folder")