from typing import Optional

from pydantic import BaseModel


class MenuSchema(BaseModel):
    id: int
    name: str
    weight: int
    composition: str
    cost: int
    stop_list: bool


class MenuAddSchema(BaseModel):
    name: str
    weight: int
    composition: str
    cost: int
    stop_list: Optional[bool] = False


class MenuUpdateSchema(BaseModel):
    name: Optional[str]
    weight: Optional[int]
    composition: Optional[str]
    cost: Optional[int]
    stop_list: Optional[bool]


class MenuDelSchema(BaseModel):
    id: int
