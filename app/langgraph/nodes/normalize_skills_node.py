from app.services.semantic.skill_normalizer import (
    normalize_skills
)

def normalize_skills_node(state):

    normalized = normalize_skills(
        state["candidate_skills"]
    )

    return {
        **state,
        "normalized_skills": normalized
    }