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
router = Router()
#----

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def choose_language():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="English 🇺🇸", callback_data="en"),
            InlineKeyboardButton(text="Русский 🇷🇺", callback_data="ru")
        ],
        [
            InlineKeyboardButton(text="Espanol 🇪🇸", callback_data="es"),
            InlineKeyboardButton(text="Українська 🇺🇦", callback_data="ua")
        ]
    ])
    return keyboard



def get_rules_keyboard(language: str):
    with open("language_pack/languages_start.json", "r", encoding="utf-8") as f:
        rules_data = json.load(f)

    # Если переданного языка нет в файле, берем английский по умолчанию
    lang = language if language in rules_data else "en"
    data = rules_data[lang]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=data["btn_rules"], url=data["rules_url"])],
            [InlineKeyboardButton(text=data["btn_agree"], callback_data=f"agree_menu")],
            [InlineKeyboardButton(text='⬅️Change language⬅️', callback_data="cancel")]
        ]
    )
    return keyboard

def back_if_broken():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=
        [InlineKeyboardButton(text='♻️RESTART♻️', callback_data='restart')])
    return keyboard