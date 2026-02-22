from fastapi import FastAPI
from app.routers import auth, books, reviews, intel

app = FastAPI(title="LuminaLib")

app.include_router(auth.router)
app.include_router(books.router)
app.include_router(reviews.router)
app.include_router(intel.router)

