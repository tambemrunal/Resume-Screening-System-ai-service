from app.services.semantic.embedding_service import (
    generate_embedding
)

from app.services.semantic.cosine_similarity import (
    calculate_similarity
)

SEMANTIC_THRESHOLD = 0.65

def semantic_match(
    candidate_skills,
    required_skills
):

    matches = []

    missing = []

    for required_skill in required_skills:

        best_score = 0
        best_match = None

        required_embedding = generate_embedding(
            required_skill
        )

        for candidate_skill in candidate_skills:

            candidate_embedding = generate_embedding(
                candidate_skill
            )

            score = calculate_similarity(
                required_embedding,
                candidate_embedding
            )

            if score > best_score:
                best_score = score
                best_match = candidate_skill

        if best_score >= SEMANTIC_THRESHOLD:

            matches.append({
                "required_skill": required_skill,
                "matched_with": best_match,
                "score": round(best_score, 2)
            })

        else:
            missing.append(required_skill)

    return {
        "matches": matches,
        "missing_skills": missing
    }