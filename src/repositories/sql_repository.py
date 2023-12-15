from sqlalchemy import insert, update, delete, select
from sqlalchemy.ext.asyncio import AsyncSession


class SQLOrmRepository:
    model = None

    async def add_one(self):
        pass

    async def edit_one(self):
        pass

    async def find_one(self):
        pass

    async def find_all(self):
        pass

    async def delete_one(self):
        pass