from typing import Optional

from tortoise import fields, models, Tortoise

from database.enums import GendersEnum, CountriesEnum
from database import mixins, utils


class Profile(mixins.TimestampMixin, models.Model):
    user: fields.OneToOneRelation['User'] = fields.OneToOneField(
        'models.User', related_name='profile', on_delete=fields.CASCADE, pk=True, index=True
    )

    gender: Optional[GendersEnum] = fields.CharEnumField(GendersEnum, null=True)
    country: fields.ForeignKeyNullableRelation = fields.ForeignKeyField(
        'models.Country', related_name='profiles', on_delete=fields.SET_NULL, null=True)
    age: Optional[int] = fields.IntField(null=True)

    class Meta:
        table = "profiles"


Tortoise.init_models(utils.fetch_database_models(), 'models')
