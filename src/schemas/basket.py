from typing import Optional

from pydantic import BaseModel

from src.schemas.history import Order


class BasketSchema(BaseModel):
    available: bool
    order: Order
    user_id: int

    class Config:
        from_attributes = True


class BasketAddSchema(BaseModel):
    available: bool
    order: Order
    user_id: int


class BasketUpdateSchema(BaseModel):
    id: str
    available: Optional[bool]


class BasketDeleteSchema(BaseModel):
    user_id: int
