from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import JSON

from src.models.base import Base
from src.schemas.history import HistorySchema

class History(Base):
    __tablename__ = "History"

    history_id: Mapped[int] = mapped_column(primary_key=True)
    order: Mapped[JSON]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))

    def to_read_model(self) -> HistorySchema:
        return HistorySchema(
            history_id=self.history_id,
            order=self.order,
            user_id=self.user_id
        )
