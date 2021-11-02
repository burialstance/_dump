from aiogram import types
from aiogram.utils.callback_data import CallbackData

from database.models.user import User
from misc import icons

index_page_callback = CallbackData('index_page', 'action')


async def build_rules_smart_keyboard(user_exists=None):
    kb = types.InlineKeyboardMarkup()
    user_id = types.User.get_current().id
    user_exists = user_exists or await User.exists(id=user_id)
    if not user_exists:
        kb.row(types.InlineKeyboardButton(
            text=f'{icons.checked} С правилами ознакомился',
            callback_data=index_page_callback.new(action='accept_rules')
        ))
    kb.row(types.InlineKeyboardButton(
        text=f'{icons.back} Назад', callback_data=index_page_callback.new(action='back')
    ))
    return kb


async def build_index_smart_keyboard(user_exists=None):
    kb = types.InlineKeyboardMarkup()
    user_id = types.User.get_current().id
    user_exists = user_exists or await User.exists(id=user_id)
    if not user_exists:
        kb.row(types.InlineKeyboardButton(
            text=f'{icons.new} Регистрация', callback_data=index_page_callback.new(action='registration')
        ))
    kb.row(types.InlineKeyboardButton(
        text=f'{icons.book} Правила', callback_data=index_page_callback.new(action='rules')
    ))
    return kb
