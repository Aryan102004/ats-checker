from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.section_extractor import extract_resume_sections


def section_score(resume_section, jd_text):
    if resume_section.strip() == "":
        return 0.0

    documents = [resume_section, jd_text]

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(documents)

    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

    return round(score * 100, 2)


def calculate_section_wise_score(resume_text, job_description):
    # Extract sections properly
    skills_text, exp_text, edu_text = extract_resume_sections(resume_text)

    # Calculate scores
    skills_score = section_score(skills_text, job_description)
    experience_score = section_score(exp_text, job_description)
    education_score = section_score(edu_text, job_description)

    overall = round((skills_score + experience_score + education_score) / 3, 2)

    return skills_score, experience_score, education_score, overall
