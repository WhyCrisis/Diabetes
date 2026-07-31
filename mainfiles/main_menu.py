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
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json

#----
#Databases
from databases.database_SQlite import get_user_language
#----
#----
router = Router()
#----

@router.callback_query(F.data.startswith('agree_'))
async def main_menu(callback: CallbackQuery):
    #хватаем айди из кнопки
    user_id = callback.from_user.id
    user_lang = get_user_language(user_id)
    print(user_lang)









