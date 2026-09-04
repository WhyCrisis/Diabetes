#----
from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
#----
router = Router()
#----

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
    with open("language_pack/languages_pack.json", "r", encoding="utf-8") as f:
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
        inline_keyboard= [
            [InlineKeyboardButton(text='♻️RESTART♻️', callback_data='restart')]
        ]
    )
    return keyboard

def hard_reset():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard= [
            [InlineKeyboardButton(text='♻️DELETE♻️', callback_data='delete')]
        ]
    )
    return keyboard

def fast_admin_things():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard= [
            [InlineKeyboardButton(text='⛔️Drop Database⛔️', callback_data="drop")],
            [InlineKeyboardButton(text='🗑Delete user🗑', callback_data="delete_user")],
            [InlineKeyboardButton(text='🛡Ban user🛡', callback_data="permban")],
            [InlineKeyboardButton(text='📩Send message to user or users📩', callback_data="send_message")]
        ]
    )
    return keyboard

def delete_db():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard= [
            [InlineKeyboardButton(text='✅I know what am i doing✅', callback_data="drop_admin")],
            [InlineKeyboardButton(text='⛔️Back⛔️', callback_data="back_to_admin")]
        ]
    )
    return keyboard