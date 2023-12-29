from src.schemas.admins import AdminAddSchema, AdminDeleteSchema
from src.uow.uow_manager import IUnitOfWork


class AdminsService:
    @staticmethod
    async def add_admin(uow: IUnitOfWork, admin: AdminAddSchema):
        admin_dict: dict = admin.model_dump()
        async with uow:
            admin_data = await uow.admins.add_one(admin_dict)
            await uow.commit()
            return admin_data

    @staticmethod
    async def get_admin(uow: IUnitOfWork, id: int):
        admin_data: dict = {"id": id}
        async with uow:
            admin_data = await uow.admins.find_one(data=admin_data)
            return admin_data

    @staticmethod
    async def get_admins(uow: IUnitOfWork):
        async with uow:
            admin_data = await uow.admins.find_all()
            return admin_data

    @staticmethod
    async def delete_admin(uow: IUnitOfWork, admin: AdminDeleteSchema):
        admin_data: dict = admin.model_dump()
        async with uow:
            admin_data = await uow.admins.delete_one(admin_data)
            await uow.commit()
            return admin_data
