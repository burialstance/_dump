from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from handlers.users.registration import start_registration
from middlewares.userdata import userdata_required
from middlewares.throttling import rate_limit
from misc.messages import (
    build_index_page_text, build_rules_text
)
from keyboards.inline.start import (
    index_page_callback,
    build_index_smart_keyboard,
    build_rules_smart_keyboard
)


async def check_referred_id(message: types.Message, state: FSMContext):
    referred_id = message.get_args()
    if referred_id.isdigit():
        await state.update_data({'referred_id': int(referred_id)})


@rate_limit(.1)
async def build_index_window():
    text, parse_mode = build_index_page_text()
    reply_markup = await build_index_smart_keyboard()
    return dict(text=text, parse_mode=parse_mode, reply_markup=reply_markup)


@rate_limit(.1)
async def build_rules_window():
    text, parse_mode = build_rules_text()
    reply_markup = await build_rules_smart_keyboard()
    return dict(text=text, parse_mode=parse_mode, reply_markup=reply_markup)


@rate_limit(.1)
@dp.message_handler(CommandStart())
async def process_start_command(message: types.Message, state: FSMContext):
    await check_referred_id(message=message, state=state)

    window_kwargs = await build_index_window()
    await message.answer(**window_kwargs)

@rate_limit(.1)
@dp.callback_query_handler(index_page_callback.filter())
async def process_index_page_callback(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    action = callback_data.get('action')

    match action:
        case 'registration':
            window_kwargs = await build_rules_window()
            await call.message.edit_text(**window_kwargs)
            await call.answer('Необходимо ознакомиться с правилами')

        case 'rules':
            window_kwargs = await build_rules_window()
            await call.message.edit_text(**window_kwargs)
            await call.answer()

        case 'back':
            window_kwargs = await build_index_window()
            await call.message.edit_text(**window_kwargs)
            await call.answer()

        case 'accept_rules':
            await call.answer()
            await start_registration(message=call.message, edit_message=True, state=state)
