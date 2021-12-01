from typing import Optional, List

from tortoise import fields, models
from tortoise.exceptions import DoesNotExist
from aiocache import cached

from database.enums import CountriesEnum
from database import mixins
from misc.enum_to_icon import icon_for_country
from database.exceptions.countries import CountryDoesNotExist


class Country(mixins.BaseMixin, models.Model):
    name: CountriesEnum = fields.CharEnumField(CountriesEnum)
    icon: str = fields.CharField(max_length=8)

    @staticmethod
    async def create_countries():
        created: List[Optional[Country]] = []
        for country in list(CountriesEnum):
            if not await Country.exists(name=country.value):
                instance = await Country.create(
                    name=country.value,
                    icon=icon_for_country.get(country, None))
                created.append(instance)
        return created

    @staticmethod
    @cached(ttl=600)
    async def get_country(id: int):
        try:
            return await Country.get(id=id)
        except DoesNotExist:
            raise CountryDoesNotExist(telegram_notify='Страна не существует')

    @staticmethod
    @cached(ttl=600)
    async def get_all_countries() -> List:
        return await Country.all()


