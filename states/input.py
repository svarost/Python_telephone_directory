from aiogram.dispatcher.filters.state import StatesGroup, State


class InputContactForm(StatesGroup):
    last_name = State()
    name = State()
    tel_number = State()
    notion = State()