#---

from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

#---

#---

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

#---

#---
#подключение новых роутеров.
dp = Dispatcher()
#---

#---инициализация
async def main():
    bot = Bot(token=TOKEN)
    print("Запущено")
    await dp.start_polling(bot)
#---
if __name__ == '__main__':
    asyncio.run(main())