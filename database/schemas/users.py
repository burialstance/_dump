from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    is_bot: Optional[bool]
    first_name: Optional[str]
    last_name: Optional[str]
    language_code: Optional[str]


class UserCreate(UserBase):
    id: int
