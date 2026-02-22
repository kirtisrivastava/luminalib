from fastapi import APIRouter
from app.services.llm import LLMService
import asyncio

router = APIRouter(prefix="/books", tags=["Reviews"])
llm = LLMService()

@router.post("/{id}/reviews")
async def submit_review(id: int, review: str):
    asyncio.create_task(llm.analyze_reviews([review]))
    return {"message": f"Review submitted for book {id}"}

