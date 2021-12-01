from aiogram import types
from aiogram.utils.callback_data import CallbackData

from database.models.countries import Country
from database.enums import GendersEnum
from misc import icons
from misc.enum_to_icon import icon_for_gender

profile_callback = CallbackData('profile', 'section')
profile_settings_callback = CallbackData('profile_settings', 'section')
profile_settings_set_callback = CallbackData('profile_settings_set', 'action', 'data')


def build_profile_kb():
    kb = types.InlineKeyboardMarkup()
    kb.row(types.InlineKeyboardButton(
        text=f'{icons.person} Настройки профиля',
        callback_data=profile_callback.new(section='settings')
    ))
    kb.row(types.InlineKeyboardButton(
        text=f'Реферальный кабинет',
        callback_data=profile_callback.new(section='referral_cabinet')
    ))
    return kb


def build_profile_settings_kb():
    kb = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(
            text=f'{icons.underage} Возраст',
            callback_data=profile_settings_callback.new(section='age')
        ),
        types.InlineKeyboardButton(
            text=f'{icons.couple} Пол',
            callback_data=profile_settings_callback.new(section='gender')
        ),
        types.InlineKeyboardButton(
            text=f'{icons.world} Страна',
            callback_data=profile_settings_callback.new(section='country')
        )
    ]
    kb.add(*buttons)
    kb.row(
        types.InlineKeyboardButton(
            text=f'{icons.arrow_left} Назад',
            callback_data=profile_settings_callback.new(section='back')
        )
    )
    return kb


async def build_profile_settings_set_country_kb() -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=2)
    countries = await Country.get_all_countries()
    for country in countries:
        kb.insert(types.InlineKeyboardButton(
            text=f'{country.icon} {country.name}',
            callback_data=profile_settings_set_callback.new(action='set_country', data=country.id)))

    kb.row(
        types.InlineKeyboardButton(
            text=f'{icons.arrow_left} Назад',
            callback_data=profile_settings_set_callback.new(action='back', data='-')
        )
    )

    return kb


def build_profile_settings_set_gender_kb() -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup()
    for gender in list(GendersEnum):
        kb.insert(types.InlineKeyboardButton(
            text=f'{icon_for_gender.get(gender)} {gender.value}',
            callback_data=profile_settings_set_callback.new(action='set_gender', data=gender.value)
        ))

    kb.row(
        types.InlineKeyboardButton(
            text=f'{icons.arrow_left} Назад',
            callback_data=profile_settings_set_callback.new(action='back', data='-')
        )
    )
    return kb