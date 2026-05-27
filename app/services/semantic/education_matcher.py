import re

from app.services.semantic.embedding_service import (
    generate_embedding,
)

from app.services.semantic.cosine_similarity import (
    calculate_similarity,
)


EDUCATION_ALIASES = {
    "bachelors degree": "bachelor degree",
    "bachelor's degree": "bachelor degree",
    "bachelor of engineering": "bachelor engineering",
    "b.e": "bachelor engineering",
    "b.e.": "bachelor engineering",
    "be": "bachelor engineering",
    "b.tech": "bachelor technology",
    "b.tech.": "bachelor technology",
    "computer science engineering": "computer engineering",
    "computer science": "computer engineering",
    "cs": "computer engineering",
    "it": "information technology",
    "information technology": "computer engineering",
    "engineering": "bachelor engineering",
    "undergraduate": "bachelor",
    "graduate": "bachelor",
    "postgraduate": "master",
    "masters": "master",
    "master's degree": "master degree",
    "master degree": "master degree",
    "m.e": "master engineering",
    "m.e.": "master engineering",
    "m.tech": "master technology",
    "m.tech.": "master technology",
}


def _normalize_education(value: str):

    normalized = re.sub(
        r"[^a-z0-9 ]",
        " ",
        value.lower().strip(),
    )

    normalized = " ".join(normalized.split())

    return EDUCATION_ALIASES.get(normalized, normalized)


def _best_semantic_match(source_items, target_item):

    if not source_items:
        return 0.0

    target_normalized = _normalize_education(target_item)

    target_embedding = generate_embedding(target_normalized)

    best_score = 0.0

    for source_item in source_items:

        source_normalized = _normalize_education(source_item)

        if source_normalized == target_normalized:
            return 1.0

        source_embedding = generate_embedding(source_normalized)

        similarity = calculate_similarity(
            source_embedding,
            target_embedding,
        )

        if similarity > best_score:
            best_score = similarity

    return best_score


def calculate_education_match(
    candidate_education,
    preferred_education
):

    if not preferred_education:
        return 1.0

    if not candidate_education:
        return 0.0

    scores = []

    for edu in preferred_education:

        scores.append(
            _best_semantic_match(
                candidate_education,
                edu,
            )
        )

    return sum(scores) / len(scores)