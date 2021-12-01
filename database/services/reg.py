from aiogram import types, Dispatcher
from tortoise.exceptions import OperationalError
from tortoise.transactions import in_transaction

from database.models.profiles import Profile
from database.models.referrals import Referral
from database.models.search_options import SearchOptions
from database.models.users import User
from database.schemas.user import RegistrationForm

async def referred_reward(referred_id: int):

    bot = Dispatcher.get_current().bot
    await bot.send_message(referred_id, 'награда за приглашенного пользователя 100$')
    return True


async def create_referral(referred_id: int, referral_id: int):
    if not await User.exists(id=referred_id):
        return False

    referral = await Referral.create(referred_id=referred_id, referral_id=referral_id)
    if referral:
        await referred_reward(referred_id=referral.referred_id)


async def register_new_user(form: RegistrationForm):
    try:
        async with in_transaction() as connection:
            user = await User.create(
                **form.user.dict(exclude_unset=True),
                using_db=connection
            )

            profile = await Profile.create(
                **form.profile.dict(exclude_unset=True),
                using_db=connection
            )

            search_options = await SearchOptions.create(
                user_id=user.id,
                using_db=connection
            )

            if form.referred_id:
                await create_referral(referred_id=form.referred_id, referral_id=user.id)
    except OperationalError:
        pass
    return user