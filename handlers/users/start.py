from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from database.models.users import User
from loader import dp

from middlewares.throttling import rate_limit
from pages.text import build_index_text, build_rules_text
from keyboards.inline.start import (
    build_index_smart_keyboard, index_page_callback,
    build_rules_smart_keyboard
)
from schemas.page import Page

from .registration import start_registration


async def _check_referred_id(message: types.Message, state: FSMContext):
    referred_id = message.get_args()
    if all([referred_id, referred_id.isdigit(), referred_id != message.from_user.id]):
        await state.update_data({'referred_id': referred_id})


async def smart_index_page(registration_btn=None) -> Page:
    if registration_btn is None:
        registration_btn = not await User.exists(id=types.User.get_current().id)

    text, parse_mode = build_index_text()
    reply_markup = await build_index_smart_keyboard(registration_btn=registration_btn)
    return Page(text=text, parse_mode=parse_mode, reply_markup=reply_markup)


async def smart_rules_page(accept_rules_btn=None):
    if accept_rules_btn is None:
        accept_rules_btn = not await User.exists(id=types.User.get_current().id)

    text, parse_mode = build_rules_text()
    reply_markup = await build_rules_smart_keyboard(accept_rules_btn=accept_rules_btn)
    return Page(text=text, parse_mode=parse_mode, reply_markup=reply_markup)


@dp.message_handler(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    await _check_referred_id(message=message, state=state)

    page = await smart_index_page()
    await message.answer(**page.dict(exclude_unset=True))


@dp.callback_query_handler(index_page_callback.filter())
async def process_index_page_callback(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    action = callback_data.get('action')

    if action == 'back':
        page = await smart_index_page()
        await call.message.edit_text(**page.dict(exclude_unset=True))

    if action == 'rules':
        page = await smart_rules_page(accept_rules_btn=False)
        await call.message.edit_text(**page.dict(exclude_unset=True))
        await call.answer()

    if action == 'registration':
        page = await smart_rules_page(accept_rules_btn=True)
        await call.message.edit_text(**page.dict(exclude_unset=True))
        await call.answer('Необходимо ознакомится с правилами')

    if action == 'accept_rules':
        await call.answer()
        await start_registration(message=call.message, state=state, edit_message=True)


