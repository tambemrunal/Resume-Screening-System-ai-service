from app.services.semantic.skill_expander import (
    expand_skills
)

def expand_skills_node(state):

    expanded = expand_skills(
        state["normalized_skills"]
    )

    return {
        **state,
        "expanded_skills": expanded
    }