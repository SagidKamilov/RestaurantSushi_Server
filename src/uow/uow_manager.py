from abc import ABC, abstractmethod
from typing import Type

from src.db.async_db import async_session_maker_orm, async_session_maker_mongodb

from src.repositories.basket import BasketRepository
from src.repositories.users import UsersRepository
from src.repositories.admins import AdminsRepository
from src.repositories.menu import MenuRepository
from src.repositories.history import HistoryRepository


class IUnitOfWork(ABC):
    users: Type[UsersRepository]
    admins: Type[AdminsRepository]
    history: Type[HistoryRepository]
    menu: Type[MenuRepository]
    basket: Type[BasketRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory_orm = async_session_maker_orm
        self.session_factory_mongo_db = async_session_maker_mongodb

    async def __aenter__(self):
        self.session_orm = self.session_factory_orm()
        self.session_mongo_db = self.session_factory_mongo_db

        self.users = UsersRepository(self.session_orm)
        self.admins = AdminsRepository(self.session_orm)
        self.menu = MenuRepository(self.session_orm)
        self.history = HistoryRepository(self.session_orm)
        self.basket = BasketRepository(self.session_mongo_db)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session_orm.close()

    async def commit(self):
        await self.session_orm.commit()

    async def rollback(self):
        await self.session_orm.rollback()
