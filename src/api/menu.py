from src.services.menu import MenuService
from src.schemas.menu import MenuDelSchema, MenuAddSchema, MenuUpdateSchema, MenuGetSchema
from src.api.dependencies import UOWDepends

from fastapi import APIRouter


router = APIRouter(
    tags=[
        "Menu"
    ]
)


@router.get("/menu")
async def get_menu(menu: MenuGetSchema, uow: UOWDepends):
    menu_data = await MenuService().get_menu(uow, menu)
    return menu_data


@router.post("/menu")
async def add_menu(menu: MenuAddSchema, uow: UOWDepends):
    menu_data = await MenuService().add_menu(uow, menu)
    return menu_data


@router.put("/menu")
async def put_menu(menu: MenuUpdateSchema, uow: UOWDepends):
    menu_data = await MenuService().update_menu(uow, menu)
    return menu_data


@router.delete("/menu")
async def del_menu(menu: MenuDelSchema, uow: UOWDepends):
    menu_data = await MenuService().del_menu(uow, menu)
    return {"deleted_rows": menu_data}



