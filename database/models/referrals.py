from tortoise import fields, models, Tortoise

from database import mixins, utils


class Referral(mixins.BaseMixin, mixins.TimestampMixin, models.Model):
    referred: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User', on_delete=fields.CASCADE, related_name='referrals'
    )
    referral: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User', on_delete=fields.CASCADE, related_name='referred'
    )

    class Meta:
        table = "referrals"

Tortoise.init_models(utils.fetch_database_models(), 'models')
