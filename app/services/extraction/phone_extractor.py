import re

def extract_phone(text: str):

    pattern = r"(\+91[\-\s]?)?[6-9]\d{9}"

    matches = re.findall(pattern, text)

    if matches:
        return matches[0]

    return None