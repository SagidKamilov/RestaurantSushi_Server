from src.api.admins import router as admin_router
from src.api.users import router as user_router
from src.api.menu import router as menu_router
from src.api.history import router as history_router


all_routers = [
    admin_router,
    user_router,
    menu_router,
    history_router
