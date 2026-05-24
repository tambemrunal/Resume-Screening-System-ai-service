import re

from app.services.extraction.skill_extractor import (
    extract_skills
)

from app.services.extraction.education_extractor import (
    extract_education
)

def extract_experience_from_jd(text):

    patterns = [
        r'(\d+)\+?\s+years',
        r'(\d+)\+?\s+yrs',
    ]

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text.lower()
        )

        if matches:
            return int(matches[0])

    return 0

def extract_domains(text):

    domains = []

    DOMAIN_KEYWORDS = [
        "healthcare",
        "fintech",
        "ecommerce",
        "education",
        "agritech",
        "ai",
    ]

    text = text.lower()

    for domain in DOMAIN_KEYWORDS:

        if domain in text:
            domains.append(domain)

    return domains

def parse_jd(text):

    parsed_data = {

        "required_skills":
            extract_skills(text),

        "minimum_experience":
            extract_experience_from_jd(text),

        "preferred_education":
            extract_education(text),

        "preferred_domains":
            extract_domains(text),

        "responsibilities": [],
    }

    return parsed_data