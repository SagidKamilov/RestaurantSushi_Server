from src.schemas.users import UserAddSchema, UserGetSchema, UserUpdateSchema, UserDeleteSchema
from src.uow.uow_manager import IUnitOfWork


class UserService:
    @staticmethod
    async def add_user(uow: IUnitOfWork, user: UserAddSchema):
        user_dict: dict = user.model_dump()
        async with uow:
            user_id = await uow.users.add_one(data=user_dict)
            await uow.commit()
            return user_id

    @staticmethod
    async def get_user(uow: IUnitOfWork, user_id: int):
        user_dict: dict = {"id": user_id}
        async with uow:
            user = await uow.users.find_one(data=user_dict)
            return user

    @staticmethod
    async def get_users(uow: IUnitOfWork):
        async with uow:
            users = await uow.users.find_all()
            return users

    @staticmethod
    async def edit_user(uow: IUnitOfWork, user: UserUpdateSchema):
        user_dict = user.model_dump()
        async with uow:
            user_id = await uow.users.edit_one(data=user_dict)
            await uow.commit()
            return user_id

    @staticmethod
    async def delete_user(uow: IUnitOfWork, user: UserDeleteSchema):
        user_dict = user.model_dump()
        async with uow:
            edited_rowcount = await uow.users.delete_one(data=user_dict)
            await uow.commit()
            return edited_rowcount
