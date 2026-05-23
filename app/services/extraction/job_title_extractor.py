JOB_TITLES = [
    "frontend developer",
    "backend developer",
    "full stack developer",
    "software engineer",
    "web developer",
    "ai engineer",
]

def extract_job_titles(text: str):

    text = text.lower()

    titles = []

    for job in JOB_TITLES:

        if job in text:
            titles.append(job)

    return titles