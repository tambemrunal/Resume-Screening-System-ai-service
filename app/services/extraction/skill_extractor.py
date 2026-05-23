from app.utils.skills_database import SKILLS

def extract_skills(text: str):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))