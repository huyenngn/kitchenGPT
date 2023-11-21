"""Oven API endpoints."""

from fastapi import APIRouter, Depends

from kitchengpt.dependencies import get_db_connection

router = APIRouter()


@router.get("/")
async def get_oven_settings(conn=Depends(get_db_connection)):
    """Get current oven settings."""
    rows = await conn.fetch("SELECT * FROM mytable")
    return rows
