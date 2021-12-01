from aiogram import types

from loader import dp
from database.exceptions.countries import CountryDoesNotExist
from database.utils import notify_telegram_about_exception


@dp.errors_handler(exception=CountryDoesNotExist)
async def country_does_not_exist(update: types.Update, exception: CountryDoesNotExist):
    return await notify_telegram_about_exception(update=update, message=exception.telegram_notify)
