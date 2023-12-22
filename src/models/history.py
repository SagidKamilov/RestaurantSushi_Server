from typing import Dict, Any

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import JSON

from src.models.base import Base
from src.schemas.history import HistorySchema


class History(Base):
    __tablename__ = "History"

    id: Mapped[int] = mapped_column(name="history_id", primary_key=True, autoincrement=True)
    order: Mapped[Dict[int, Any]] = mapped_column(type_=JSON)
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.user_id"))

    def to_read_model(self) -> HistorySchema:
        return HistorySchema(
            history_id=self.id,
            order=self.order,
            user_id=self.user_id
        )
