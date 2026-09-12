from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

#---
from src.Admin.admin_menu import router as admin_router
from src.Start.start_menu import router as start_router
from src.Menu.menu_main import router as menu_router

#---Инициализация БД
from src.Start.start_SQL import log_start

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
DB_name = "DB_start"
#---

#---Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

#подключение новых роутеров
dp.include_router(admin_router)
dp.include_router(start_router)
dp.include_router(menu_router)
#---

#---инициализация
async def main():
    print("Запущено")
    log_start()
    await dp.start_polling(bot)

#---
if __name__ == '__main__':
    asyncio.run(main())