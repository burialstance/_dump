from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from database.models.user import User, User_Pydantic
from middlewares.userdata import userdata_required
from middlewares.throttling import rate_limit
from misc.messages import (
    build_index_page_text, build_rules_text,
    build_text_from_kwargs
)
from keyboards.inline.profile import (
    build_profile_keyboard,
    profile_callback
)

async def build_user_profile_smart_window(user: User):
    user = user or await User.get(id=types.User.get_current().id)
    user_data = await User_Pydantic.from_tortoise_orm(user)
    text, parse_mode = build_text_from_kwargs(header='User panel', **user_data.dict())
    reply_markup = build_profile_keyboard()
    return dict(text=text, parse_mode=parse_mode, reply_markup=reply_markup)


@userdata_required
@dp.message_handler(Command(['profile']))
async def show_user_profile(message: types.Message, user: User):
    window_kwargs = await build_user_profile_smart_window(user=user)
    await message.answer(**window_kwargs)

@dp.callback_query_handler(profile_callback.filter())
async def process_profile_callback(call: types.CallbackQuery, callback_data: dict):
    section = callback_data.get('section')
    match section:
        case 'settings':
            await call.answer()
        case 'search_options':
            await call.answer()
        case 'referral_cabinet':
            await call.answer()