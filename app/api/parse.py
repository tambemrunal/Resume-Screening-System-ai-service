from fastapi import APIRouter
from pydantic import BaseModel

from app.services.extraction.email_extractor import extract_email
from app.services.extraction.phone_extractor import extract_phone
from app.services.extraction.skill_extractor import extract_skills
from app.services.extraction.experience_extractor import extract_experience
from app.services.extraction.education_extractor import extract_education
from app.services.extraction.job_title_extractor import extract_job_titles
from app.services.extraction.name_extractor import extract_name

router = APIRouter()

class ResumeRequest(BaseModel):
    resume_text: str

@router.post("/parse-resume")
def parse_resume(data: ResumeRequest):

    text = data.resume_text

    parsed_data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "experience": extract_experience(text),
        "education": extract_education(text),
        "job_titles": extract_job_titles(text),
    }

    return parsed_data