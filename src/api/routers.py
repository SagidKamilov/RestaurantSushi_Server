from src.api.admins import router as admin_router
from src.api.users import router as user_router


all_routers = [
    admin_router,
    user_router,
]