import re

from app.utils.skills_database import SKILLS

from app.services.extraction.section_extractor import (
    extract_section_text,
)

from app.services.semantic.skill_normalizer import (
    normalize_skill,
)

SKILL_SECTION_HEADINGS = [
    "skills",
    "technical skills",
    "tech stack",
    "technical expertise",
    "core skills",
    "key skills",
    "skills & technologies",
]

IGNORED_SKILLS = {
    "c",
    "r",
    "http",
    "https",
}


def _skill_pattern(skill: str):

    escaped = re.escape(skill.lower().strip())

    if len(skill.strip()) == 1:
        return None

    escaped = escaped.replace(r"\ ", r"\s+")

    return rf"(?<!\w){escaped}(?!\w)"

def extract_skills(text: str):

    section_text = extract_section_text(
        text,
        SKILL_SECTION_HEADINGS,
    )

    normalized_text = " ".join(
        section_text.lower().split()
    )

    found_skills = []

    seen = set()

    ordered_skills = sorted(
        SKILLS,
        key=lambda value: len(value),
        reverse=True,
    )

    for skill in ordered_skills:

        normalized_skill = skill.lower().strip()

        if normalized_skill in IGNORED_SKILLS:
            continue

        pattern = _skill_pattern(skill)

        if not pattern:
            continue

        if re.search(pattern, normalized_text):

            canonical_skill = normalize_skill(normalized_skill)

            if canonical_skill in seen:
                continue

            found_skills.append(canonical_skill)
            seen.add(canonical_skill)

    return found_skills