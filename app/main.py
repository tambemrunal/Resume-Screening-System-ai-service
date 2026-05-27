import warnings

from langchain_core._api.deprecation import (
    LangChainPendingDeprecationWarning,
)

warnings.filterwarnings(
    "ignore",
    message=r".*allowed_objects.*",
    category=LangChainPendingDeprecationWarning,
    module=r"langgraph\.cache\.base",
)

from fastapi import FastAPI

from app.api.parse import (
    router as parse_router
)

from app.api.embeddings import (
    router as embeddings_router
)

from app.api.match import (
    router as match_router
)

from app.api.jd import (
    router as jd_router
)

from app.api.advanced_match import (
    router as advanced_match_router
)

app = FastAPI()

app.include_router(parse_router)

app.include_router(embeddings_router)

app.include_router(match_router)

app.include_router(jd_router)

app.include_router(
    advanced_match_router
)

@app.get("/")
def home():

    return {
        "message":
            "AI Resume Service Running"
    }