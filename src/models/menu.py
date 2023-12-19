from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.models.base import Base
from src.schemas.menu import MenuSchema


class Menu(Base):
    __tablename__ = "Menu"

    id: Mapped[int] = mapped_column(name="menu_id", primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(250))
    weight: Mapped[int]
    composition: Mapped[str] = mapped_column(String(300))
    cost: Mapped[int]
    stop_list: Mapped[bool]

    def to_read_model(self) -> MenuSchema:
        return MenuSchema(
            menu_id=self.id,
            name=self.name,
            weight=self.weight,
            composition=self.composition,
            cost=self.cost,
            stop_list=self.stop_list
        )
