"""Functions for dependency injection."""
import asyncpg

from .config import settings


async def get_db_connection():
    """Get a database connection."""
    conn = await asyncpg.connect(settings.DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()
