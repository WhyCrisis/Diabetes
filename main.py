#---

from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

#---
from mainfiles.afterstartcommand import router as starter_router
from construct.keyboards import router as constructor_router
from databases.database_SQlite import router as database_router
#---

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

#---

#---
#подключение новых роутеров.
dp = Dispatcher()
dp.include_router(starter_router)
dp.include_router(constructor_router)
dp.include_router(database_router)

#---

#---инициализация
async def main():
    bot = Bot(token=TOKEN)
    print("Запущено")
    await dp.start_polling(bot)
#---
if __name__ == '__main__':
    asyncio.run(main())