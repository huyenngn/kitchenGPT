"""API layer for kitchenGPT."""

from fastapi import APIRouter

from .v1 import fridge, oven

api_router = APIRouter(prefix="/v1", tags=["v1"])
api_router.include_router(fridge.router, prefix="/fridge", tags=["Fridge"])
api_router.include_router(oven.router, prefix="/oven", tags=["Oven"])
