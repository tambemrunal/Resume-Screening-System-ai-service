from app.services.semantic.semantic_matcher import (
    semantic_match
)

def semantic_match_node(state):

    result = semantic_match(
        state["expanded_skills"],
        state["required_skills"]
    )

    return {
        **state,
        "matched_skills": result["matches"],
        "missing_skills": result["missing_skills"]
    }