from fastapi import APIRouter

from src.schemas.users import UserAddSchema, UserGetSchema, UserUpdateSchema, UserDeleteSchema
from src.services.users import UserService

from src.api.dependencies import UOWDepends

router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@router.post("")
async def add_user(uow: UOWDepends, user: UserAddSchema):
    user_id = UserService().add_user(uow=uow, user=user)
    return user_id


@router.get("")
async def get_user(uow: UOWDepends, user: UserGetSchema):
    user = UserService().get_user(uow=uow, user=user)
    return user


@router.get("")
async def get_users(uow: UOWDepends):
    users = UserService().get_users(uow=uow)
    return users


@router.put("")
async def edit_user(uow: UOWDepends, user: UserUpdateSchema):
    user = UserService().edit_user(uow=uow, user=user)
    return user


@router.delete("")
async def delete_user(uow: UOWDepends, user: UserDeleteSchema):
    edited_rowcount = UserService().delete_user(uow=uow, user=user)
    return edited_rowcount
