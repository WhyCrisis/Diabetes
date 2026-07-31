from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    id = State()
    lang = State()


