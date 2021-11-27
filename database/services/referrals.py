from .base_service import BaseService
from ..models.referrals import Referral


class ReferralService(BaseService[Referral]):

    async def create_referral(self, referred_id: int, referral_id: int):
        instance = await self._create(referred_id=referred_id, referral_id=referral_id)
        return instance


referral_service = ReferralService(Referral)
