from aiogram import types

from loader import dp
from database.exceptions.profile import ProfileDoesNotExist, ProfileAgeException
from database.utils import notify_telegram_about_exception


@dp.errors_handler(exception=ProfileDoesNotExist)
async def profile_does_not_exist_exc(update: types.Update, exception: ProfileDoesNotExist):
    return await notify_telegram_about_exception(update=update, message=exception.telegram_notify)


@dp.errors_handler(exception=ProfileAgeException)
async def profile_age_exc(update: types.Update, exception: ProfileAgeException):
    return await notify_telegram_about_exception(update=update, message=exception.telegram_notify)