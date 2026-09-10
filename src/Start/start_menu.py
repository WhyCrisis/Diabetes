#----
import json
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (Message,CallbackQuery)
from aiogram.fsm.context import FSMContext
import os
import json
#----
#Databases
from src.Start.start_SQL import log_start, add_user, get_user_language
#----
#Keyboards
from src.Start.start_keyboard import choose_language,get_rules_keyboard
from src.Menu.menu_main import launch_menu
#----
#FSM
from src.Start.start_FSM import Form
#----
router = Router()
#----

#----
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "start_language.json")
with open(json_path, "r", encoding="utf-8") as f:
    TRANSLATIONS = json.load(f)

def get_text(lang: str, key: str):
    return TRANSLATIONS.get(lang, {}).get(key, key)
#----
@router.callback_query(F.data == 'restart')
async def process_restart(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    await start(callback.message)

@router.message(Command('start'))
async def start(message: Message, state: FSMContext):

    await log_start()
    user_id = message.from_user.id
    lang = await get_user_language(user_id)

    if lang is None:
        # Главное не забыть запустить бд
        await state.clear()
        await state.set_state(Form.lang)
        # даем выбор языка
        await message.answer(
            text=(
                "<i>Hello!</i>\n"
                "Lets get started with basic settings!\n\n"
                "<b>First</b>..what language do you perform more? Choose it from below"
            ),
            parse_mode='HTML',
            reply_markup=choose_language())
    else:
        await launch_menu(message, user_id)


@router.callback_query(F.data.in_({"ru", "en", "es", "ua"}))
async def process_any_language(callback: CallbackQuery, state: FSMContext):

    #Захватили ответ
    language = callback.data[-2:]
    await state.update_data(lang=language)

    #Сохранили ответ
    await callback.answer()

    # Удаляем старое сообщение пишем новое
    await callback.message.delete()

    keyboard = get_rules_keyboard(language)
    text = get_text(language, "selected_lang")

    await callback.message.answer(text,reply_markup=keyboard)


@router.callback_query(F.data.startswith('agree_'))
async def process_agree(callback: CallbackQuery, state: FSMContext):

    data = await state.get_data()
    user_id = callback.from_user.id
    language = data['lang']
    #Передаем в БД
    await add_user(user_id, language)
    #Вызываем главное меню на нужном языке удалив прошлое окно
    await state.clear()
    await callback.answer()
    await callback.message.delete()
    await launch_menu(callback.message, user_id)


@router.callback_query(F.data=='cancel')
async def process_cancel(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await start(callback.message, state)

