from typing import Any

from pydantic import BaseModel, Json


class HistorySchema(BaseModel):
    id: int
    order: Json[Any]
    user_id: int

    class Config:
        from_attributes = True


class HistoryAddSchema(BaseModel):
    order: Json[Any]
    user_id: int
