def calculate_final_score(

    skills_score,

    experience_score,

    project_score,

    education_score,

    domain_score
):

    final_score = (

        (skills_score * 0.35)

        +

        (experience_score * 0.20)

        +

        (project_score * 0.25)

        +

        (education_score * 0.10)

        +

        (domain_score * 0.10)
    )

    return round(
        final_score * 100,
        2
    )