from aiogram import types
from aiogram.utils.callback_data import CallbackData

from database.enums import CountriesEnum, GendersEnum
from misc.enum_to_icon import icon_for_country, icon_for_gender

registration_callback = CallbackData('registration', 'action', 'payload')


def build_registration_set_country_kb() -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=2)
    countries = [
        CountriesEnum.RUSSIA,
        CountriesEnum.UKRAINE,
        CountriesEnum.BELARUS,
        CountriesEnum.KAZAKHSTAN,
        CountriesEnum.UZBEKISTAN,
        CountriesEnum.TAJIKISTAN,
        CountriesEnum.TURKMENISTAN,
        CountriesEnum.AZERBAIJAN,
        CountriesEnum.ARMENIA,
        CountriesEnum.MOLDOVA
    ]
    for country in countries:
        kb.insert(types.InlineKeyboardButton(
            text=f'{icon_for_country.get(country)} {country}',
            callback_data=registration_callback.new(action='set_country', payload=country)))

    return kb


def build_registration_set_gender_kb() -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup()
    genders = [GendersEnum.MALE, GendersEnum.FEMALE]
    for gender in genders:
        icon = icon_for_gender.get(gender)
        kb.insert(types.InlineKeyboardButton(
            text=f'{icon} {gender}',
            callback_data=registration_callback.new(action='set_gender', payload=gender)
        ))
    return kb
