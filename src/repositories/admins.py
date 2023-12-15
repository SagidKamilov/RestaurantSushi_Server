from src.models.admins import Admins
from src.repositories.sql_repository import SQLOrmRepository


class AdminsRepository(SQLOrmRepository):
    model = Admins
