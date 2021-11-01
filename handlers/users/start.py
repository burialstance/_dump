from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ParseMode

from loader import dp

from database.models.user import User, User_Pydantic
from middlewares.userdata import userdata_required
from middlewares.throttling import rate_limit
from misc.messages import build_start_message


@userdata_required
@dp.message_handler(CommandStart())
async def process_start_command(message: types.Message, user: User):
    user_data = await User_Pydantic.from_tortoise_orm(user)
    text, parse_mode = await build_start_message(**user_data.dict())
    await message.answer(text=text, parse_mode=parse_mode)
