from src.schemas.menu import MenuAddSchema, MenuDelSchema, MenuUpdateSchema
from src.uow.uow_manager import IUnitOfWork


class MenuService:
    @staticmethod
    async def add_menu(uow: IUnitOfWork, menu: MenuAddSchema):
        menu_data: dict = menu.model_dump()
        async with uow:
            menu_data = await uow.menu.add_one(data=menu_data)
            await uow.commit()
            return menu_data

    @staticmethod
    async def get_menu(uow: IUnitOfWork, menu_id: int):
        menu_data: dict = {"id": menu_id}
        async with uow:
            menu_data = await uow.menu.find_one(data=menu_data)
            return menu_data

    @staticmethod
    async def get_menus(uow: IUnitOfWork):
        async with uow:
            menu_data_all = await uow.menu.find_all()
            return menu_data_all

    @staticmethod
    async def update_menu(uow: IUnitOfWork, menu: MenuUpdateSchema):
        menu_data: dict = menu.model_dump()
        async with uow:
            menu_data = await uow.menu.edit_one(data=menu_data)
            await uow.commit()
            return menu_data

    @staticmethod
    async def del_menu(uow: IUnitOfWork, menu: MenuDelSchema):
        menu_data: dict = menu.model_dump()
        async with uow:
            row_count = await uow.menu.delete_one(data=menu_data)
            await uow.commit()
            return row_count
