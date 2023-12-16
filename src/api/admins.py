from fastapi import APIRouter

from src.schemas.admins import AdminGetSchema, AdminDeleteSchema, AdminAddSchema
from src.services.admins import AdminsService

from src.api.dependencies import UOWDepends


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.post("")
async def add_admin(admin: AdminAddSchema, uow: UOWDepends):
    admin_id = await AdminsService.add_admin(uow, admin)
    return admin_id


@router.get("")
async def get_admin(admin: AdminGetSchema, uow: UOWDepends):
    admin_data = await AdminsService.get_admin(uow, admin)
    return admin_data


@router.get("")
async def get_admins(uow: UOWDepends):
    admins_data = await AdminsService.get_admins(uow)
    return admins_data


@router.delete("")
async def delete_admin(admin: AdminDeleteSchema, uow: UOWDepends):
    admin_data = await AdminsService.delete_admin(uow, admin)
    return {"deleted_rows": admin_data}

