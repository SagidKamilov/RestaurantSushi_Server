from fastapi import APIRouter

from src.services.history import HistoryAddSchema
from src.services.history import HistoryGetSchema
from src.schemas.history import HistoryDeleteSchema
from src.services.history import HistoryService
from src.api.dependencies import UOWDepends

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.post("")
async def add_history(history: HistoryAddSchema, uow: UOWDepends):
    history_id = await HistoryService().add_history(history, uow)
    return history_id


@router.delete("")
async def del_history(history: HistoryDeleteSchema, uow: UOWDepends):
    history_data = await HistoryService().delete_history(history, uow)
    return {"deleted_rows": history_data}


@router.get("{history_id}")
async def get_history(history_id: int, uow: UOWDepends):
    history_data = await HistoryService().get_history(history_id, uow)
    return history_data
