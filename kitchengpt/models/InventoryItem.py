from pydantic import BaseModel


class InventoryItem(BaseModel):
    name: str
    amount: int
