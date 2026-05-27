from app.services.semantic.embedding_service import (
    generate_embedding
)

from app.services.semantic.cosine_similarity import (
    calculate_similarity
)


PROJECT_ALIGNMENT_TERMS = {
    "web",
    "application",
    "applications",
    "app",
    "platform",
    "system",
    "dashboard",
    "frontend",
    "backend",
    "full stack",
    "software",
    "api",
    "fastapi",
    "flask",
    "react",
    "mern",
    "responsive",
    "deployment",
    "performance",
    "authentication",
    "real-time",
    "data",
}


def _split_context(text: str):

    chunks = []

    for line in text.replace("•", "\n").splitlines():

        parts = [
            part.strip()
            for part in __import__("re").split(
                r"[.;]",
                line,
            )
        ]

        for part in parts:

            clean_part = part.strip()

            if len(clean_part) >= 12:
                chunks.append(clean_part)

    return chunks or [text]


def _alignment_score(text_a: str, text_b: str):

    a = text_a.lower()

    b = text_b.lower()

    shared = 0

    relevant = 0

    for term in PROJECT_ALIGNMENT_TERMS:

        if term in b:
            relevant += 1

            if term in a:
                shared += 1

    if relevant == 0:
        return 0.0

    return shared / relevant

def calculate_project_relevance(
    resume_projects,
    jd_text
):

    if not resume_projects or not jd_text:
        return 0

    jd_chunks = _split_context(jd_text)

    jd_embeddings = [
        generate_embedding(chunk)
        for chunk in jd_chunks
    ]

    jd_embedding = generate_embedding(jd_text)

    scores = []

    for project in resume_projects:

        project_embedding =generate_embedding(project)

        chunk_scores = []

        for chunk_embedding in jd_embeddings:

            chunk_scores.append(
                calculate_similarity(
                    project_embedding,
                    chunk_embedding,
                )
            )

        chunk_similarity = max(chunk_scores) if chunk_scores else 0

        similarity =calculate_similarity(
                project_embedding,
                jd_embedding
            )

        similarity = max(similarity, chunk_similarity)

        scores.append(similarity)

    if not scores:
        return 0

    scores.sort(reverse=True)

    top_scores = scores[: min(2, len(scores))]

    average_top_scores = sum(top_scores) / len(top_scores)

    combined_projects_text = " ".join(
        project.strip()
        for project in resume_projects
        if project and project.strip()
    )

    combined_similarity = 0.0

    if combined_projects_text:
        combined_embedding = generate_embedding(combined_projects_text)

        combined_similarity = calculate_similarity(
            combined_embedding,
            jd_embedding,
        )

        chunk_scores = [
            calculate_similarity(
                combined_embedding,
                chunk_embedding,
            )
            for chunk_embedding in jd_embeddings
        ]

        if chunk_scores:
            combined_similarity = max(
                combined_similarity,
                max(chunk_scores),
            )

    alignment_bonus = _alignment_score(
        combined_projects_text or " ".join(resume_projects),
        jd_text,
    )

    project_score = max(
        average_top_scores,
        combined_similarity,
        alignment_bonus,
    )

    if len(resume_projects) >= 2:
        project_score = min(
            1.0,
            project_score + 0.05,
        )

    return project_score