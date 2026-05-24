from fastapi import APIRouter
from pydantic import BaseModel

from app.services.extraction.jd_parser import (
    parse_jd
)

router = APIRouter()

class JDRequest(BaseModel):

    jd_text: str

@router.post("/parse-jd")
def parse_job_description(
    data: JDRequest
):

    parsed_data = parse_jd(
        data.jd_text
    )

    return parsed_data