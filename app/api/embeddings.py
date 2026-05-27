from fastapi import APIRouter
from pydantic import BaseModel

from app.services.semantic.embedding_service import (
    generate_embedding,
)

router = APIRouter()


class EmbeddingRequest(BaseModel):

    text: str


@router.post("/embeddings")
def create_embedding(data: EmbeddingRequest):

    return {
        "embedding": generate_embedding(data.text),
    }