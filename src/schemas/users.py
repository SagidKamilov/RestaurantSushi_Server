import datetime

from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    telegram_id: int
    date_registration: datetime.date
    time_registration: datetime.time
    date_update: datetime.date
    time_update: datetime.time
    name: str
    address: str
    count_ask_address: int
    ban: bool

    class Config:
        from_attributes = True


class UserAddSchema(BaseModel):
    name: str
    telegram_id: int
    date_registration: datetime.date
    time_registration: datetime.time
    date_update: datetime.date
    time_update: datetime.time
    address: str
    count_ask_address: int
    ban: bool


class UserGetSchema(BaseModel):
    id: int


class UserUpdateSchema(BaseModel):
    id: int
    telegram_id: int
    date_update: datetime.date
    time_update: datetime.time
    name: Optional[str]
    address: Optional[str]
    count_ask_address: Optional[int]
    ban: Optional[bool]


class UserDeleteSchema(BaseModel):
    id: int
