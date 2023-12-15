from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.schemas.admins import AdminSchema


class Admins(Base):
    __tablename__ = "Admins"

    id: Mapped[int] = mapped_column(primary_key=True)

    def to_read_model(self) -> AdminSchema:
        return AdminSchema(
            id=self.id,
        )