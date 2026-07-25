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
#Databases
from databases.database_SQlite import log_start, add_user

#----
router = Router()
#----


#Стартуем фсм для записи и передачи в SQL



@router.message(Command('start'))
async def start(state: FSMContext, message: Message):
        #обязательный перезапуск!
        #await state.clear()

    #Главное не забыть запустить бд
    await log_start()

    #Тут старт фсм должен быть и сохранение данных (потом передача в SQ)
    #надо бы найти конец, я думаю до главного экрана(?)
    #есть ли толк его делать вообще или хватит только старта?

    #Запуск фсм
        #iduser=message.from_user.id
        #await state.set_state(Start.user_id)
        #await state.update_data(user=iduser)
    #Закончили запись ID юзера

    #даем выбор языка
    await message.answer(
        text=(
            "<i>Hello!</i>\n"
            "Lets get started with basic settings!\n\n"
            "<b>First</b>..what language do you perform more? Choose it from below"
        ),
            parse_mode='HTML',
            reply_markup=choose_language())


@router.callback_query(F.data.in_({"ru", "en", "es", "ua"}))
async def process_any_language(callback: CallbackQuery, state: FSMContext):

    #Захватили ответ
    user_id = callback.from_user.id
    language = callback.data


    #Передали в ФСМ
        #await state.set_state(Start.language)
    #Сохранили в ФСМ
        #await state.update_data(language=selected_lang)

    #Вытягиваем из ФСМ и передаем в БД
        #user_data = await state.get_data()
        #user_id = user_data.get('user_id')   #айди
        #language = user_data.get('language') #язык
    await add_user(user_id,language)     #передали в бд


    await callback.message.answer(f"You selected: {language}")
    await callback.answer()

