#----
from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
#----

def back_if_broken():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard= [
            [InlineKeyboardButton(text='♻️RESTART♻️', callback_data='restart')]
        ]
    )
    return keyboard
