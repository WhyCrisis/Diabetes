#----
from os import getenv
from aiogram import Router, F, Bot
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
from databases.database_SQlite import get_user_anket, delete_user

#----
#Keyboards
from construct.keyboards import choose_language,get_rules_keyboard,hard_reset
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


@router.callback_query(F.data == 'DELETE')
async def asdads(callback: CallbackQuery):
    await callback.answer()
    await delete_user()
    await callback.message.answer('deleted')

@router.message(Command('admin_menu_with_things'))
async def admin_menu_with_things(message: Message):
    if F.from_user.id != auid:
        await message.answer('Access Denied')
        return

    else:

        text =(f''
               f'Diabetes bot\n'
               f'-------------------------\n\n\n'
               f'Привет\n. Общая сводка:\n'
               f'Количество пользователей:<b>{}</b>\n'
               f'Популярный язык:<b>{}</b>\n'
               f'Последняя регистрация:<b>{}</b>\n')