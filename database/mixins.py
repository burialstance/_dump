from tortoise import fields
from tortoise import Model, fields


class BaseMixin:
    id = fields.BigIntField(pk=True, index=True)

    class Meta:
        abstract = True

    async def to_dict(self):
        d = {}
        for field in self._meta.db_fields:
            d[field] = getattr(self, field)
        for field in self._meta.backward_fk_fields:
            d[field] = await getattr(self, field).all().values()
        return d


class TimestampMixin:
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
