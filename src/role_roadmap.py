ROLE_ROADMAPS = {
    "Data Scientist": [
        "Learn Python + Statistics",
        "Master SQL + Data Analysis",
        "Build ML Models (Regression/Classification)",
        "Deep Learning + TensorFlow",
        "Deploy ML Projects"
    ],
    "Web Developer": [
        "Learn HTML, CSS, JavaScript",
        "Master React + Node.js",
        "Work with APIs + Databases",
        "Deploy Full Stack Projects",
        "Build Strong Portfolio"
    ],
    "DevOps Engineer": [
        "Learn Linux + Networking Basics",
        "Master Docker + Kubernetes",
        "CI/CD with Jenkins/GitHub Actions",
        "Cloud Platforms (AWS/Azure)",
        "Infrastructure Automation"
    ]
}


def get_role_based_roadmap(role):
    return ROLE_ROADMAPS.get(role, [])
