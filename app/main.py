from fastapi import FastAPI

from app.api.parse import router as parse_router
from app.api.match import router as match_router

app = FastAPI()

app.include_router(parse_router)
app.include_router(match_router)

@app.get("/")
def home():
    return {
        "message": "AI Resume Service Running"
    }