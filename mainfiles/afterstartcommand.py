#----
from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import (Message,ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           CallbackQuery,
                           FSInputFile
                           )
from aiogram.types import ReplyKeyboardRemove
from construct.keyboards import choose_language
from aiogram.fsm.context import FSMContext



#----
#Databases
from databases.database_SQlite import log_start, add_user, get_user_anket

#----
router = Router()
#----



@router.message(Command('start'))
async def start(message: Message):

    #Главное не забыть запустить бд
    await log_start()

    #Тут старт фсм должен быть и сохранение данных (потом передача в SQ)
    #надо бы найти конец, я думаю до главного экрана(?)
    #есть ли толк его делать вообще или хватит только старта?


    #даем выбор языка
    await message.answer(
        text=(
            "<i>Hello!</i>\n"
            "Lets get started with basic settings!\n\n"
            "<b>First</b>..what language do you perform more? Choose it from below"
        ),
            parse_mode='HTML',
            reply_markup=choose_language())


@router.callback_query(F.data.in_({"ru", "en", "es", "ua"}))
async def process_any_language(callback: CallbackQuery):

    #Захватили ответ
    user_id = callback.from_user.id
    language = callback.data

    await callback.answer()
    await add_user(user_id,language)

    # Удаляем старое сообщение пишем новое
    await callback.message.delete()

    await callback.message.answer(f"You selected: {language}")

mainfiles/afterstartcommand.py
#Временная заглушка, перенесу чуть позже!!!
@router.message(Command('alo'))
async def help(message: Message):
    users = await get_user_anket()
    text = 'Созданные анкеты:\n\n'
    for user in users:
        text += f"Айди: {user[0]} | Язык: {user[1]} | Штамп: {user[2]}\n"
    await message.answer(text)

