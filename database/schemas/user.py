from typing import Optional

from pydantic import BaseModel

from database.schemas.profile import ProfileCreate


class UserBase(BaseModel):
    username: str
    is_bot: Optional[bool]
    first_name: Optional[str]
    last_name: Optional[str]
    language_code: Optional[str]


class UserCreate(UserBase):
    id: int


class UserPublic(UserBase):
    id: int


class RegistrationForm(BaseModel):
    user: UserCreate
    profile: ProfileCreate
    referred_id: Optional[int]
