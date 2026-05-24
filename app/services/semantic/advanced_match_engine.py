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

def advanced_match_engine(

    candidate_data,

    job_data
):

    # Skill Match
    semantic_result = semantic_match(
        candidate_data["skills"],
        job_data["required_skills"]
    )

    skills_score = (
        len(semantic_result["matches"])
        /
        max(
            len(job_data["required_skills"]),
            1
        )
    )

    # Experience Match
    experience_score = (
        calculate_experience_match(
            candidate_data["experience"],
            job_data["minimum_experience"]
        )
    )

    # Education Match
    education_score = (
        calculate_education_match(
            candidate_data["education"],
            job_data["preferred_education"]
        )
    )

    # Domain Match
    domain_score = (
        calculate_domain_similarity(
            candidate_data["domains"],
            job_data["preferred_domains"]
        )
    )

    # Project Relevance
    project_score = (
        calculate_project_relevance(
            candidate_data["projects"],
            " ".join(
                job_data["required_skills"]
            )
        )
    )

    # Final Weighted Score
    final_score = (
        calculate_final_score(

            skills_score,

            experience_score,

            project_score,

            education_score,

            domain_score
        )
    )

    return {

        "final_score":
            final_score,

        "skills_score":
            round(skills_score * 100, 2),

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