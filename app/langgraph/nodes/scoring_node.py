from app.services.semantic.weighted_scorer import (
    calculate_match_score
)

def scoring_node(state):

    score = calculate_match_score(
        len(state["required_skills"]),
        len(state["matched_skills"])
    )

    return {
        **state,
        "match_score": score
    }