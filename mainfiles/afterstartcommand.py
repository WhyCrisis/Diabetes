#----
import json
import sqlite3

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (Message,CallbackQuery)

from aiogram.fsm.context import FSMContext
#----
#Databases
from databases.database_SQlite import log_start, add_user, get_user_anket, delete_user, get_user_language

#----
#Keyboards
from construct.keyboards import choose_language,get_rules_keyboard,hard_reset
from mainfiles import main_menu
#----
#FSM
from mainfiles.FSM import Form
#----
router = Router()
#----

#----
with open("language_pack/languages_pack.json", "r", encoding="utf-8") as f:
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
        await main_menu.launch_menu(message, user_id)


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
    await main_menu.launch_menu(callback.message, user_id)


@router.callback_query(F.data=='cancel')
async def process_cancel(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await start(callback.message, state)

#Временная заглушка, перенесу чуть позже!!!
@router.message(Command('alo'))
async def help(message: Message):
        users = await get_user_anket()

        if not users:
            await message.answer('База пустая')
            return

        text = 'Текущие пользователи:\n\n'
        for user in users:
            text += f"Айди: {user[0]} | Язык: {user[1]} | Штамп: {user[2]}\n"
        await message.answer(text,reply_markup=hard_reset())


@router.callback_query(F.data == 'DELETE')
async def asdads(callback: CallbackQuery):
    await callback.answer()
    await delete_user()
    await callback.message.answer('deleted')
