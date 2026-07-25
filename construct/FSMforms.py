from aiogram.fsm.state import StatesGroup, State

class Start(StatesGroup):
    user_id = State()
    language = State()
    joinAT = State()