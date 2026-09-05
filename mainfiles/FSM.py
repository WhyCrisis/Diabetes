from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    lang = State()

class Delete(StatesGroup):
    user_id = State()
