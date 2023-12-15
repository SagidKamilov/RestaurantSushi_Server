from src.models.users import Users
from src.repositories.sql_repository import SQLOrmRepository


class UserRepository(SQLOrmRepository):
    model = Users
