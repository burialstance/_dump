from aiogram import types

from loader import dp
from database.utils import notify_telegram_about_exception
from database.exceptions.search_options import (
    SearchOptionsDoesNotExist,
    ToAgeLessThanFromAge,
    FromAgeGreaterThanToAge
)


@dp.errors_handler(exception=SearchOptionsDoesNotExist)
async def search_options_does_not_exist_exc(update: types.Update, exception: SearchOptionsDoesNotExist):
    return await notify_telegram_about_exception(update=update, message=exception.telegram_notify)


@dp.errors_handler(exception=ToAgeLessThanFromAge)
async def search_options_to_age_exc(update: types.Update, exception: ToAgeLessThanFromAge):
    return await notify_telegram_about_exception(update=update, message=exception.telegram_notify)


@dp.errors_handler(exception=FromAgeGreaterThanToAge)
async def search_options_from_age_exc(update: types.Update, exception: FromAgeGreaterThanToAge):
    return await notify_telegram_about_exception(update=update, message=exception.telegram_notify)

