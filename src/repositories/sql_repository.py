from sqlalchemy import insert, update, delete, select
from sqlalchemy.ext.asyncio import AsyncSession


class SQLOrmRepository:
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model.id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def find_one(self, data: dict):
        hidden_id = data.get("id")
        stmt = select(self.model).filter_by(id=hidden_id)
        result = await self.session.execute(stmt)
        print(result)
        return result.scalar_one().to_read_model()

    async def find_all(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        result = [record[0].to_read_model() for record in result.all()]
        return result

    async def edit_one(self, data: dict):
        hidden_id = data.get("id")
        stmt = update(self.model).values(**data).filter_by(id=hidden_id).returning(self.model.id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def delete_one(self, data: dict):
        hidden_id = data.get("id")
        stmt = delete(self.model).filter_by(id=hidden_id)
        result = await self.session.execute(stmt)
        return result.rowcount
