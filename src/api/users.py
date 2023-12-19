from fastapi import APIRouter

from src.schemas.users import UserAddSchema, UserGetSchema, UserUpdateSchema, UserDeleteSchema
from src.services.users import UserService

from src.api.dependencies import UOWDepends

router = APIRouter(
    tags=["User"],
)


@router.post("/user")
async def add_user(user: UserAddSchema, uow: UOWDepends):
    user_id = UserService().add_user(uow=uow, user=user)
    return user_id


@router.get("/user")
async def get_user(user: UserGetSchema, uow: UOWDepends):
    user = UserService().get_user(uow=uow, user=user)
    return user


@router.get("/users")
async def get_users(uow: UOWDepends):
    users = UserService().get_users(uow=uow)
    return users


@router.put("/user")
async def edit_user(user: UserUpdateSchema, uow: UOWDepends):
    user = UserService().edit_user(uow=uow, user=user)
    return user


@router.delete("/user")
async def delete_user(user: UserDeleteSchema, uow: UOWDepends):
    edited_rowcount = UserService().delete_user(uow=uow, user=user)
    return edited_rowcount
