from typing import Annotated

from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)


# @router.post("")