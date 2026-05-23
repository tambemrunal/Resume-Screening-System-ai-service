def explanation_node(state):

    matched = len(state["matched_skills"])

    missing = len(state["missing_skills"])

    explanation = (
        f"Candidate matched {matched} skills. "
        f"{missing} required skills missing. "
        f"Overall semantic match score is "
        f"{state['match_score']}%"
    )

    return {
        **state,
        "explanation": explanation
    }