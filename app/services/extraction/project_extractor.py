from app.services.extraction.section_extractor import (
    extract_section_text,
)

PROJECT_KEYWORDS = [
    "project",
    "developed",
    "built",
    "engineered",
    "implemented",
    "created",
]

PROJECT_SECTION_HEADINGS = [
    "projects",
    "project experience",
    "personal projects",
    "academic projects",
]

def extract_projects(text: str):

    section_text = extract_section_text(
        text,
        PROJECT_SECTION_HEADINGS,
    )

    lines = section_text.split("\n")

    projects = []

    for line in lines:

        clean_line = line.strip()

        lower_line = clean_line.lower()

        for keyword in PROJECT_KEYWORDS:

            if keyword in lower_line:

                if len(clean_line) > 15:

                    projects.append(clean_line)

                    break

    return projects