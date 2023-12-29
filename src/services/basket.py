from src.schemas.basket import BasketAddSchema, BasketUpdateSchema, BasketDeleteSchema
from src.uow.uow_manager import IUnitOfWork


class BasketService:
    @staticmethod
    async def add_basket(basket: BasketAddSchema, uow: IUnitOfWork):
        basket_data = basket.model_dump()
        async with uow:
            basket_id = await uow.basket.add_one(data=basket_data)
            await uow.commit()
            return basket_id

    @staticmethod
    async def get_basket(basket_id: str, uow: IUnitOfWork):
        basket_data = {"id": basket_id}
        async with uow:
            basket = await uow.basket.get_one(data=basket_data)
            return basket

    @staticmethod
    async def get_baskets(uow: IUnitOfWork):
        async with uow:
            baskets = await uow.basket.get_all()
            return baskets

    @staticmethod
    async def update_basket(basket: BasketUpdateSchema, uow: IUnitOfWork):
        basket_data = basket.model_dump()
        async with uow:
            basket_id = await uow.basket.edit_one(data=basket_data)
            await uow.commit()
            return basket_id

    @staticmethod
    async def delete_basket(basket: BasketDeleteSchema, uow: IUnitOfWork):
        basket_data = basket.model_dump()
        async with uow:
            basket_id = await uow.basket.delete_one(data=basket_data)
            await uow.commit()
            return basket_id
