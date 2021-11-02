from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text, Command
from aiogram.types import ParseMode

from loader import dp
from database.models.search_options import SearchOptions, SearchOptions_Pydantic
from database.models.user import User, User_Pydantic
from misc.messages import build_text_from_kwargs


@dp.message_handler(Command('user'))
async def info_user(message: types.Message):
    try:
        user_model = await User.get(id=message.from_user.id)
        user_data = await User_Pydantic.from_tortoise_orm(user_model)
        text, parse_mode = build_text_from_kwargs(header=f'User model info', **user_data.dict())
        await message.answer(text=text, parse_mode=parse_mode)
    except Exception as e:
        await message.answer(text=f'Exception: {e}')


@dp.message_handler(Command('search'))
async def info_user(message: types.Message):
    try:
        search_model = await SearchOptions.get(user_id=message.from_user.id)
        search_data = await SearchOptions_Pydantic.from_tortoise_orm(search_model)
        text, parse_mode = build_text_from_kwargs(header=f'SearchOptions model info', **search_data.dict())
        await message.answer(text=text, parse_mode=parse_mode)
    except Exception as e:
        await message.answer(text=f'Exception: {e}')
