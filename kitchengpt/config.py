"""Project settings."""
import os

import dotenv

dotenv.load_dotenv(".env")


class Settings:
    """Project settings."""

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://kitchengpt_user:kitchengpt_password@db/kitchengpt_db",
    )
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


settings = Settings()
