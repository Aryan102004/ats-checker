from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def base_similarity(resume_text, jd_text):
    docs = [resume_text, jd_text]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(docs)
    return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]


def simulate_ats_score(resume_text, jd_text, matched_skills, mode="Basic ATS"):
    """
    Simulates different ATS scoring algorithms.
    """

    similarity = base_similarity(resume_text, jd_text)

    # Skill match factor
    skill_factor = len(matched_skills) / 20
    if skill_factor > 1:
        skill_factor = 1

    if mode == "Basic ATS":
        score = similarity * 100

    elif mode == "Skill-Weighted ATS":
        score = (0.6 * similarity + 0.4 * skill_factor) * 100

    elif mode == "Experience-Boosted ATS":
        exp_bonus = 0.15 if "experience" in resume_text.lower() else 0.05
        score = (0.55 * similarity + 0.35 * skill_factor + exp_bonus) * 100

    else:
        score = similarity * 100

    return round(score, 2)
