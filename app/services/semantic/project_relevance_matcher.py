from app.services.semantic.embedding_service import (
    generate_embedding
)

from app.services.semantic.cosine_similarity import (
    calculate_similarity
)

def calculate_project_relevance(
    resume_projects,
    jd_text
):

    if not resume_projects:
        return 0

    jd_embedding =generate_embedding(jd_text)

    scores = []

    for project in resume_projects:

        project_embedding =generate_embedding(project)

        similarity =calculate_similarity(
                project_embedding,
                jd_embedding
            )

        scores.append(similarity)

    if not scores:
        return 0

    return max(scores)