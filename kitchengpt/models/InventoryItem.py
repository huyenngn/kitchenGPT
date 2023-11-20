"""Pydantic Models for KitchenGPT."""

from datetime import datetime

from pydantic import BaseModel


class InventoryItem(BaseModel):
    """Represents an item in the inventory."""

    timestamp: datetime
    name: str
    amount: int
    location: str
    categories: list


class Recipe(BaseModel):
    """Represents a recipe."""

    name: str
    ingredients: list
    instructions: str
    categories: list
