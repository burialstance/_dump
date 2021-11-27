from aiogram import types
from aiogram.utils.callback_data import CallbackData

from database.models.users import User
from misc import icons

index_page_callback = CallbackData('index_page', 'action')


async def build_rules_smart_keyboard(accept_rules_btn=None):
    kb = types.InlineKeyboardMarkup()
    if accept_rules_btn:
        kb.row(types.InlineKeyboardButton(
            text=f'{icons.checked} С правилами ознакомился',
            callback_data=index_page_callback.new(action='accept_rules')
        ))
    kb.row(types.InlineKeyboardButton(
        text=f'{icons.arrow_left} Назад',
        callback_data=index_page_callback.new(action='back')
    ))
    return kb


async def build_index_smart_keyboard(registration_btn=None):
    kb = types.InlineKeyboardMarkup()
    if registration_btn:
        kb.row(types.InlineKeyboardButton(
            text=f'{icons.new} Регистрация',
            callback_data=index_page_callback.new(action='registration')
        ))
    kb.row(types.InlineKeyboardButton(
        text=f'{icons.book} Правила',
        callback_data=index_page_callback.new(action='rules')
    ))
    return kb
