from fastapi import APIRouter, UploadFile
from app.services.storage import LocalStorage
from app.services.llm import LLMService
import asyncio

router = APIRouter(prefix="/books", tags=["Books"])
storage = LocalStorage()
llm = LLMService()

@router.post("/")
async def upload_book(file: UploadFile):
    path = await storage.save_file(file, file.filename)
    asyncio.create_task(llm.summarize_book(await file.read()))
    return {"message": "Book uploaded", "path": path}

@router.get("/")
async def list_books():
    return {"books": ["demo_book1.pdf", "demo_book2.pdf"]}

@router.post("/{id}/borrow")
async def borrow_book(id: int):
    return {"message": f"Book {id} borrowed"}

@router.post("/{id}/return")
async def return_book(id: int):
    return {"message": f"Book {id} returned"}

