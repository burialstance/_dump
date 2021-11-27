from typing import TypeVar, Type, Generic, Optional, List, Any

from tortoise import models

ModelType = TypeVar("ModelType", bound=models.Model)


class BaseService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    @property
    def pk_field(self):
        return self.model._meta.pk_attr

    async def _get(self, **kwargs) -> ModelType:
        return await self.model.filter(**kwargs).first()

    async def _create(self, **kwargs) -> ModelType:
        return await self.model.create(**kwargs)

    async def _update(self, pk: Any, **kwargs):
        lookup = {self.pk_field: pk}
        return await self.model.filter(**lookup).update(**kwargs)

    async def _delete(self, **kwargs) -> ModelType:
        instance = await self.model.filter(**kwargs).first()
        await instance.delete()
        return instance

    async def _all(self) -> List[Optional[ModelType]]:
        return await self.model.all()

    async def _exists(self, **kwargs) -> bool:
        return await self.model.exists(**kwargs)
