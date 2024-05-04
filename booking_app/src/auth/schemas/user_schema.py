from datetime import datetime
from typing import Optional

from pydantic import (
    BaseModel,
    ConfigDict,
)

from src.auth.enums import UserRole


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    role: UserRole


class UserCreateSchema(UserBaseSchema):
    pass


class UserReadSchema(UserBaseSchema):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class UserUpdatePartialSchema(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    role: UserRole | None = None


class UserUpdateSchema(BaseModel):
    first_name: str
    last_name: str
    role: UserRole


class UserCreateRetrieveSchema(UserBaseSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int
