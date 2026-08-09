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
#keyboards
from construct.keyboards import back_if_broken
#----
with open("language_pack/languages_pack.json", "r", encoding="utf-8") as f:
    TRANSLATIONS = json.load(f)
def get_text(lang: str, key: str):
    return TRANSLATIONS.get(lang, {}).get(key, key)
#----
router = Router()
#----


async def launch_menu(message:Message, user_id: int):
    language = await get_user_language(user_id)

    if language is None:
        await message.answer(
            text=(
                "Sorry! We can't find your language preferences! \n"
                "Please restart the bot using button below!\n"
                ),
                parse_mode = 'HTML',
                reply_markup =back_if_broken())
        return

    text = get_text(language, 'main_menu_lang')
    await message.answer(text, parse_mode='HTML')

    








