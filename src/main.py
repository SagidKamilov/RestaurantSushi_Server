from asyncio import get_event_loop

from uvicorn import run
from fastapi import FastAPI

from src.api.routers import routers
from src.db.create_db import create_database

app = FastAPI(title="API для Restaurant of Sushi")

for router in routers:
    app.include_router(router=router)


if __name__ == "__main__":
    loop = get_event_loop()
    loop.run_until_complete(create_database())

    run(app="main:app")
