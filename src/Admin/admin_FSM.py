from aiogram.fsm.state import StatesGroup, State

class Delete(StatesGroup):
    id_user = State()