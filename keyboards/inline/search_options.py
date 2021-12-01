from aiogram import types
from aiogram.utils.callback_data import CallbackData

from database import Country
from database.enums import GendersEnum
from misc import icons
from misc.enum_to_icon import icon_for_gender

search_options_callback = CallbackData('search_options', 'section')
search_options_set_callback = CallbackData('search_options_set', 'action', 'data')

search_options_age_callback = CallbackData('search_options_age', 'action')
search_options_age_set_callback = CallbackData('search_options_age_set', 'action', 'data')


def build_search_options_kb():
    kb = types.InlineKeyboardMarkup()
    kb.row(types.InlineKeyboardButton(
        text=f'{icons.underage} Возраст собеседника',
        callback_data=search_options_callback.new(section='age')
    ))
    kb.row(types.InlineKeyboardButton(
        text=f'{icons.couple} Пол собеседника',
        callback_data=search_options_callback.new(section='gender')
    ))
    kb.row(types.InlineKeyboardButton(
        text=f'{icons.world} Страна собеседника',
        callback_data=search_options_callback.new(section='country')
    ))
    return kb


async def build_search_options_set_country_kb():
    kb = types.InlineKeyboardMarkup(row_width=2)
    countries = await Country.get_all_countries()
    for country in countries:
        kb.insert(types.InlineKeyboardButton(
            text=f'{country.icon} {country.name}',
            callback_data=search_options_set_callback.new(action='set_country', data=country.id)))

    kb.row(types.InlineKeyboardButton(
        text=f'{icons.world} Сбросить',
        callback_data=search_options_set_callback.new(action='reset_country', data='-')
    ))
    kb.row(
        types.InlineKeyboardButton(
            text=f'{icons.arrow_left} Назад',
            callback_data=search_options_set_callback.new(action='back', data='-')
        )
    )

    return kb


def build_search_options_set_gender_kb():
    kb = types.InlineKeyboardMarkup()
    for gender in list(GendersEnum):
        kb.insert(types.InlineKeyboardButton(
            text=f'{icon_for_gender.get(gender)} {gender.value}',
            callback_data=search_options_set_callback.new(action='set_gender', data=gender.value)
        ))

    kb.row(
        types.InlineKeyboardButton(
            text=f'Сбросить',
            callback_data=search_options_set_callback.new(action='reset_gender', data='-')
        )
    )
    kb.row(
        types.InlineKeyboardButton(
            text=f'{icons.arrow_left} Назад',
            callback_data=search_options_set_callback.new(action='back', data='-')
        )
    )
    return kb


def build_search_options_age_kb():
    kb = types.InlineKeyboardMarkup()
    kb.row(types.InlineKeyboardButton(
        text='Максимальный возраст собеседника',
        callback_data=search_options_age_callback.new(action='to_age')
    ))
    kb.row(types.InlineKeyboardButton(
        text='Минимальный возраст собеседника',
        callback_data=search_options_age_callback.new(action='from_age')
    ))
    kb.row(types.InlineKeyboardButton(
        text='Сбросить',
        callback_data=search_options_age_callback.new(action='reset_age')
    ))
    kb.row(
        types.InlineKeyboardButton(
            text=f'{icons.arrow_left} Назад',
            callback_data=search_options_age_callback.new(action='back')
        )
    )

    return kb


def _build_search_options_set_age_kb(direction: str):
    assert direction in ['from', 'to']
    kb = types.InlineKeyboardMarkup(row_width=5)
    for i in range(7, 80, 3):
        kb.insert(types.InlineKeyboardButton(
            text=str(i),
            callback_data=search_options_age_set_callback.new(action=f'set_{direction}_age', data=i)
        ))
    kb.row(types.InlineKeyboardButton(
        text='Сбросить',
        callback_data=search_options_age_set_callback.new(action=f'reset_{direction}_age', data='-')
    ))
    kb.row(types.InlineKeyboardButton(
        text=f'{icons.arrow_left} Назад',
        callback_data=search_options_age_set_callback.new(action='back', data='-')
    ))
    return kb


def build_search_options_set_from_age_kb():
    return _build_search_options_set_age_kb('from')


def build_search_options_set_to_age_kb():
    return _build_search_options_set_age_kb('to')