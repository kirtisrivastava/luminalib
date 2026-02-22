from fastapi import APIRouter
from app.services.recommender import Recommender

router = APIRouter(tags=["Intel"])
recommender = Recommender()

@router.get("/books/{id}/analysis")
async def get_analysis(id: int):
    return {"analysis": f"Consensus sentiment for book {id}"}

@router.get("/recommendations")
async def get_recommendations(user_id: int):
    return {"recommendations": recommender.recommend(user_id, [1,2,3])}

