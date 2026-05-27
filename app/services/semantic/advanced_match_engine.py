from app.services.semantic.semantic_matcher import (
    semantic_match
)

from app.services.semantic.experience_matcher import (
    calculate_experience_match
)

from app.services.semantic.education_matcher import (
    calculate_education_match
)

from app.services.semantic.domain_similarity_matcher import (
    calculate_domain_similarity
)

from app.services.semantic.project_relevance_matcher import (
    calculate_project_relevance
)

from app.services.semantic.advanced_weighted_scorer import (
    calculate_final_score
)

from app.services.semantic.embedding_service import (
    generate_embedding
)

from app.services.semantic.cosine_similarity import (
    calculate_similarity
)

from app.services.semantic.skill_normalizer import (
    normalize_skills
)

def advanced_match_engine(

    candidate_data,

    job_data,

    candidate_text=None,

    job_text=None,

    candidate_embedding=None,

    job_embedding=None,
):

    candidate_data = candidate_data or {}

    job_data = job_data or {}

    candidate_text = candidate_text or candidate_data.get("resume_text") or ""

    job_text = job_text or job_data.get("jd_text") or job_data.get("raw_jd_text") or ""

    candidate_skills = normalize_skills(
        candidate_data.get("skills") or []
    )

    candidate_projects = candidate_data.get("projects") or []

    candidate_experience = candidate_data.get("experience") or 0

    candidate_education = candidate_data.get("education") or []

    candidate_domains = candidate_data.get("domains") or []

    required_skills = normalize_skills(
        job_data.get("required_skills") or []
    )

    minimum_experience = job_data.get("minimum_experience") or 0

    preferred_education = job_data.get("preferred_education") or []

    preferred_domains = job_data.get("preferred_domains") or []

    def _context_similarity_score(items, context_text, top_n=3):

        if not items or not context_text:
            return 0.0

        context_embedding = generate_embedding(context_text)

        scores = []

        for item in items:

            item_text = str(item).strip()

            if not item_text:
                continue

            item_embedding = generate_embedding(item_text)

            scores.append(
                calculate_similarity(
                    item_embedding,
                    context_embedding,
                )
            )

        if not scores:
            return 0.0

        scores.sort(reverse=True)

        top_scores = scores[: min(top_n, len(scores))]

        average_top_scores = sum(top_scores) / len(top_scores)

        combined_text = " ".join(
            item.strip()
            for item in items
            if str(item).strip()
        )

        combined_similarity = 0.0

        if combined_text:
            combined_similarity = calculate_similarity(
                generate_embedding(combined_text),
                context_embedding,
            )

        return max(average_top_scores, combined_similarity)

    candidate_semantic_text = " ".join(
        part
        for part in [
            " ".join(candidate_skills),
            " ".join(candidate_projects),
            " ".join(candidate_education),
            " ".join(candidate_domains),
        ]
        if part
    ).strip()

    if not candidate_semantic_text:
        candidate_semantic_text = candidate_text

    job_semantic_text = " ".join(
        part
        for part in [
            job_text,
            " ".join(required_skills),
            " ".join(preferred_education),
            " ".join(preferred_domains),
        ]
        if part
    ).strip()

    candidate_embedding = candidate_embedding or (
        generate_embedding(candidate_semantic_text)
        if candidate_semantic_text
        else None
    )

    job_embedding = job_embedding or (
        generate_embedding(job_semantic_text)
        if job_semantic_text
        else None
    )

    semantic_similarity = 0.0

    if candidate_embedding and job_embedding:
        semantic_similarity = calculate_similarity(
            candidate_embedding,
            job_embedding,
        )

    # Skill Match
    semantic_result = semantic_match(
        candidate_skills,
        required_skills,
    )

    skill_context_score = _context_similarity_score(
        candidate_skills,
        job_semantic_text,
        top_n=3,
    )

    list_skill_score = (
        len(semantic_result["matches"])
        /
        max(
            len(required_skills),
            1
        )
    )

    skills_score = max(
        list_skill_score,
        skill_context_score,
    )

    # Experience Match
    experience_score = (
        calculate_experience_match(
            candidate_experience,
            minimum_experience,
        )
    )

    # Education Match
    education_score = (
        calculate_education_match(
            candidate_education,
            preferred_education,
        )
    )

    # Domain Match
    domain_score = (
        calculate_domain_similarity(
            candidate_domains,
            preferred_domains,
        )
    )

    # Project Relevance
    project_score = (
        calculate_project_relevance(
            candidate_projects,
            job_semantic_text or job_text or " ".join(required_skills),
        )
    )

    # Final Weighted Score
    heuristic_score = (
        calculate_final_score(

            skills_score,

            experience_score,

            project_score,

            education_score,

            domain_score
        )
    )

    semantic_score = round(
        semantic_similarity * 100,
        2
    )

    signal_scores = sorted(
        [
            semantic_score,
            skills_score * 100,
            project_score * 100,
            education_score * 100,
            experience_score * 100,
            domain_score * 100,
        ],
        reverse=True,
    )

    confidence_score = (
        (signal_scores[0] * 0.55)
        + (signal_scores[1] * 0.30)
        + (signal_scores[2] * 0.15)
    )

    if education_score >= 0.90 and project_score >= 0.40:
        confidence_score += 5.0

    if skills_score >= 0.30 and semantic_score >= 35.0:
        confidence_score += 4.0

    if domain_score >= 0.50:
        confidence_score += 3.0

    if experience_score >= 0.50:
        confidence_score += 2.0

    confidence_score = min(confidence_score, 100.0)

    final_score = (
        (heuristic_score * 0.45)
        + (confidence_score * 0.55)
    )

    final_score = round(
        min(
            100.0,
            final_score,
        ),
        2
    )

    return {

        "final_score":
            final_score,

        "finalScore":
            final_score,

        "match_score":
            final_score,

        "semantic_similarity":
            round(semantic_similarity, 4),

        "semantic_score":
            semantic_score,

        "skills_score":
            round(skills_score * 100, 2),

        "skill_context_score":
            round(skill_context_score * 100, 2),

        "list_skill_score":
            round(list_skill_score * 100, 2),

        "experience_score":
            round(experience_score * 100, 2),

        "project_score":
            round(project_score * 100, 2),

        "education_score":
            round(education_score * 100, 2),

        "domain_score":
            round(domain_score * 100, 2),

        "matched_skills":
            semantic_result["matches"],

        "missing_skills":
            semantic_result["missing_skills"],
    }