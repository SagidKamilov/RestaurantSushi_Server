import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.schemas.admins import AdminSchema
from src.schemas.users import UserSchema


class Users(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[str]
    count_ask_address: Mapped[int]
    telegram_id: Mapped[int]
    date_registration: Mapped[datetime.date]
    time_registration: Mapped[datetime.time]
    date_update: Mapped[datetime.date]
    time_update: Mapped[datetime.date]
    ban: Mapped[bool]

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            name=self.name,
            address=self.address,
            date_registration=self.date_registration,
            time_registration=self.time_registration,
        )

