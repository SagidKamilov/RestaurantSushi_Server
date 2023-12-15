from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    date_registration: datetime.date
    time_registration: datetime.time
    date_update: datetime.date
    time_update: datetime.time
    name: str
    address: str
    check_address: int
    ban: bool

    class Config:
        from_attributes = True


class UserAddSchema(BaseModel):
    name: str
    date_registration: datetime.date
    time_registration: datetime.time
    date_update: datetime.date = 0
    time_update: datetime.time = 0
    address: Optional[str] = None
    check_address: Optional[int] = 0
    ban: Optional[bool] = False


class UserGetSchema(BaseModel):
    id: int


class UserUpdateSchema(BaseModel):
    date_update: datetime.date
    time_update: datetime.time
    name: Optional[str]
    address: Optional[str]
    check_address: Optional[int]
    ban: Optional[bool]


class UserDeleteSchema(BaseModel):
    id: int
