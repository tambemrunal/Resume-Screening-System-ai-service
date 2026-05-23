SKILL_ALIASES = {

    # React
    "reactjs": "react",
    "react.js": "react",

    # Node
    "node": "node.js",
    "nodejs": "node.js",

    # JavaScript
    "js": "javascript",

    # Mongo
    "mongo": "mongodb",

    # AI
    "llm": "large language models",

    # CSS
    "tailwind": "tailwind css",
}

def normalize_skill(skill: str):

    skill = skill.lower().strip()

    return SKILL_ALIASES.get(skill, skill)

def normalize_skills(skills: list):

    normalized = []

    for skill in skills:
        normalized.append(normalize_skill(skill))

    return list(set(normalized))