from fastapi import APIRouter

from src.services.users import UserService
from src.schemas.users import UserAddSchema, UserGetSchema, UserDeleteSchema, UserUpdateSchema

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.get("")
async def user_get():
    pass


@router.post("")
async def user_add():
    pass


@router.delete("")
async def user_delete():
    pass


@router.put("")
async def user_update():
    pass

