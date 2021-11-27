from typing import Optional

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

from database.mixins import TimestampMixin, BaseMixin


class User(BaseMixin, TimestampMixin, models.Model):
    username: str = fields.CharField(max_length=64)
    is_bot: Optional[bool] = fields.BooleanField(null=True)
    first_name: Optional[str] = fields.CharField(max_length=64, null=True)
    last_name: Optional[str] = fields.CharField(max_length=64, null=True)
    language_code: Optional[str] = fields.CharField(max_length=2, null=True)

    class Meta:
        table = "users"

User_Pydantic = pydantic_model_creator(User)
