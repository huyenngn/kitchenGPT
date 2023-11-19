from fastapi import APIRouter

from .v1 import fridge, oven

api_router = APIRouter()
api_router.include_router(fridge.router, prefix="/fridge", tags=["Fridge"])
api_router.include_router(oven.router, prefix="/oven", tags=["Oven"])
