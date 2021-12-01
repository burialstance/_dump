from typing import Optional, Union, Tuple, List

from aiogram import types
from tortoise import fields, models, Tortoise
from tortoise.exceptions import DoesNotExist

from database.enums import GendersEnum
from database import mixins, utils
from database.exceptions.profile import ProfileDoesNotExist, ProfileAgeException
from misc.age import declination_from


class Profile(mixins.TimestampMixin, models.Model):
    class Meta:
        table = "profiles"

    user: fields.OneToOneRelation['User'] = fields.OneToOneField(
        'models.User', related_name='profile', on_delete=fields.CASCADE, pk=True, index=True)
    age: Optional[int] = fields.IntField(null=True)
    gender: Optional[GendersEnum] = fields.CharEnumField(GendersEnum, null=True)
    country: fields.ForeignKeyNullableRelation = fields.ForeignKeyField(
        'models.Country', related_name='profiles', on_delete=fields.SET_NULL, null=True)

    @staticmethod
    async def get_current_profile():
        try:
            return await Profile.get(user_id=types.User.get_current().id)
        except DoesNotExist:
            raise ProfileDoesNotExist(telegram_notify='Профиль не существует')

    async def _update(self, **kwargs):
        return await self.select_for_update().update(**kwargs)

    async def set_age(self, age: Optional[int]):
        if age is not None and not Profile.is_acceptable_age(age):
            return False
        return await self._update(age=age)

    async def reset_age(self):
        return await self.set_age(age=None)

    async def set_gender(self, gender: Optional[str]):
        return await self._update(gender=gender)

    async def reset_gender(self):
        return await self.set_gender(gender=None)

    async def set_country(self, country_id: Optional[int]):
        return await self._update(country_id=country_id)

    async def reset_country(self):
        return await self.set_country(country_id=None)

    @staticmethod
    def is_acceptable_age(age: Union[str, int]) -> int:
        minimal_age = 7
        maximum_age = 80

        try:
            age = int(age)
        except ValueError:
            raise ProfileAgeException(telegram_notify='Возраст должен быть числом')

        if age <= 0:
            raise ProfileAgeException(
                telegram_notify='Некорректный возраст'
            )
        elif age < minimal_age:
            raise ProfileAgeException(
                telegram_notify=f'Минимальный допустимый возраст участника от '
                                f'{minimal_age} {declination_from(minimal_age)}'
            )
        elif age > maximum_age:
            raise ProfileAgeException(
                telegram_notify=f'Максимальный допустимый возраст участника от '
                                f'{maximum_age} {declination_from(maximum_age)}'
            )
        return age

Tortoise.init_models(utils.fetch_database_models(), 'models')



