#----
from os import getenv
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (Message,CallbackQuery)
from dotenv import load_dotenv
#---
load_dotenv()
auid = int(getenv("admin"))
#---
router = Router()
#----
#Databases
from databases.database_SQlite import get_user_anket, delete_user, get_stats_last_join, get_stats_user_language, \
    get_stats_user_count, log_start, log_admin, do_admin, see_admin

#----
#Keyboards
from construct.keyboards import hard_reset, fast_admin_things, delete_db
#----
from mainfiles.FSM import UnBan_form
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

@router.message(Command('alo_admins'))
async def admins_fast_check(message: Message):
        users = await see_admin()
        if not users:
            await message.answer('База пустая')
            return
        text = 'Текущие пользователи:\n\n'
        for user in users:
            text += f"Айди: {user[0]} | Действие: {user[1]} | Штамп: {user[2]}\n"
        await message.answer(text)





@router.message(Command('admin_menu_with_things'))
async def admin_menu_with_things(message: Message):
    if F.from_user.id == auid:
        await log_admin()
        users = await get_stats_user_count()
        top = await get_stats_user_language()
        last = await get_stats_last_join()

        text =(f''
               f'Diabetes bot\n'
               f'-------------------------\n\n\n'
               f'Hi, total count:\n'
               f'Users: <b>{users}</b>\n'
               f'Popular language: <b>{top}</b>\n'
               f'Last registration: <b>{last} GMC +3</b>\n')
        parse_mode = 'HTML'
        reply_markup = fast_admin_things()
        await message.answer(text,parse_mode=parse_mode,reply_markup=reply_markup)
    else:
        message.answer('Denied')

#-----Удаление БД

@router.callback_query(F.data == 'drop')
async def asdads(callback: CallbackQuery):
    text = ('This command is <b>PERMANENT</b>!\nThat means that no undo of that!\nTo proceed push button below')
    parse_mode = 'HTML'
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(text,parse_mode=parse_mode,reply_markup=delete_db())

@router.callback_query(F.data == 'drop_admin')
async def drop_admin(callback: CallbackQuery):

    #---Логирование---
    id_user = callback.from_user.id
    action = 'Database drop'
    await do_admin(id_user, action)
    print(action)
    #---Логирование---

    await callback.answer('Deleted! This action is in log now!', show_alert=True)
    await callback.answer()

    #Удаление и создание новой базы
    await delete_user()
    #Создание
    await log_start()

    await callback.message.delete()
    await admin_menu_with_things(callback.message)

@router.callback_query(F.data == 'back_to_admin')
async def back_admin(callback: CallbackQuery):
    await callback.answer()
    await admin_menu_with_things(callback.message)
    await callback.message.delete()

#----Удаление БД

#----Удаление пользователя

@router.callback_query(F.data == 'delete_user')
async def delete_user(callback: CallbackQuery):

    checking = callback.from_user.id

    if checking != auid:
        await callback.answer()
        await callback.answer('Denied! Connect with main admin!')
        return
    else:
        await callback.answer(delete_user_2(checking))

async def delete_user_2(checking, message: Message):

    if checking == auid:
        await message.answer('Enter the uid of user to unban:')

        id_user = message.from_user

        if id_user != int:
            await message.answer('Enter the valid uid to unban!')
            return




