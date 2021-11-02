from typing import Optional

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from database.models import AbstractBaseModel
from database.mixins import TimestampMixin
from database.enums import CountriesEnum, GendersEnum


class SearchOptions(AbstractBaseModel, TimestampMixin):
    user: str = fields.OneToOneField('models.User', related_name='search_options', on_delete=fields.CASCADE)

    gender: Optional[GendersEnum] = fields.CharEnumField(
        GendersEnum, null=True)

    country: Optional[CountriesEnum] = fields.CharEnumField(
        CountriesEnum, null=True)

    age: Optional[int] = fields.IntField(null=True)


SearchOptions_Pydantic = pydantic_model_creator(SearchOptions)
