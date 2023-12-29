from src.schemas.history import HistoryAddSchema, HistoryDeleteSchema
from src.uow.uow_manager import IUnitOfWork


class HistoryService:
    @staticmethod
    async def add_history(history: HistoryAddSchema, uow: IUnitOfWork):
        history_dict: dict = history.model_dump()
        async with uow:
            history_dict = await uow.history.add_one(data=history_dict)
            await uow.commit()
            return history_dict

    @staticmethod
    async def get_history(history_id: int, uow: IUnitOfWork):
        history_dict: dict = {"id": history_id}
        async with uow:
            history_id = await uow.history.find_one(data=history_dict)
            return history_id

    @staticmethod
    async def delete_history(history: HistoryDeleteSchema, uow: IUnitOfWork):
        history_dict: dict = history.model_dump()
        async with uow:
            history_del = await uow.history.delete_one(data=history_dict)
            return history_del
