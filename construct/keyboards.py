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
#----
router = Router()
#----

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def choose_language():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="English 🇺🇸", callback_data="lang_en"),
            InlineKeyboardButton(text="Русский 🇷🇺", callback_data="lang_ru")
        ],
        [
            InlineKeyboardButton(text="Espanol 🇪🇸", callback_data="lang_es"),
            InlineKeyboardButton(text="Українська 🇺🇦", callback_data="lang_ua")
        ]
    ])
    return keyboard