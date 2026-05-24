PROJECT_KEYWORDS = [
    "project",
    "developed",
    "built",
    "engineered",
    "implemented",
    "created",
]

def extract_projects(text: str):

    lines = text.split("\n")

    projects = []

    for line in lines:

        clean_line = line.strip()

        lower_line = clean_line.lower()

        for keyword in PROJECT_KEYWORDS:

            if keyword in lower_line:

                if len(clean_line) > 30:

                    projects.append(clean_line)

                    break

    return list(set(projects))