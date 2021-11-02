from typing import Tuple
from loguru import logger
from database.models.user import User
from database.enums import CountriesEnum, GendersEnum


class ReferralService:
    @staticmethod
    async def add_referral(referred_id, referral_id):
        referred_instance = await User.get_or_none(id=referred_id)
        if referred_instance:
            logger.info('NOT IMPLEMENT Created referral related model and make reward for referred')


class UserService:
    @staticmethod
    async def get_or_create(id: int, username: str, is_bot: bool = None, first_name: str = None, last_name: str = None,
                            language_code: str = None, gender: GendersEnum = None, country: CountriesEnum = None,
                            age: int = None, **kwargs) -> Tuple[User, bool]:

        if not isinstance(gender, GendersEnum):
            gender = GendersEnum(gender)

        if not isinstance(country, CountriesEnum):
            country = CountriesEnum(country)

        defaults = dict(
            username=username,
            is_bot=is_bot,
            first_name=first_name,
            last_name=last_name,
            language_code=language_code,
            gender=gender,
            country=country,
            age=age,
            **kwargs
        )
        return await User.get_or_create(id=id, defaults=defaults)

    @staticmethod
    async def register_new_user(id: int, username: str, is_bot: bool = None, first_name: str = None,
                                last_name: str = None,
                                language_code: str = None, gender: GendersEnum = None, country: CountriesEnum = None,
                                age: int = None, referred_id: int = None, **kwargs) -> Tuple[User, bool]:

        user, user_created = await UserService.get_or_create(
            id=id, username=username, is_bot=is_bot, first_name=first_name, last_name=last_name,
            language_code=language_code, gender=gender, country=country, age=age, **kwargs)

        if user_created and referred_id:
            await ReferralService.add_referral(referred_id=referred_id, referral_id=user.id)

        return user, user_created
