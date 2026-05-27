# ==========================================
# IMPORT
# ==========================================
import re

from app.utils.education_database import EDUCATION_KEYWORDS

from app.services.extraction.section_extractor import (
    extract_section_text,
)

EDUCATION_SECTION_HEADINGS = [
    "education",
    "academic background",
    "academic qualification",
    "educational qualification",
    "qualifications",
    "academics",
    "certifications",
]

IGNORED_EDUCATION_KEYWORDS = {
    "college",
    "ca",
    "me",
    "ms",
    "llm",
    "architecture",
    "ba",
    "be",
    "certification",
    "gpa",
    "cgpa",
    "percentage",
    "research",
    "cat",
}


def _education_pattern(keyword: str):

    escaped = re.escape(keyword.lower().strip())

    if len(keyword.strip()) == 1:
        return None

    escaped = escaped.replace(r"\ ", r"\s+")

    if keyword.lower().strip() in {"b.e", "b.e.", "m.e", "m.e.", "b.tech", "m.tech", "b.sc", "m.sc", "b.a", "m.a"}:
        return rf"(?<!\w){escaped}(?!\w)"

    return rf"(?<!\w){escaped}(?!\w)"


# ==========================================
# EXTRACT EDUCATION FUNCTION
# ==========================================

def extract_education(text: str):

    section_text = extract_section_text(
        text,
        EDUCATION_SECTION_HEADINGS,
    )

    normalized_text = " ".join(
        section_text.lower().split()
    )

    found = []

    seen = set()

    def normalized_key(value: str):

        return re.sub(
            r"[^a-z0-9]",
            "",
            value.lower().strip(),
        )

    ordered_keywords = sorted(
        EDUCATION_KEYWORDS,
        key=lambda value: len(value),
        reverse=True,
    )

    for edu in ordered_keywords:

        normalized_edu = edu.lower().strip()

        if normalized_edu in IGNORED_EDUCATION_KEYWORDS:
            continue

        pattern = _education_pattern(edu)

        if not pattern:
            continue

        if re.search(pattern, normalized_text):

            key = normalized_key(edu)

            if key in seen:
                continue

            found.append(edu)
            seen.add(key)

    return found