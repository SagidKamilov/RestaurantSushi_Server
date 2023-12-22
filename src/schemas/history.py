from typing import Any, Dict

from pydantic import BaseModel


class Order(BaseModel):
    order_id: dict


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
    user_id: int


class HistoryDeleteSchema(BaseModel):
    id: int
