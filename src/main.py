from fastapi import FastAPI

from src.api.routers import routers
from src.db.create_db import create_database


app = FastAPI(title="API для Restaurant of Sushi")


@app.on_event('start_up')
async def create_db():
    await create_database()


for router in routers:
    app.include_router(router=router)
