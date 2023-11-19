from fastapi import APIRouter, Depends

from kitchengpt.dependencies import get_db_connection

router = APIRouter()


@router.get("/")
async def get_inventory(conn=Depends(get_db_connection)):
    """Get all items inside the fridge"""
    rows = await conn.fetch("SELECT * FROM mytable")
    return rows
