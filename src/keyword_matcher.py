import re

STOPWORDS = {
    "the", "and", "is", "in", "to", "of", "for", "on", "with", "a", "an",
    "as", "at", "by", "from", "or", "that", "this", "it", "be", "are",
    "was", "were", "will", "can", "has", "have", "had", "your", "you",
    "we", "our", "they", "their", "but", "not", "if", "into", "than",
    "then", "so", "such"
}

# ✅ Skill Dictionary (ATS Focus)
SKILLS = {
    # Programming Languages
    "python", "java", "c", "c++", "javascript", "typescript", "sql", "r",

    # Web Development
    "html", "css", "react", "angular", "vue", "node", "express",
    "flask", "django", "streamlit", "spring", "bootstrap",

    # Databases
    "mysql", "postgresql", "mongodb", "sqlite", "oracle", "firebase",

    # Data Science & Analytics
    "pandas", "numpy", "matplotlib", "statistics", "excel", "powerbi",
    "tableau", "data", "analysis", "visualization",

    # Machine Learning
    "machine", "learning", "regression", "classification", "clustering",
    "scikit", "sklearn", "model", "training", "prediction",

    # Deep Learning
    "deep", "neural", "networks", "tensorflow", "pytorch", "keras",

    # NLP Skills
    "nlp", "spacy", "nltk", "transformers", "bert", "gpt",
    "tokenization", "embedding",

    # Computer Vision
    "opencv", "cnn", "image", "detection",

    # DevOps & Tools
    "git", "github", "docker", "kubernetes", "jenkins",
    "linux", "bash",

    # Cloud Platforms
    "aws", "azure", "gcp", "cloud", "deployment",

    # Software Engineering
    "api", "rest", "microservices", "testing", "debugging",
    "agile", "scrum",

    # Security Basics
    "authentication", "authorization", "encryption",

    # Other Common ATS Keywords
    "project", "internship", "experience", "communication",
    "teamwork", "leadership"
}



def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text


def extract_keywords(words):
    """Return only ATS-relevant skill words"""
    return {word for word in words if word in SKILLS}


def find_skill_gap(resume_text, job_description):
    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    resume_words = set(resume_text.split())
    jd_words = set(job_description.split())

    # Remove stopwords
    resume_words = {w for w in resume_words if w not in STOPWORDS}
    jd_words = {w for w in jd_words if w not in STOPWORDS}

    # Extract only skills
    resume_skills = extract_keywords(resume_words)
    jd_skills = extract_keywords(jd_words)

    matched_skills = sorted(list(resume_skills.intersection(jd_skills)))
    missing_skills = sorted(list(jd_skills.difference(resume_skills)))

    return matched_skills, missing_skills
