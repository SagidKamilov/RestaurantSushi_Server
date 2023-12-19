from abc import ABC, abstractmethod
from typing import Type

from src.db.async_db import async_session_maker

from src.repositories.users import UsersRepository
from src.repositories.admins import AdminsRepository
from src.repositories.menu import MenuRepository
from src.repositories.history import HistoryRepository


class IUnitOfWork(ABC):
    admins: Type[AdminsRepository]
    users: Type[UsersRepository]
    menu: Type[MenuRepository]
    history: Type[HistoryRepository]

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
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UsersRepository(self.session)
        self.admins = AdminsRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
