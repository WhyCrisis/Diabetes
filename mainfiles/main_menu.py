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
with open("language_pack/languages_start.json", "r", encoding="utf-8") as f:
    TRANSLATIONS = json.load(f)
def get_text(lang: str, key: str):
    return TRANSLATIONS.get(lang, {}).get(key, key)
#----
router = Router()
#----



@router.callback_query(F.data.in_({"menu"}))
async def launch_menu(callback: CallbackQuery):
    user_id = callback.from_user.id
    language = await get_user_language(user_id)

    if language is None:
        await callback.message.answer(
            text=(
                'Sorry! We cant find your language preferences! \n'
                'Please restart the bot using button below!\n'
                ),
                ParseMode = 'HTML',
                reply_markup =back_if_broken())

    text = get_text(language, 'main_menu_lang')
    await callback.message.answer(text)

    








