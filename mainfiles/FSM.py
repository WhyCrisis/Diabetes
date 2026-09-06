from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    lang = State()

class Delete(StatesGroup):
    id_user = State()

