from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import DB_URL

engine = create_async_engine(DB_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def async_session():
    async with async_session_maker() as session:
        yield session
