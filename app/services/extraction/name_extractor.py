def extract_name(text: str):

    lines = text.split("\n")

    for line in lines[:10]:

        line = line.strip()

        if (
            len(line.split()) >= 2
            and len(line.split()) <= 4
            and line.isupper()
        ):
            return line.title()

    return ""