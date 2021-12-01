from typing import Optional

from pydantic import BaseModel


class CountryBase(BaseModel):
    name: str
    icon: Optional[str]

    class Config:
        orm_mode = True


class CountryPublic(BaseModel):
    id: int
