from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    lang = State()

class Ban_form(StatesGroup):
    id_admin = State()
    id_user = State()
    reason = State()

class UnBan_form(StatesGroup):
    id_user_unban = State()
