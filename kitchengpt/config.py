"""Project settings."""
import os


class Settings:
    """Project settings."""

    DATABASE_URL = os.getenv(
        "DATABASE_URL", "postgresql://user:password@localhost:5432/dbname"
    )


settings = Settings()
