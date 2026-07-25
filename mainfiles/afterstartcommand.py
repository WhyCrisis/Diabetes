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
#FSM class
from construct.FSMforms import Start
#----


#----
router = Router()
#----


#Стартуем фсм для записи и передачи в SQL



@router.message(Command('start'))
async def start(state: FSMContext, message: Message):
    iduser=message.from_user.id
    await state.update_data(user=iduser)
    await message.answer(
        text=(
            "<i>Hello!</i>\n"
            "Lets get started with basic settings!\n\n"
            "<b>First</b>..what language do you perform more? Choose it from below"
        ),
            parse_mode='HTML',
            reply_markup=choose_language())

