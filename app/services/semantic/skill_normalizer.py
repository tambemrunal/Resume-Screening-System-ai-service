SKILL_ALIASES = {

    # React
    "reactjs": "react",
    "react.js": "react",
    "react js": "react",

    # Node
    "node": "node.js",
    "nodejs": "node.js",
    "node js": "node.js",

    # JavaScript
    "js": "javascript",

    # Mongo
    "mongo": "mongodb",

    # AI
    "llm": "large language models",

    # CSS
    "tailwind": "tailwind css",
    "tailwindcss": "tailwind css",
    "tailwind css": "tailwind css",
    "css3": "css",
    "html5": "html",

    # Backend
    "express": "express.js",
    "expressjs": "express.js",
    "express js": "express.js",
}

def normalize_skill(skill: str):

    skill = skill.lower().strip()

    return SKILL_ALIASES.get(skill, skill)

def normalize_skills(skills: list):

    normalized = []
    seen = set()

    for skill in skills:
        canonical = normalize_skill(skill)

        if canonical in seen:
            continue

        seen.add(canonical)
        normalized.append(canonical)

    return normalized