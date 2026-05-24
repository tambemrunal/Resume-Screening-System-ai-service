def calculate_domain_similarity(
    candidate_domains,
    preferred_domains
):

    if not preferred_domains:
        return 1.0

    matched = 0

    for domain in preferred_domains:

        if domain.lower() in [
            d.lower()
            for d in candidate_domains
        ]:
            matched += 1

    return matched / len(
        preferred_domains
    )