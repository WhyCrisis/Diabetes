#---
from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client import bot
from dotenv import load_dotenv
import aiosqlite
#---
from mainfiles.afterstartcommand import router as starter_router
from construct.keyboards import router as constructor_router
from databases.database_SQlite import router as database_router
from mainfiles.main_menu import router as menu_router
#---

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
DB_name = "DB_start"
#---

#---
#подключение новых роутеров
dp = Dispatcher()
dp.include_router(starter_router)
dp.include_router(constructor_router)
dp.include_router(database_router)
dp.include_router(menu_router)
#---
#---рассылка
async def if_restart_db():
    async with aiosqlite.connect(DB_name) as db:
        cursor = await db.execute("SELECT id_user FROM users ")
        users = await cursor.fetchall()
        return users

async def sending(bot: Bot):
    users = await if_restart_db()
    for user in users:
        user_id = user[0]
        try:
            await bot.send_message(user_id, "Restart needed! Please use /restart command to restart")
            await asyncio.sleep(1)
        except Exception as e:
            print(f'Не удалось отправить сообщение некоторым пользователям: {user_id}')



#---инициализация
async def main():
    bot = Bot(token=TOKEN)
    print("Запущено")

    await if_restart_db()
    await sending(bot)

    await dp.start_polling(bot)
#---
if __name__ == '__main__':
    asyncio.run(main())