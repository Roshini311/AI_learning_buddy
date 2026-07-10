# AI Learning Buddy 🤖

This project is an interactive AI-powered Learning Buddy built with Streamlit and OpenAI. It acts as a specialized tutor designed to help users prepare for software engineering interviews, specifically focusing on core concepts like **Binary Search**. 

It explains concepts simply, provides real-world analogies, tests understanding via quizzes, and evaluates answers with encouraging feedback.

---

## 🎯 Features

- **Topic Selection:** Choose between multiple computer science topics.
- **Learner Level Adjustment:** Tailor the AI's explanations for Beginner, Intermediate, or Advanced levels.
- **Interactive Chat Interface:** Natural, conversational learning flow.
- **Quick Actions:** Single-click buttons to instantly generate an Explanation, a Real-Life Example, a Quiz, or Evaluate your answers.
- **Progress Tracking:** Tracks the number of messages and quizzes taken during your session.
- **Mock Mode:** Can run locally without an OpenAI API key (provides static placeholder responses for testing).
- **Responsible AI:** Includes a built-in safety disclaimer regarding AI hallucination mitigation.

---

## 🚀 Installation & Local Setup

Follow these steps to run the application on your local machine:

### 1. Clone the repository (or download the folder)
Ensure you are in the `AI_Learning_Buddy` directory.

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
1. Rename `.env.example` to `.env`.
2. Open the `.env` file and replace `your_openai_api_key_here` with your actual OpenAI API key.
   *(Note: If you do not have an API key, leave the file as is or do not create it. The application will automatically fall back to "Mock Mode" so you can still view the UI and test the buttons!)*

### 5. Run the Application
```bash
streamlit run app.py
```
Your browser should automatically open to `http://localhost:8501`.

---

## ☁️ Deployment Guide (Streamlit Community Cloud)

To make this app accessible on the internet, deploy it using Streamlit Community Cloud:

1. **Upload to GitHub:**
   - Create a new repository on GitHub.
   - Upload the `app.py` and `requirements.txt` files to the repository.
   - *(Note: Never upload your `.env` file containing the API key).*

2. **Connect to Streamlit:**
   - Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
   - Click **"New app"**.
   - Select the repository, branch (usually `main`), and the main file path (`app.py`).

3. **Configure Secrets (API Key):**
   - Click on **"Advanced settings..."** before clicking deploy.
   - In the "Secrets" field, add your OpenAI API key like this:
     ```toml
     OPENAI_API_KEY="sk-your-actual-api-key-here"
     ```
   - Click **Save**.

4. **Deploy:**
   - Click **"Deploy!"**. Wait 1-2 minutes for Streamlit to spin up the container and install dependencies.
   - Your app is now live!

### Common Deployment Errors & Solutions
- **ModuleNotFoundError:** Ensure all imported libraries (like `openai`, `python-dotenv`) are correctly spelled in `requirements.txt`.
- **OpenAI Authentication Error:** Double-check that your API key is correctly entered in the Streamlit Secrets (without any extra spaces or missing quotes).

---

## 📸 Screenshots



- **Home Page:** `assets/home.png`
- **Explanation:** `assets/explanation.png` 
- **Quiz:** `assets/quiz.png`
- **Feedback:** `assets/feedback.png`
- **Conversation:** `assets/conversation.png`

---

##wesite_URL: https://ailearningbuddy-4pfiaw5vc4rkxsvawvne5r.streamlit.app/


## 📋 Assignment Submission Checklist

Before submitting your assignment zip file, ensure you have included:
- [x] `report.md` (Contains Topic Selection, Persona, Conversation, Quiz, Reflection, Responsible AI)
- [x] `prompts.md` (Contains the 5 prompt templates)
- [x] `app.py` (The main application code)
- [x] `requirements.txt` (Dependencies)
- [x] `README.md` (This file)
- [ ] `assets/` directory populated with your 5 captured screenshots

---
*Developed for the AI Learning Buddy University Assignment.*
