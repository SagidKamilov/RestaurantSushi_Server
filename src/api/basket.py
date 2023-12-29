from fastapi import APIRouter

from src.services.basket import BasketService
from src.schemas.basket import BasketAddSchema, BasketUpdateSchema, BasketDeleteSchema
from src.api.dependencies import UOWDepends


router = APIRouter(
    tags=[
        "Basket"
    ]
)


@router.post("/basket")
async def add_basket(basket: BasketAddSchema, uow: UOWDepends):
    basket_id = await BasketService().add_basket(basket=basket, uow=uow)
    return basket_id


@router.get("/basket/{basket_id}")
async def get_basket(basket_id: str, uow: UOWDepends):
    basket = await BasketService().get_basket(basket_id=basket_id, uow=uow)
    return basket


@router.get("/baskets")
async def get_baskets(uow: UOWDepends):
    baskets = await BasketService().get_baskets(uow=uow)
    return baskets


@router.patch("/basket")
async def update_basket(basket: BasketUpdateSchema, uow: UOWDepends):
    basket_id = await BasketService().update_basket(basket=basket, uow=uow)
    return basket_id


@router.delete("/basket")
async def delete_basket(basket: BasketDeleteSchema, uow: UOWDepends):
    basket_id = await BasketService().delete_basket(basket=basket, uow=uow)
    return basket_id
