from src.services.menu import MenuService
from src.schemas.menu import MenuDelSchema, MenuAddSchema, MenuUpdateSchema
from src.api.dependencies import UOWDepends

from fastapi import APIRouter


router = APIRouter(
    prefix="/menu",
    tags=[
        "Menu"
    ]
)


@router.get("")
async def add_menu(menu: MenuAddSchema, uow: UOWDepends):
    menu_data = await MenuService().add_menu(menu=menu, uow=uow)
    return menu_data


@router.post("")
async def post_menu(menu: MenuUpdateSchema, uow: UOWDepends):
    menu_data = await MenuService().update_menu(menu=menu, uow=uow)
    return menu_data


@router.delete("")
async def del_menu(menu: MenuDelSchema, uow: UOWDepends):
    menu_data = await MenuService().del_menu(menu=menu, uow=uow)
    return {"deleted_rows": menu_data}



