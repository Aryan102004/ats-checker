import re


def extract_section(text, start_keywords, end_keywords):
    """
    Extract a section from resume text using heading keywords.
    """

    text = text.lower()

    # Find start position
    start_pos = -1
    for key in start_keywords:
        match = re.search(rf"\b{key}\b", text)
        if match:
            start_pos = match.start()
            break

    if start_pos == -1:
        return ""

    # Find end position
    end_pos = len(text)
    for key in end_keywords:
        match = re.search(rf"\b{key}\b", text[start_pos + 1:])
        if match:
            end_pos = start_pos + match.start()
            break

    return text[start_pos:end_pos]


def extract_resume_sections(resume_text):
    """
    Extract Skills, Experience, Education sections.
    """

    skills = extract_section(
        resume_text,
        start_keywords=["skills", "technical skills"],
        end_keywords=["experience", "projects", "education"]
    )

    experience = extract_section(
        resume_text,
        start_keywords=["experience", "internship", "work experience"],
        end_keywords=["projects", "education", "skills"]
    )

    education = extract_section(
        resume_text,
        start_keywords=["education", "qualification"],
        end_keywords=["skills", "experience", "projects"]
    )

    return skills, experience, education
