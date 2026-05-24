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

@router.post("/advanced-match")
def advanced_match(
    data: AdvancedMatchRequest
):

    result = advanced_match_engine(

        data.candidate_data,

        data.job_data
    )

    return result