import datetime

from pydantic import BaseModel
from sqlalchemy import JSON


class Basket(BaseModel):
    user_id: int
    order_id: int
    date: datetime.date
    time: datetime.time
    order: JSON
