from fastapi import APIRouter

from src.schemas.admins import AdminGetSchema, AdminDeleteSchema, AdminAddSchema
from src.services.admins import AdminsService

from src.api.dependencies import UOWDepends


router = APIRouter(
    tags=["Admin"]
)


@router.post("/admin")
async def add_admin(admin: AdminAddSchema, uow: UOWDepends):
    admin_id = await AdminsService().add_admin(uow, admin)
    return admin_id


@router.get("/admin/{id}")
async def get_admin(id: int, uow: UOWDepends):
    admin_data = await AdminsService().get_admin(uow, id)
    return admin_data


@router.get("/admins")
async def get_admins(uow: UOWDepends):
    admins_data = await AdminsService().get_admins(uow)
    return admins_data


@router.delete("/admin")
async def delete_admin(admin: AdminDeleteSchema, uow: UOWDepends):
    admin_data = await AdminsService().delete_admin(uow, admin)
    return {"deleted_rows": admin_data}
