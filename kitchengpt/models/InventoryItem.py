"""Pydantic Models for KitchenGPT."""

from pydantic import BaseModel


class InventoryItem(BaseModel):
    """Represents an item in the inventory."""

    name: str
    amount: int
