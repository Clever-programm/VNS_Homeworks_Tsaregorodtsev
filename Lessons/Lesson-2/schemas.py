from pydantic import BaseModel, StringConstraints

from typing import Annotated
from typing import Literal
from enum import  StrEnum


class StatusResponse(BaseModel):
    status: Literal["ok"]


class Role(StrEnum):
    USER = "USER"
    ADMIN = "ADMIN"
    MAIN_ADMIN = "MAIN_ADMIN"


class AccountSchema(BaseModel):
    id: int
    login: str
    name: str
    role: Role


class AccountRegisterSchema(BaseModel):
    login: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    password: Annotated[str, StringConstraints(min_length=8, pattern=r"^[a-zA-Z0-9 -] +$")]
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]

