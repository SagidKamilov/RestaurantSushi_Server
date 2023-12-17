import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, func, Time

from src.models.base import Base
from src.schemas.users import UserSchema


class Users(Base):
    __tablename__ = "Users"

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int]
    name: Mapped[str] = mapped_column(String(250))
    address: Mapped[str] = mapped_column(String(250))
    count_ask_address: Mapped[int]
    date_registration: Mapped[datetime.date] = mapped_column(Date())
    time_registration: Mapped[datetime.time] = mapped_column(Time())
    date_update: Mapped[datetime.date] = mapped_column(Date())
    time_update: Mapped[datetime.time] = mapped_column(Time())
    ban: Mapped[bool]

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.user_id,
            telegram_id=self.telegram_id,
            name=self.name,
            address=self.address,
            date_registration=self.date_registration,
            time_registration=self.time_registration,
            date_update=self.date_update,
            time_update=self.time_update,
            count_ask_address=self.count_ask_address,
            ban=self.ban,
        )

