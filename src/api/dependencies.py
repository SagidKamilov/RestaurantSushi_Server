from typing import Annotated

from fastapi import Depends

from src.uow.uow_manager import IUnitOfWork, UnitOfWork


UOWDepends = Annotated[IUnitOfWork, Depends(UnitOfWork)]