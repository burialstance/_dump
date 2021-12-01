from aiogram import types
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher.storage import FSMContext

from database.models.users import User

from database.services.reg import register_new_user
from database.schemas.profile import ProfileCreate
from database.schemas.user import RegistrationForm, UserCreate
from loader import dp
from keyboards.inline.registration import (
    build_registration_set_country_kb,
    build_registration_set_gender_kb,
    registration_callback
)
from states.registration import RegistrationState
from handlers.users.profile import build_profile_smart_page


@dp.message_handler(Command(['registration']))
async def start_registration(message: types.Message, state: FSMContext, edit_message: bool = False):
    if await User.exists(id=message.from_user.id):
        return await message.answer('Пользователь уже зарегистрирован')

    keyboard = await build_registration_set_country_kb()
    text = 'Регистрация шаг 1 из 3\nВыберите вашу страну'
    if edit_message:
        return await message.edit_text(text=text, reply_markup=keyboard)
    return message.answer(text=text, reply_markup=keyboard)


async def finish_registration(message: types.Message, state: FSMContext, edit_message: bool = False):
    data = await state.get_data()
    current_user = types.User.get_current()
    signup_form = RegistrationForm(
        user=UserCreate(**current_user.to_python()),
        profile=ProfileCreate(
            user_id=current_user.id,
            age=data.get('age'),
            gender=data.get('gender'),
            country=data.get('country')
        ),
        referred_id=data.get('referred_id', None)
    )
    user = await register_new_user(form=signup_form)
    page = await build_profile_smart_page()
    await message.answer(**page.dict(exclude_unset=True))


@dp.callback_query_handler(registration_callback.filter())
async def process_registration_callback(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    action = callback_data.get('action')

    if action == 'set_country':
        await state.update_data({'country_id': callback_data.get('payload')})
        keyboard = build_registration_set_gender_kb()
        await call.message.edit_text(text='Регистрация шаг 2 из 3\nУкажите ваш пол', reply_markup=keyboard)

    if action == 'set_gender':
        await state.update_data({'gender': callback_data.get('payload')})
        await call.message.edit_text(text='Регистрация шаг 3 из 3\nНапиши сколько тебе лет')
        await RegistrationState.set_age.set()


@dp.message_handler(state=RegistrationState.set_age)
async def process_registration_set_age(message: types.Message, state: FSMContext):
    age = message.text.strip()
    if not age.isdigit():
        return await message.answer('Возраст необходимо отправить только цифрами')
    age = int(age)
    if 0 >= age >= 90:
        return await message.answer('Некорректный возраст')

    await state.update_data({'age': age})
    await state.reset_state(with_data=False)
    await finish_registration(message=message, state=state)
