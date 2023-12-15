from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.schemas.menu import MenuSchema

class Menu(Base):
    __tablename__ = "Menu"

    menu_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    weight: Mapped[int]
    composition: Mapped[str]
    cost: Mapped[int]
    stop_list: Mapped[bool]

    def to_read_model(self) -> MenuSchema:
        return MenuSchema(
            menu_id=self.menu_id,
            name=self.name,
            weight=self.weight,
            composition=self.composition,
            cost=self.cost,
            stop_list=self.stop_list
        )
