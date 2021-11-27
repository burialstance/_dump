from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise import fields, models, Tortoise

from database.enums import GendersEnum
from database import mixins, utils


class SearchOptions(mixins.TimestampMixin, models.Model):
    user: fields.OneToOneRelation['User'] = fields.OneToOneField(
        'models.User', related_name='search_options', on_delete=fields.CASCADE, pk=True, index=True
    )

    gender: Optional[GendersEnum] = fields.CharEnumField(GendersEnum, null=True)
    country: fields.ForeignKeyNullableRelation = fields.ForeignKeyField(
        'models.Country', related_name='search_options', on_delete=fields.SET_NULL, null=True)
    from_age: Optional[int] = fields.IntField(null=True)
    to_age: Optional[int] = fields.IntField(null=True)

    class Meta:
        table = "search_options"


Tortoise.init_models(utils.fetch_database_models(), 'models')
SearchOptions_Pydantic = pydantic_model_creator(SearchOptions)
