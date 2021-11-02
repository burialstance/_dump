from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from loader import dp
from database.enums import CountriesEnum, GendersEnum
from database.services import UserService
from keyboards.inline.registration import (
    build_registration_set_country_kb,
    build_registration_set_gender_kb,
    registration_callback
)
from states.registration import RegistrationState
from handlers.users.profile import build_user_profile_smart_window


async def start_registration(message: types.Message, state: FSMContext, edit_message: bool = False):
    current_telegram_user = types.User.get_current()
    await state.update_data(current_telegram_user.to_python())

    keyboard = build_registration_set_country_kb()
    text = 'Регистрация шаг 1 из 3\nВыберите вашу страну'
    if edit_message:
        return await message.edit_text(text=text, reply_markup=keyboard)
    return message.answer(text=text, reply_markup=keyboard)


async def finish_registration(message: types.Message, state: FSMContext, edit_message: bool = False):
    user_data = await state.get_data()
    user, created = await UserService.register_new_user(**user_data)
    if created:
        window_kwargs = await build_user_profile_smart_window(user)
        return await message.answer(**window_kwargs)
    await message.answer(text=user_data)



# country
@dp.callback_query_handler(registration_callback.filter())
async def process_registration_callback(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    action = callback_data.get('action')

    match action:
        case 'set_country':
            country = callback_data.get('payload')
            if country not in list(CountriesEnum):
                return await call.message.answer('Юный киндер, хватит ковырять сервис')

            await state.update_data({'country': CountriesEnum(country)})
            keyboard = build_registration_set_gender_kb()
            await call.message.edit_text(text='Регистрация шаг 2 из 3\nУкажите ваш пол', reply_markup=keyboard)

        case 'set_gender':
            gender = callback_data.get('payload')
            if gender not in list(GendersEnum):
                return await call.message.answer('Юный киндер, хватит ковырять сервис')

            await state.update_data({'gender': GendersEnum(gender)})
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

