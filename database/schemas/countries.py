from typing import Optional

from pydantic import BaseModel


class Country(BaseModel):
    name: str
    icon: Optional[str]