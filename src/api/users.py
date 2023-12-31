from fastapi import APIRouter

from src.services.users import UserService
from src.schemas.users import UserAddSchema, UserUpdateSchema, UserDeleteSchema
from src.api.dependencies import UOWDepends


router = APIRouter(
    tags=[
        "User"
    ],
)


@router.post("/user")
async def add_user(user: UserAddSchema, uow: UOWDepends):
    user_id = await UserService().add_user(uow=uow, user=user)
    return user_id


@router.get("/user/{user_id}")
async def get_user(user_id: int, uow: UOWDepends):
    user = await UserService().get_user(uow=uow, user_id=user_id)
    return user


@router.get("/users")
async def get_users(uow: UOWDepends):
    users = await UserService().get_users(uow=uow)
    return users


@router.put("/user")
async def edit_user(user: UserUpdateSchema, uow: UOWDepends):
    user = await UserService().edit_user(uow=uow, user=user)
    return user


@router.delete("/user")
async def delete_user(user: UserDeleteSchema, uow: UOWDepends):
    edited_rowcount = await UserService().delete_user(uow=uow, user=user)
    return edited_rowcount
