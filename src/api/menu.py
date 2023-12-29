from fastapi import APIRouter

from src.services.menu import MenuService
from src.schemas.menu import MenuDelSchema, MenuAddSchema, MenuUpdateSchema, MenuGetSchema
from src.api.dependencies import UOWDepends


router = APIRouter(
    tags=[
        "Menu"
    ]
)


@router.post("/menu")
async def add_menu(menu: MenuAddSchema, uow: UOWDepends):
    menu_data = await MenuService().add_menu(uow, menu)
    return menu_data


@router.get("/menu/{menu_id}")
async def get_menu(menu_id: int, uow: UOWDepends):
    menu_data = await MenuService().get_menu(uow, menu_id)
    return menu_data


@router.get("/menu")
async def get_menus(uow: UOWDepends):
    menu_data_all = await MenuService().get_menus(uow)
    return menu_data_all


@router.put("/menu")
async def put_menu(menu: MenuUpdateSchema, uow: UOWDepends):
    menu_data = await MenuService().update_menu(uow, menu)
    return menu_data


@router.delete("/menu")
async def del_menu(menu: MenuDelSchema, uow: UOWDepends):
    menu_data = await MenuService().del_menu(uow, menu)
    return {"deleted_rows": menu_data}
