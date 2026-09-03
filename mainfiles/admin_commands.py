#----
from os import getenv
from aiogram import Router, F, Bot
from aiogram.enums import parse_mode
from aiogram.filters import Command
from aiogram.types import (Message,CallbackQuery)
from dotenv import load_dotenv
#---
load_dotenv()
auid = int(getenv("admin"))
print(auid)
#---
router = Router()
#----
#Databases
from databases.database_SQlite import get_user_anket, delete_user, get_stats_last_join, get_stats_user_language, get_stats_user_count

#----
#Keyboards
from construct.keyboards import choose_language,get_rules_keyboard,hard_reset, fast_admin_things, delete_db
#----
router.message.filter(F.from_user.id == auid)
router.callback_query.filter(F.from_user.id == auid)
#----

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


@router.callback_query(F.data == 'drop')
async def asdads(callback: CallbackQuery):
    text = ('This command is <b>PERMANENT</b>!/n That means that no undo of that!/n To proceed push button below')
    parse_mode = 'HTML'
    await callback.answer()
    await message.answer(text,parse_mode=parse_mode,reply_markup=delete_db())


@router.message(Command('admin_menu_with_things'))
async def admin_menu_with_things(message: Message):
    if F.from_user.id == auid:
        users = await get_stats_user_count()
        top = await get_stats_user_language()
        last = await get_stats_last_join()
        text =(f''
               f'Diabetes bot\n'
               f'-------------------------\n\n\n'
               f'Привет. Общая сводка:\n'
               f'Количество пользователей: <b>{users}</b>\n'
               f'Популярный язык: <b>{top}</b>\n'
               f'Последняя регистрация: <b>{last} GMC +3</b>\n')
        parse_mode = 'HTML'
        reply_markup = fast_admin_things()
        await message.answer(text,parse_mode=parse_mode,reply_markup=reply_markup)
    else:
        message.answer('Denied')
