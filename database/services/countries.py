from aiocache import Cache, cached
from typing import Optional, List

from .base_service import BaseService
from ..models.countries import Country


class CountriesService(BaseService[Country]):

    @cached(ttl=60)
    async def get_all(self) -> List[Optional[Country]]:
        return await self._all()


countries_service = CountriesService(Country)
