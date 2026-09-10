#-----
from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
#-----

def fast_admin_things():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard= [
            [InlineKeyboardButton(text='⛔️Drop Database⛔️', callback_data="drop")],
            [InlineKeyboardButton(text='🗑Delete user🗑', callback_data="delete_user")],
            [InlineKeyboardButton(text='📑See admin logs📑', callback_data="show_admin_logs")],
            [InlineKeyboardButton(text='📩Add AD📩', callback_data="add_ad")]
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

def delete_users():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard= [
            [InlineKeyboardButton(text='✅I know what am i doing✅', callback_data="drop_user")],
            [InlineKeyboardButton(text='⛔️Back⛔️', callback_data="back_to_admin")]
        ]
    )
    return keyboard

def back_to_admin():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard= [
            [InlineKeyboardButton(text='⛔️Back⛔️', callback_data="back_to_admin")]
        ]
    )
    return keyboard