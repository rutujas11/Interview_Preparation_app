import streamlit as st 
import google.generativeai as genai
import pdfplumber
import io

api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="🎯 Interview Prep App", layout = "wide")
st.title("🎯 AI_Powered Interview Preparation")
st.write("Generate Personalized interview questions based on your role, skills, resume, and projects.")

question_type = st.selectbox("🧠 What type of questions do you want?", ["Technical", "Behavioural","Situational"])

with st.form("interview_form"):
    num_questions = st.slider("Number of questions",3, 20, 5)
    
    
            
    # if not resume_text:
    #     resume_text = st.text_area("Or paste Your Resume", height=150)
        
    if question_type == "Technical":
        role = st.text_input("👩‍💻 Job Role", placeholder="e.g.,Data Scientist")
        topics = st.text_input("📘 Topics (comma-separated)", placeholder="e.g., Python, SQL, ML")
        difficulty = st.selectbox("📈 Difficulty Level", ["Easy","Medium","Hard"])
        resume_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])
        resume_text = ""
        if resume_file is not None:
            with pdfplumber.open(io.BytesIO(resume_file.read())) as pdf:
                resume_text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
        
    submitted = st.form_submit_button("Generate Questions")
    
    
if submitted:
    with st.spinner("Generating your Questions...👩‍💻"):
        base_prompt = f"""
You are an AI Assistant helping a candidate prepare for a **{question_type}** interview questions.

Number of Questions: {num_questions}
""" 

        if question_type == "Technical":
            base_prompt += f"""
Role: {role}
Topics to focus on: {topics}
Difficulty: {difficulty}
"""

        base_prompt += """

Generate professional, non-casual interview questions based on the above inputs.
Also include answers in detail.and

Format:
Question 1: <text>
Answer: <model-suggested points or tips>
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
       
        response = model.generate_content(base_prompt)
        questions = response.text.strip()
        
        st.subheader("📋 Interview Questions")
        st.text_area("Generated Questions", questions, height=500)
        st.download_button("Download as Text", questions, file_name="interview_questions.txt")
