import streamlit as st

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="centered")

st.title("📄 AI-Powered Resume Analyzer & Match Score")
st.write("Scan resumes against job descriptions using smart text logic!")

resume_text = st.text_area("Paste Resume Text Here:")
job_description = st.text_area("Paste Job Description (JD) Here:")

if st.button("Analyze Match Score"):
    if resume_text and job_description:
        # Basic matching logic simulation using keywords
        resume_words = set(resume_text.lower().split())
        jd_words = set(job_description.lower().split())
        
        if jd_words:
            common_words = resume_words.intersection(jd_words)
            score = int((len(common_words) / len(jd_words)) * 100)
            if score > 100:
                score = 100
        else:
            score = 0
            
        st.subheader("📊 Results")
        st.metric(label="Match Score", value=f"{score}%")
        
        if score > 75:
            st.success("Great match! This resume fits the job description very well.")
        elif score > 40:
            st.warning("Moderate match. Some key skills might be missing.")
        else:
            st.error("Low match. Significant skill gaps found.")
    else:
        st.warning("Please enter both resume text and job description.")
