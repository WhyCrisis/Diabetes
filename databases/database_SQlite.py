#Логика взята из конструктора из моего проекта, и что ты мне сделаешь а?
#Думаю что тут буду хранить логику SQlite что бы быстрее к ней обращаться, а основное будет лежать в PG
import aiosqlite
from aiogram import Router

#----
router = Router()
#-----

DB_name = "DB_start"
async def log_start():
    async with aiosqlite.connect(DB_name) as db:
        query = (
            "CREATE TABLE IF NOT EXISTS users ("
            "id_user INT UNIQUE, "
            "language TEXT,"
            "joinAT timestamp DEFAULT CURRENT_TIMESTAMP"
        )
        await db.execute(query)

async def add_user(id_user, language):
    async with aiosqlite.connect(DB_name) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (id_user, language) VALUES (?, ?)",
            (id_user, language)
        )
        await db.commit()
