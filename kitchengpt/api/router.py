"""API layer for kitchenGPT."""

from fastapi import APIRouter

from .endpoints import fridge, oven

api_router = APIRouter()


@api_router.get("/", tags=["Chat"])
async def root(text: str):
    """Chat endpoint."""
    return {"message": text}


api_router.include_router(fridge.router, prefix="/fridge", tags=["Fridge"])
api_router.include_router(oven.router, prefix="/oven", tags=["Oven"])
