import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def gemini_ai_advisor(score, matched_skills, missing_skills, target_role):
    """
    Uses Gemini AI to generate personalized career suggestions.
    """

    prompt = f"""
You are an expert ATS Resume Career Advisor.

Candidate ATS Score: {score}%
Target Role: {target_role}

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

Generate the following:

1. Short Career Summary (2 lines)
2. Personalized Learning Path (5 steps)
3. 3 Project Ideas to cover missing skills
4. 3 ATS-friendly Resume Bullet Improvements

Return response in clear numbered format.
"""

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text
