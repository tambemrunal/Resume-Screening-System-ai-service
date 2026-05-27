from fastapi import APIRouter
from pydantic import BaseModel

from app.services.semantic.advanced_match_engine import (
    advanced_match_engine
)

router = APIRouter()

class AdvancedMatchRequest(
    BaseModel
):

    candidate_data: dict

    job_data: dict

    candidate_text: str | None = None

    job_text: str | None = None

    candidate_embedding: list[float] | None = None

    job_embedding: list[float] | None = None

@router.post("/advanced-match")
def advanced_match(
    data: AdvancedMatchRequest
):

    result = advanced_match_engine(

        data.candidate_data,

        data.job_data,

        candidate_text=data.candidate_text,

        job_text=data.job_text,

        candidate_embedding=data.candidate_embedding,

        job_embedding=data.job_embedding,
    )

    return result