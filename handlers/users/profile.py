from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from database.models.profiles import Profile
from keyboards.inline.profile import (
    build_profile_kb, profile_callback, profile_settings_callback,
    profile_settings_set_callback, build_profile_settings_kb, build_profile_settings_set_gender_kb,
    build_profile_settings_set_country_kb
)
from loader import dp
from pages.text import build_profile_text
from schemas.page import Page
from states.profile import ProfileState


async def build_profile_smart_page() -> Page:
    profile = await Profile.get_current_profile()
    await profile.fetch_related('country')

    text, parse_mode = build_profile_text(profile=profile)
    reply_markup = build_profile_kb()
    return Page(text=text, parse_mode=parse_mode, reply_markup=reply_markup)


@dp.message_handler(Command(['profile']))
async def show_user_profile(message: types.Message):
    page = await build_profile_smart_page()
    await message.answer(**page.dict())


@dp.callback_query_handler(profile_callback.filter())
async def profile_section_callback(call: types.CallbackQuery, callback_data: dict):
    section = callback_data.get('section')
    if section == 'settings':
        await call.message.edit_reply_markup(reply_markup=build_profile_settings_kb())
        await call.answer()

    if section == 'referral_cabinet':
        await call.answer()


@dp.callback_query_handler(profile_settings_callback.filter())
async def profile_settings_callback(call: types.CallbackQuery, callback_data: dict):
    section = callback_data.get('section')

    if section == 'age':
        await ProfileState.set_age.set()
        await call.message.edit_text(text='Отправь свой возраст цифрами')
        await call.answer()

    if section == 'gender':
        await call.message.edit_text(
            text=f'Выберите ваш пол',
            reply_markup=build_profile_settings_set_gender_kb())
        await call.answer()

    if section == 'country':
        await call.message.edit_text(
            text='Выберите вашу страну',
            reply_markup=await build_profile_settings_set_country_kb())
        await call.answer()

    if section == 'back':
        await call.message.edit_reply_markup(reply_markup=build_profile_kb())
        await call.answer()


@dp.callback_query_handler(profile_settings_set_callback.filter())
async def process_profile_settings_set_callback(call: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    data = callback_data.get('data')
    processed = False

    if action == 'set_country':
        profile = await Profile.get_current_profile()
        processed = await profile.set_country(country_id=data)

    if action == 'set_gender':
        profile = await Profile.get_current_profile()
        processed = await profile.set_gender(gender=data)

    if action == 'back':
        processed = False

    if processed:
        await call.answer('Изменения сохранены')
        page = await build_profile_smart_page()
        await call.message.edit_text(**page.dict())


@dp.message_handler(state=ProfileState.set_age)
async def process_profile_settings_set_age(message: types.Message, state: FSMContext):
    profile = await Profile.get_current_profile()
    processed = await profile.set_age(age=message.text.strip())

    if processed:
        await state.reset_state(with_data=False)
        await message.answer('Изменения сохранены')
        page = await build_profile_smart_page()
        await message.answer(**page.dict())
