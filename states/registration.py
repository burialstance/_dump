from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationState(StatesGroup):
    set_age = State()