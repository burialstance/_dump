from typing import Optional, List

from loguru import logger
from tortoise import fields, models

from database.enums import CountriesEnum
from database import mixins
from misc.enum_to_icon import icon_for_country


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
                logger.debug('created new country', instance)
                created.append(instance)

        return created
