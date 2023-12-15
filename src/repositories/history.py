from src.models.history import History
from src.repositories.sql_repository import SQLOrmRepository


class HistoryRepository(SQLOrmRepository):
    model = History
