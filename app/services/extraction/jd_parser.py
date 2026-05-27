import re

from app.services.extraction.skill_extractor import (
    extract_skills
)

from app.services.extraction.education_extractor import (
    extract_education
)

from app.utils.domain_database import (
    DOMAIN_KEYWORDS
)


# ==========================================
# EXPERIENCE EXTRACTION
# ==========================================

def extract_experience_from_jd(text):

    patterns = [

        # 3 years
        r'(\d+)\+?\s+years',

        # 3 yrs
        r'(\d+)\+?\s+yrs',

        # experience of 3 years
        r'experience\s+of\s+(\d+)\+?\s+years',

        # minimum 2 years
        r'minimum\s+(\d+)\+?\s+years',

        # at least 5 years
        r'at\s+least\s+(\d+)\+?\s+years',

        # 1-3 years
        r'(\d+)\s*-\s*\d+\s+years',

        # 2 to 5 years
        r'(\d+)\s+to\s+\d+\s+years',
    ]

    text = text.lower()

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text
        )

        if matches:

            try:
                return int(matches[0])

            except:
                continue

    return 0


# ==========================================
# DOMAIN EXTRACTION
# ==========================================

def extract_domains(text):

    text = text.lower()

    domains = []

    # ==========================================
    # IMPORTANT:
    # For JD:
    # Extract only educational / domain fields
    # NOT technologies from projects/tasks.
    #
    # Example:
    # "Bachelor in Computer Science"
    # should detect:
    # -> computer science
    #
    # But:
    # "Built AI healthcare platform"
    # should NOT dominate domain extraction.
    # ==========================================

    relevant_sections = []

    # ==========================================
    # EDUCATION SECTION
    # ==========================================

    education_match = re.search(
        r"(education|qualification|requirements|preferred qualifications)(.*?)(responsibilities|skills|experience|benefits|$)",
        text,
        re.DOTALL,
    )

    if education_match:

        relevant_sections.append(
            education_match.group(0)
        )

    # ==========================================
    # PROFILE / SUMMARY SECTION
    # ==========================================

    summary_match = re.search(
        r"(summary|profile|about|candidate profile)(.*?)(education|skills|experience|responsibilities|$)",
        text,
        re.DOTALL,
    )

    if summary_match:

        relevant_sections.append(
            summary_match.group(0)
        )

    # ==========================================
    # FALLBACK
    # ==========================================

    if not relevant_sections:

        relevant_sections.append(text)

    final_text = " ".join(
        relevant_sections
    )

    # ==========================================
    # DOMAIN MATCHING
    # ==========================================

    for domain in DOMAIN_KEYWORDS:

        if domain.lower() in final_text:

            domains.append(domain)

    return list(set(domains))


# ==========================================
# JD PARSER
# ==========================================

def parse_jd(text):

    parsed_data = {

        # ======================================
        # Skills
        # ======================================

        "required_skills":
            extract_skills(text),

        # ======================================
        # Experience
        # ======================================

        "minimum_experience":
            extract_experience_from_jd(
                text
            ),

        # ======================================
        # Education
        # ======================================

        "preferred_education":
            extract_education(text),

        # ======================================
        # Domains
        # ======================================

        "preferred_domains":
            extract_domains(text),

        # ======================================
        # Future Extension
        # ======================================

        "responsibilities": [],
    }

    return parsed_data