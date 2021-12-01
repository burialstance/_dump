from typing import Optional

from pydantic import BaseModel

from database.enums import GendersEnum
from database.schemas.country import CountryPublic


class ProfileBase(BaseModel):
    age: Optional[int]
    gender: Optional[GendersEnum]
    country_id: Optional[int]

    class Config:
        orm_mode = True


class ProfileDetail(BaseModel):
    class Config:
        orm_mode = True

    age: Optional[int]
    gender: Optional[GendersEnum]
    country: Optional[CountryPublic]


class ProfileCreate(ProfileBase):
    user_id: int