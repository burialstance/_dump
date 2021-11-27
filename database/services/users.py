from typing import Optional, Any

from pydantic import BaseModel

from .base_service import BaseService
from .referrals import referral_service
from ..models.users import User
from ..schemas.profiles import ProfileBase, ProfileUpdate
from ..schemas.users import UserCreate

from ..services.profiles import profiles_service


class SignupForm(BaseModel):
    user: UserCreate
    profile: Optional[ProfileUpdate]
    referred_id: Optional[int]


class UserService(BaseService[User]):
    async def exists(self, pk: Any):
        lookup = {self.pk_field: pk}
        return await self._exists(**lookup)

    async def create_user(self, form: UserCreate) -> User:
        return await self._create(**form.dict(exclude_unset=True))

    async def get_user(self, telegram_id: int) -> User:
        return await self._get(id=telegram_id)

    async def registration(self, form: SignupForm) -> User:
        user = await self.create_user(form.user)
        print(form)
        if form.profile:
            await profiles_service.update_profile(form.profile)

        if form.referred_id and await self.exists(pk=form.referred_id):
            await referral_service.create_referral(referred_id=form.referred_id, referral_id=user.id)

        return user



users_service = UserService(User)