from aiogram.dispatcher.filters.state import StatesGroup, State


class ProfileState(StatesGroup):
    set_age = State()

