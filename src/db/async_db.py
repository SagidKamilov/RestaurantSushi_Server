from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from motor.motor_asyncio import AsyncIOMotorClient

from src.config import DB_URL_SQLITE
from src.config import DB_URL_MONGO

engine_orm = create_async_engine(DB_URL_SQLITE)
async_session_maker_orm = async_sessionmaker(engine_orm, expire_on_commit=False)


engine_motor = AsyncIOMotorClient(DB_URL_MONGO)
async_session_maker_mongodb = engine_motor.sushi
