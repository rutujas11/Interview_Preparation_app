# 🎯 AI-Powered Interview Preparation App

This is an AI-powered Streamlit app that helps users prepare for interviews by generating personalized questions using Google Generative AI (Gemini API).

## Link of Project : (https://crack-interview.streamlit.app/)

## 🔧 Features

- Upload resume or job description (PDF)
- Get AI-generated personalized interview questions
- Simple and interactive Streamlit interface

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/interview_preparation_app.git
cd interview_preparation_app
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add Google API Key
Create a file named .streamlit/secrets.toml and add your API key like this:

toml
Copy
Edit
[api_keys]
google_api_key = "YOUR_GOOGLE_API_KEY"
Replace "YOUR_GOOGLE_API_KEY" with your actual Gemini API key.

4. Run the App
bash
Copy
Edit
streamlit run app.py
🌐 Deploy on Streamlit Cloud
Push your code to GitHub.

Go to Streamlit Cloud and connect your repo.

In the app Settings > Secrets, add the following:

toml
Copy
Edit
[api_keys]
google_api_key = "YOUR_GOOGLE_API_KEY"
Click Deploy.


📩 Contact
For any questions or suggestions, feel free to open an issue or contact the maintainer.

yaml
Copy
Edit

---

✅ You can now copy this **entire file** into your project as `README.md`. Let me know if yo