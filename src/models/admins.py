from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.schemas.admins import AdminSchema


class Admins(Base):
    __tablename__ = "Admins"

    admin_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    level: Mapped[int]

    def to_read_model(self) -> AdminSchema:
        return AdminSchema(
            id=self.admin_id,
            level=self.level
        )