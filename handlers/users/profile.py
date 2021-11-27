from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from database.models.users import User
from database.schemas.profiles import Profile, ProfileUpdate
from database.services.profiles import profiles_service
from keyboards.inline.profile import (
    build_profile_kb, profile_callback, profile_settings_callback,
    profile_settings_set_callback, build_profile_settings_kb, build_profile_settings_set_gender_kb,
    build_profile_settings_set_country_kb
)
from loader import dp
from middlewares.userdata import userdata_required
from pages.text import build_profile_text

from schemas.page import Page
from states.profile import ProfileState


async def build_profile_smart_page(user: User = None) -> Page:
    user_id = user.id if user else types.User.get_current().id
    profile = await profiles_service.get_profile(user_id=user_id)
    if not profile:
        return Page(text='Профиль не существует')

    text, parse_mode = build_profile_text(Profile.from_orm(profile))
    reply_markup = build_profile_kb()
    return Page(text=text, parse_mode=parse_mode, reply_markup=reply_markup)


@userdata_required
@dp.message_handler(Command(['profile']))
async def show_user_profile(message: types.Message, user: User):
    page = await build_profile_smart_page(user=user)
    await message.answer(**page.dict())


@dp.callback_query_handler(profile_callback.filter())
async def process_profile_callback(call: types.CallbackQuery, callback_data: dict):
    section = callback_data.get('section')
    match section:
        case 'settings':
            reply_markup = build_profile_settings_kb()
            await call.message.edit_reply_markup(reply_markup=reply_markup)
            await call.answer()
        case 'search_options':
            await call.answer()
        case 'referral_cabinet':
            await call.answer()


@dp.callback_query_handler(profile_settings_callback.filter())
async def process_profile_settings_callback(call: types.CallbackQuery, callback_data: dict):
    section = callback_data.get('section')

    match section:
        case 'age':
            await ProfileState.set_age.set()
            await call.message.edit_text(text='Отправь свой возраст цифрами')
            await call.answer()

        case 'gender':
            await call.message.edit_text(
                text=f'Выберите ваш пол',
                reply_markup=build_profile_settings_set_gender_kb()
            )
            await call.answer()

        case 'country':
            await call.message.edit_text(
                text='Выберите вашу страну',
                reply_markup=await build_profile_settings_set_country_kb()
            )
            await call.answer()

        case 'back':
            # page = await build_profile_smart_page()
            await call.message.edit_reply_markup(reply_markup=build_profile_kb())
            await call.answer()


@dp.callback_query_handler(profile_settings_set_callback.filter())
async def process_profile_settings_set_callback(call: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    data = callback_data.get('data')

    match action:
        case 'set_country':
            profile_update_form = ProfileUpdate(user_id=call.from_user.id, country_id=data)
            updated = await profiles_service.update_profile(profile_update_form)
            if updated:
                await call.answer('Изменения сохранены')

                page = await build_profile_smart_page()
                await call.message.edit_text(**page.dict(exclude_unset=True))
            else:
                await call.answer('Произошла ошибка. Изменения не сохранены', show_alert=True)

        case 'set_gender':
            profile_update_form = ProfileUpdate(user_id=call.from_user.id, gender=data)
            updated = await profiles_service.update_profile(profile_update_form)
            if updated:
                await call.answer('Изменения сохранены')
                page = await build_profile_smart_page()
                await call.message.edit_text(**page.dict())
            else:
                await call.answer('Произошла ошибка. Изменения не сохранены', show_alert=True)

        case 'back':
            page = await build_profile_smart_page()
            await call.message.edit_text(**page.dict())
            await call.answer()


@dp.message_handler(state=ProfileState.set_age)
async def process_profile_settings_set_age(message: types.Message, state: FSMContext):
    age = message.text.strip()
    if not age.isdigit():
        return await message.answer('Возраст необходимо отправить только цифрами')
    age = int(age)
    if 6 >= age >= 90:
        return await message.answer('Некорректный возраст')
    await state.reset_state(with_data=False)

    profile_update_form = ProfileUpdate(user_id=message.from_user.id, age=age)
    updated = await profiles_service.update_profile(profile_update_form)
    if updated:
        await message.answer('Изменения сохранены')
        page = await build_profile_smart_page()
        await message.answer(**page.dict())
    else:
        await message.answer('Произошла ошибка. Изменения не сохранены')
