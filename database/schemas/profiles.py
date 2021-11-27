from typing import Optional

from pydantic import BaseModel, PositiveInt, validate_arguments

from database.enums import GendersEnum
from database.schemas.countries import Country


class ProfileBase(BaseModel):
    gender: Optional[GendersEnum]
    country_id: Optional[PositiveInt]
    age: Optional[PositiveInt]


class ProfileUpdate(ProfileBase):
    user_id: PositiveInt


class Profile(BaseModel):
    user_id: int
    age: Optional[int]
    gender: Optional[GendersEnum]
    country: Optional[Country]

    class Config:
        orm_mode = True