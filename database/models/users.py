from typing import Optional

from aiogram import types
from tortoise import fields, models
from tortoise.exceptions import DoesNotExist

from database.exceptions.users import UserDoesNotExist
from database.mixins import TimestampMixin, BaseMixin


class User(BaseMixin, TimestampMixin, models.Model):
    class Meta:
        table = "users"
    username: str = fields.CharField(max_length=64)
    is_bot: Optional[bool] = fields.BooleanField(null=True)
    first_name: Optional[str] = fields.CharField(max_length=64, null=True)
    last_name: Optional[str] = fields.CharField(max_length=64, null=True)
    language_code: Optional[str] = fields.CharField(max_length=2, null=True)

    @staticmethod
    async def get_current_user():
        try:
            return await User.get(id=types.User.get_current().id)
        except DoesNotExist:
            raise UserDoesNotExist(telegram_notify='Пользователь не найден')



