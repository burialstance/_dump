from typing import Optional

from aiogram import types
from tortoise import fields, models, Tortoise
from tortoise.exceptions import DoesNotExist

from database.enums import GendersEnum
from database import mixins, utils
from database.exceptions.search_options import ToAgeLessThanFromAge, FromAgeGreaterThanToAge, SearchOptionsDoesNotExist
from misc.age import declination


class SearchOptions(mixins.TimestampMixin, models.Model):
    class Meta:
        table = "search_options"

    user: fields.OneToOneRelation['User'] = fields.OneToOneField(
        'models.User', related_name='search_options', on_delete=fields.CASCADE, pk=True, index=True)
    gender: Optional[GendersEnum] = fields.CharEnumField(GendersEnum, null=True)
    country: fields.ForeignKeyNullableRelation = fields.ForeignKeyField(
        'models.Country', related_name='search_options', on_delete=fields.SET_NULL, null=True)
    from_age: Optional[int] = fields.IntField(null=True)
    to_age: Optional[int] = fields.IntField(null=True)

    @staticmethod
    async def get_current_search_options():
        try:
            return await SearchOptions.get(user_id=types.User.get_current().id)
        except DoesNotExist:
            raise SearchOptionsDoesNotExist(telegram_notify='Поисковые опции не существуют')

    async def _update(self, **kwargs):
        return await self.select_for_update().update(**kwargs)

    async def set_from_age(self, from_age: Optional[int]):
        if from_age is not None and self.to_age is not None and from_age > self.to_age:
            raise FromAgeGreaterThanToAge(
                telegram_notify=f'Минимальный возраст для поиска не должен быть больше максимального '
                                f'(сейчас {self.to_age} {declination(self.to_age)})'
            )
        return await self._update(from_age=from_age)

    async def reset_from_age(self):
        return await self.set_from_age(from_age=None)

    async def set_to_age(self, to_age: Optional[int]):
        if to_age is not None and self.from_age is not None and to_age < self.from_age:
            raise ToAgeLessThanFromAge(
                telegram_notify=f'Максимальный возраст для поиска не должен быть меньше минимального '
                                f'(сейчас {self.from_age} {declination(self.from_age)})'
            )
        return await self._update(to_age=to_age)

    async def reset_to_age(self):
        return await self.set_to_age(to_age=None)

    async def set_gender(self, gender: Optional[GendersEnum]):
        return await self._update(gender=gender)

    async def reset_gender(self):
        return await self.set_gender(gender=None)

    async def set_country(self, country_id: Optional[int]):
        return await self._update(country_id=country_id)

    async def reset_country(self):
        return await self.set_country(country_id=None)


Tortoise.init_models(utils.fetch_database_models(), 'models')

