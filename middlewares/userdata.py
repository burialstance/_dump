import loguru
from aiogram.dispatcher.handler import current_handler, CancelHandler
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

    async def push_user_to_context(self, user_id: int, data: dict):
        handler = current_handler.get()
        if handler and getattr(handler, 'userdata_required', False):
            user = await User.get_or_none(id=user_id)
            if user:
                data['user'] = user
                return

            await self.manager.bot.send_message(chat_id=user_id, text='Для этого действия Требуется регистрация /start')
            raise CancelHandler



    async def on_process_message(self, message: types.Message, data: dict):
        await self.push_user_to_context(user_id=message.from_user.id, data=data)

    async def on_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        await self.push_user_to_context(user_id=callback_query.from_user.id, data=data)
