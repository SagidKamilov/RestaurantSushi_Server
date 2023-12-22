from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import Any
#from sqlalchemy.types import JSON
from pydantic import Json

from src.models.base import Base
from src.schemas.history import HistorySchema


class History(Base):
    __tablename__ = "History"

    id: Mapped[int] = mapped_column(name="history_id", primary_key=True, autoincrement=True)
    order: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.user_id"))

    def to_read_model(self) -> HistorySchema:
        return HistorySchema(
            history_id=self.id,
            order=self.order,
            user_id=self.user_id
        )
