from app.services.semantic.ontology import RELATED_SKILLS

def expand_skills(skills: list):

    expanded = set(skills)

    for skill in skills:

        related = RELATED_SKILLS.get(skill.lower(), [])

        for item in related:
            expanded.add(item)

    return list(expanded)