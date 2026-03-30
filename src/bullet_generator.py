def generate_resume_bullets(missing_skills):
    bullets = []

    for skill in missing_skills[:5]:
        bullets.append(
            f"Implemented projects using **{skill.upper()}** to improve job-specific expertise."
        )

    if not bullets:
        bullets.append("Your resume already aligns strongly with job requirements.")

    return bullets
