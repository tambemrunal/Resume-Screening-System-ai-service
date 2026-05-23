def calculate_match_score(
    total_required,
    matched_count
):

    if total_required == 0:
        return 0

    score = (
        matched_count / total_required
    ) * 100

    return round(score, 2)