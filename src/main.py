from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
#---
from src.mainfiles.admin_commands import router as admin_router
from src.Start.start_menu import router as starter_router
from src.construct.keyboards import router as constructor_router
from src.databases.database_SQlite import router as database_router, log_start
from src.mainfiles.main_menu import router as menu_router
#---
load_dotenv()
TOKEN = getenv("BOT_TOKEN")
DB_name = "DB_start"
#---

#---
#подключение новых роутеров
dp = Dispatcher()
dp.include_router(admin_router)
dp.include_router(starter_router)
dp.include_router(constructor_router)
dp.include_router(database_router)
dp.include_router(menu_router)
#---

#---инициализация
async def main():
    bot = Bot(token=TOKEN)
    print("Запущено")
    await log_start()
    await dp.start_polling(bot)

#---
if __name__ == '__main__':
    asyncio.run(main())