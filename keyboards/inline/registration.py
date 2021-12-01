from aiogram import types
from aiogram.utils.callback_data import CallbackData

from database import Country
from database.enums import GendersEnum
from misc.enum_to_icon import icon_for_country, icon_for_gender

registration_callback = CallbackData('registration', 'action', 'payload')


async def build_registration_set_country_kb() -> types.InlineKeyboardMarkup:
    available_countries = await Country.get_all_countries()

    kb = types.InlineKeyboardMarkup(row_width=2)
    for country in available_countries:
        kb.insert(types.InlineKeyboardButton(
            text=f'{country.icon} {country.name}',
            callback_data=registration_callback.new(action='set_country', payload=country.id)))

    return kb


def build_registration_set_gender_kb() -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup()
    for gender in list(GendersEnum):
        icon = icon_for_gender.get(gender)
        kb.insert(types.InlineKeyboardButton(
            text=f'{icon} {gender.value}',
            callback_data=registration_callback.new(action='set_gender', payload=gender.value)
        ))
    return kb
