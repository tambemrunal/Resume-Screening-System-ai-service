def calculate_experience_match(
    candidate_experience,
    required_experience
):

    if required_experience == 0:
        return 1.0

    ratio = (
        candidate_experience /
        required_experience
    )

    return min(ratio, 1.0)