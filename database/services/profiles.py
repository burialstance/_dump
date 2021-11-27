from .base_service import BaseService

from ..models.profiles import Profile
from ..schemas.profiles import ProfileUpdate


class ProfileService(BaseService[Profile]):

    async def update_profile(self, form: ProfileUpdate):
        validated_data = form.dict(exclude_unset=True)
        pk = validated_data.pop('user_id')
        return await self._update(pk=pk, **validated_data)

    async def get_profile(self, **kwargs) -> Profile:
        profile = await self._get(**kwargs)
        if profile:
            await profile.fetch_related('country')
        return profile


profiles_service = ProfileService(Profile)