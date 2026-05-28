def calculate_match_score(
    required_skill_count,
    matched_skill_count
):

    if required_skill_count <= 0:

        return 0.0

    score = (
        matched_skill_count
        / required_skill_count
    ) * 100

    return round(
        min(score, 100.0),
        2
    )