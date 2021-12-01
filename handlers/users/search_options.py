from aiogram import types
from aiogram.dispatcher.filters import Command

from database.models.search_options import SearchOptions
from keyboards.inline.search_options import build_search_options_kb, search_options_set_callback, \
    build_search_options_set_gender_kb, search_options_callback, build_search_options_set_country_kb, \
    build_search_options_age_kb, search_options_age_callback, \
    build_search_options_set_from_age_kb, build_search_options_set_to_age_kb, search_options_age_set_callback
from loader import dp
from pages.text import build_search_options_text
from schemas.page import Page


async def build_search_options_smart_page() -> Page:
    search_options = await SearchOptions.get_current_search_options()
    await search_options.fetch_related('country')

    text, parse_mode = build_search_options_text(search_options)
    reply_markup = build_search_options_kb()
    return Page(text=text, parse_mode=parse_mode, reply_markup=reply_markup)


@dp.message_handler(Command(['search_options']))
async def show_search_options(message: types.Message):
    search_options_page = await build_search_options_smart_page()
    return await message.answer(**search_options_page.dict(exclude_unset=True))


@dp.callback_query_handler(search_options_callback.filter())
async def process_search_options_callbacks(call: types.CallbackQuery, callback_data: dict):
    section = callback_data.get('section')

    if section == 'age':
        await call.message.edit_text(
            text='Здесь можете указать предпочитаемый возраст собеседника',
            reply_markup=build_search_options_age_kb())
        await call.answer()

    if section == 'gender':
        await call.message.edit_text(
            text='Выберите предпочитаемый пол собеседника',
            reply_markup=build_search_options_set_gender_kb())
        await call.answer()

    if section == 'country':
        await call.message.edit_text(
            text='Выберите предпочитаемую страну собеседника',
            reply_markup=await build_search_options_set_country_kb())
        await call.answer()


@dp.callback_query_handler(search_options_set_callback.filter())
async def process_search_options_set_callback(call: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    data = callback_data.get('data')
    processed = None

    if action == 'set_country':
        options = await SearchOptions.get_current_search_options()
        processed = await options.set_country(country_id=data)

    if action == 'reset_country':
        options = await SearchOptions.get_current_search_options()
        processed = await options.reset_country()

    if action == 'set_gender':
        options = await SearchOptions.get_current_search_options()
        processed = await options.set_gender(gender=data)

    if action == 'reset_gender':
        options = await SearchOptions.get_current_search_options()
        processed = await options.reset_gender()

    if action == 'back':
        page = await build_search_options_smart_page()
        await call.message.edit_text(**page.dict())

    if processed:
        await call.answer('Изменения сохранены')
        page = await build_search_options_smart_page()
        await call.message.edit_text(**page.dict())


@dp.callback_query_handler(search_options_age_callback.filter())
async def process_search_options_age_callback(call: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    processed = None

    if action == 'from_age':
        await call.answer()
        await call.message.edit_text(
            text='Укажите минимальный возраст собседеника',
            reply_markup=build_search_options_set_from_age_kb())
    if action == 'to_age':
        await call.answer()
        await call.message.edit_text(
            text='Укажите максимальный возраст собеседника',
            reply_markup=build_search_options_set_to_age_kb())

    if action == 'reset_age':
        options = await SearchOptions.get_current_search_options()
        processed = all([
            await options.reset_from_age(),
            await options.reset_to_age()
        ])
    if action == 'back':
        processed = True

    if processed:
        await call.answer('Изменения сохранены')
        page = await build_search_options_smart_page()
        await call.message.edit_text(**page.dict())


@dp.callback_query_handler(search_options_age_set_callback.filter())
async def process_search_options_age_set_callback(call: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    data = callback_data.get('data')
    processed = None

    if action == 'set_from_age':
        options = await SearchOptions.get_current_search_options()
        processed = await options.set_from_age(from_age=int(data))
    if action == 'reset_from_age':
        options = await SearchOptions.get_current_search_options()
        processed = await options.reset_from_age()

    if action == 'set_to_age':
        options = await SearchOptions.get_current_search_options()
        processed = await options.set_to_age(to_age=int(data))
    if action == 'reset_to_age':
        options = await SearchOptions.get_current_search_options()
        processed = await options.reset_to_age()

    if action == 'back':
        await call.answer()
        await call.message.edit_text(
            text='Здесь можете указать предпочитаемый возраст собеседника',
            reply_markup=build_search_options_age_kb())
        return

    if processed:
        await call.answer('Изменения сохранены')
        page = await build_search_options_smart_page()
        await call.message.edit_text(**page.dict())
