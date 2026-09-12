# ----
from aiogram import Router
from aiogram.types import (Message
                           )
import os
import json
# ----
# Databases
from SQL.start_SQL import get_user_language
# ----
# keyboards
from src.Menu.main_keyboard import back_if_broken

# ----
#----
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "menu_language.json")
with open(json_path, "r", encoding="utf-8") as f:
    TRANSLATIONS = json.load(f)

def get_text(lang: str, key: str):
    return TRANSLATIONS.get(lang, {}).get(key, key)
#----
# ----
router = Router()


# ----
async def launch_menu(message: Message, user_id: int):
    language = await get_user_language(user_id)

    if language is None:
        await message.answer(
            text=(
                "Sorry! We can't find your language preferences! \n"
                "Please restart the bot using button below!\n"
            ),
            parse_mode='HTML',
            reply_markup=back_if_broken())
        return

    text = get_text(language, 'main_menu_lang')
    await message.answer(text, parse_mode='HTML')










