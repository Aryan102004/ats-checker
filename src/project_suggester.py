def suggest_projects(missing_skills):
    projects = []

    if "nlp" in missing_skills:
        projects.append("Build a Resume Screening System using NLP + TF-IDF")

    if "docker" in missing_skills:
        projects.append("Containerize a Streamlit App using Docker")

    if "aws" in missing_skills:
        projects.append("Deploy your ATS Checker on AWS EC2 or S3")

    if "react" in missing_skills:
        projects.append("Create a Frontend Dashboard for ATS Reports in React")

    if "sql" in missing_skills:
        projects.append("Build a Job Application Tracker using SQL Database")

    if not projects:
        projects.append("Create an Advanced Portfolio Website + Resume Optimizer")

    return projects
