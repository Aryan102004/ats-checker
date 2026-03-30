LEARNING_RESOURCES = {
    "python": "Learn Python: https://www.learnpython.org/",
    "sql": "SQL Basics: https://www.w3schools.com/sql/",
    "machine": "ML Course: https://www.coursera.org/learn/machine-learning",
    "learning": "ML Roadmap: https://roadmap.sh/ai-data-scientist",
    "nlp": "NLP Tutorial: https://www.analyticsvidhya.com/blog/category/nlp/",
    "docker": "Docker Guide: https://docs.docker.com/get-started/",
    "aws": "AWS Cloud Practitioner: https://aws.amazon.com/training/",
    "react": "React Docs: https://react.dev/learn"
}


def generate_learning_path(missing_skills):
    """
    Create a personalized roadmap based on missing skills.
    """

    roadmap = []

    for skill in missing_skills[:8]:
        if skill in LEARNING_RESOURCES:
            roadmap.append((skill.upper(), LEARNING_RESOURCES[skill]))
        else:
            roadmap.append((skill.upper(), "Search recommended course on Coursera/YouTube"))

    return roadmap
