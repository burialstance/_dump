from aiogram.dispatcher.handler import current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from database.models.user import User


def userdata_required(func):
    """Setting userdata_required to function"""
    setattr(func, 'userdata_required', True)
    return func


class UserMiddleware(BaseMiddleware):

    def __init__(self):
        super(UserMiddleware, self).__init__()

    async def push_user_to_context(self, user_id: int, context: dict):
        handler = current_handler.get()
        if handler and getattr(handler, 'userdata_required', False):
            telegram_user = types.User.get_current()
            user, _ = await User.get_or_create(**telegram_user.to_python())
            context['user'] = user

    async def on_process_message(self, message: types.Message, data: dict):
        await self.push_user_to_context(user_id=message.from_user.id, context=data)

    async def on_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        await self.push_user_to_context(user_id=callback_query.from_user.id, context=data)
