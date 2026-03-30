import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def resume_chatbot(user_message, resume_context, jd_context):
    """
    Gemini Chatbot for Resume Guidance
    """

    prompt = f"""
You are an AI Resume & Career Assistant.

Resume Content:
{resume_context}

Job Description:
{jd_context}

User Question:
{user_message}

Answer professionally in a helpful way.
Give clear suggestions, bullet improvements, and skill guidance.
"""

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text
