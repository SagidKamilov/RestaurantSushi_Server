import uvicorn

from fastapi import FastAPI

from src.api.routers import all_routers
from src.db.create_db import create_database


app = FastAPI(title="API для Restaurant of Sushi")


@app.on_event('startup')
async def create_db():
    await create_database()


for router in all_routers:
    app.include_router(router=router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
