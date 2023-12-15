from src.models.menu import Menu
from src.repositories.sql_repository import SQLOrmRepository


class MenuRepository(SQLOrmRepository):
    model = Menu
