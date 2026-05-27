import re


DEFAULT_SECTION_HEADINGS = [
    "experience",
    "work experience",
    "employment history",
    "internship",
    "internships",
    "skills",
    "technical skills",
    "tech stack",
    "education",
    "academic background",
    "qualifications",
    "projects",
    "project experience",
    "personal projects",
    "summary",
    "profile",
    "objective",
    "certifications",
]


def _normalize_heading(line: str):

    return re.sub(
        r"[^a-z0-9+#.&\-/ ]",
        " ",
        line.lower(),
    ).strip()


def _is_heading(line: str, headings: list):

    cleaned = _normalize_heading(line)

    if not cleaned or len(cleaned) > 80:
        return False

    for heading in headings:

        normalized_heading = _normalize_heading(heading)

        if (
            cleaned == normalized_heading
            or cleaned.startswith(normalized_heading + " ")
            or cleaned.startswith(normalized_heading + ":")
            or cleaned.startswith(normalized_heading + "-")
            or normalized_heading in cleaned.split(" ")[:3]
        ):
            return True

    return False


def extract_section_text(
    text: str,
    section_headings: list,
):

    lines = [line.strip() for line in text.splitlines()]

    start_index = None

    for index, line in enumerate(lines):

        if _is_heading(line, section_headings):
            start_index = index + 1
            break

    if start_index is None:
        return text

    collected = []

    for line in lines[start_index:]:

        if _is_heading(line, DEFAULT_SECTION_HEADINGS):
            break

        if line:
            collected.append(line)

    section_text = "\n".join(collected).strip()

    return section_text or text