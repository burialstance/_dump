from aiogram import types
from aiogram.utils.callback_data import CallbackData
from misc import icons

profile_callback = CallbackData('profile', 'section')


def build_profile_keyboard():
    kb = types.InlineKeyboardMarkup()
    kb.row(types.InlineKeyboardButton(
        text=f'{icons.person} Настройки профиля',
        callback_data=profile_callback.new(section='settings')
    )),
    kb.row(types.InlineKeyboardButton(
        text=f'{icons.search} Настройки поиска',
        callback_data=profile_callback.new(section='search_options')
    ))
    kb.row(types.InlineKeyboardButton(
        text=f'Реферальный кабинет',
        callback_data=profile_callback.new(section='referral_cabinet')
    ))
    return kb

def build_profile_settings_kb():
    kb = types.InlineKeyboardMarkup(row_width=2)
