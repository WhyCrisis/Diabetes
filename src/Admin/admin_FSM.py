from aiogram.fsm.state import StatesGroup, State

class Delete(StatesGroup):
    user_id = State()