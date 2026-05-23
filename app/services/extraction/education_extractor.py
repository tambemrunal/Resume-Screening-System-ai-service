def extract_education(text: str):

    text = text.lower()

    education_keywords = [
        "bachelor",
        "master",
        "b.e",
        "b.tech",
        "m.tech",
        "phd"
    ]

    found = []

    for edu in education_keywords:

        if edu in text:
            found.append(edu)

    return found