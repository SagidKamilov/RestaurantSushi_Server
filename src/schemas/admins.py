from pydantic import BaseModel


class AdminSchema(BaseModel):
    id: int

    class Config:
        from_attributes = True


class AdminGetSchema(BaseModel):
    id: int


class AdminDeleteSchema(BaseModel):
    id: int
