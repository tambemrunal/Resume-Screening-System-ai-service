from fastapi import APIRouter
from pydantic import BaseModel

from app.langgraph.workflow import app_workflow

router = APIRouter()

class MatchRequest(BaseModel):

    candidate_skills: list

    required_skills: list

@router.post("/match-resume")
def match_resume(data: MatchRequest):

    result = app_workflow.invoke({

        "candidate_skills":
            data.candidate_skills,

        "required_skills":
            data.required_skills
    })

    return result