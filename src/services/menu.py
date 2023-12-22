from src.schemas.menu import MenuAddSchema, MenuDelSchema, MenuUpdateSchema
from src.models.menu import Menu

from src.uow.uow_manager import IUnitOfWork


class MenuService:
    @staticmethod
    async def add_menu(menu: MenuAddSchema, uow: IUnitOfWork):
        menu_data = menu.model_dump()
        async with uow:
            menu_data = await uow.menu.add_one(data=menu_data)
            await uow.commit()
            return menu_data

    @staticmethod
    async def del_menu(menu: MenuDelSchema, uow: IUnitOfWork):
        menu_data = menu.model_dump()
        async with uow:
            row_count = await uow.menu.delete_one(data=menu_data)
            await uow.commit()
            return row_count

    @staticmethod
    async def update_menu(menu: MenuUpdateSchema, uow: IUnitOfWork):
        menu_data = menu.model_dump()
        async with uow:
            menu_data = await uow.menu.edit_one(data=menu_data)
            await uow.commit()
            return menu_data