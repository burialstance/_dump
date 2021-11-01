from typing import Optional

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from database.models import AbstractBaseModel
from database.mixins import TimestampMixin


class User(AbstractBaseModel, TimestampMixin):
    id: int = fields.IntField(pk=True)
    username: str = fields.CharField(max_length=64)
    is_bot: Optional[bool] = fields.BooleanField(null=True)
    first_name: Optional[str] = fields.CharField(max_length=64, null=True)
    last_name: Optional[str] = fields.CharField(max_length=64, null=True)
    language_code: Optional[str] = fields.CharField(max_length=2, null=True)


User_Pydantic = pydantic_model_creator(User)
