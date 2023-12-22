from typing import Any, Dict, List

from pydantic import BaseModel


class Order(BaseModel):
    list_dishes: List[int]
    comment: str
    cost: int
    address: str


class HistorySchema(BaseModel):
    id: int
    order: Order
    user_id: int

    class Config:
        from_attributes = True


class HistoryAddSchema(BaseModel):
    order: Order
    user_id: int


class HistoryGetSchema(BaseModel):
    id: int


class HistoryDeleteSchema(BaseModel):
    id: int
