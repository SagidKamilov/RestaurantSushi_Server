from pydantic import BaseModel


class AdminSchema(BaseModel):
    id: int
    level: int

    class Config:
        from_attributes = True


class AdminAddSchema(BaseModel):
    level: int


class AdminGetSchema(BaseModel):
    id: int


class AdminDeleteSchema(BaseModel):
    id: int
