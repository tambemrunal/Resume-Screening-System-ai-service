def calculate_education_match(
    candidate_education,
    preferred_education
):

    if not preferred_education:
        return 1.0

    matched = 0

    for edu in preferred_education:

        if edu.lower() in [
            e.lower()
            for e in candidate_education
        ]:
            matched += 1

    return matched / len(
        preferred_education
    )