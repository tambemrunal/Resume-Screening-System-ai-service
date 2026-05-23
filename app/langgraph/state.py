from typing import TypedDict

class ResumeState(TypedDict):

    candidate_skills: list

    required_skills: list

    normalized_skills: list

    expanded_skills: list

    matched_skills: list

    missing_skills: list

    match_score: float

    explanation: str