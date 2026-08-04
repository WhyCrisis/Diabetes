#Логика взята из конструктора из моего проекта, и что ты мне сделаешь а?
#Думаю что тут буду хранить логику SQlite что бы быстрее к ней обращаться, а основное будет лежать в PG
import sqlite3
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
            "joinAT timestamp DEFAULT CURRENT_TIMESTAMP )"
        )
        await db.execute(query)

async def add_user(id_user, language):
    async with aiosqlite.connect(DB_name) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (id_user, language) VALUES (?, ?)",
            (id_user, language)
        )
        await db.commit()

#временная заглушка не забыть бы удалить позже
async def get_user_anket():
    async with aiosqlite.connect(DB_name) as db:
        try:
            cursor = await db.execute("SELECT * FROM users ")
            result = await cursor.fetchall()
            return result

        except sqlite3.OperationalError as e:
            query = (
                "CREATE TABLE IF NOT EXISTS users ("
                "id_user INT UNIQUE, "
                "language TEXT,"
                "joinAT timestamp DEFAULT CURRENT_TIMESTAMP )"
            )
            await db.execute(query)
            await db.commit()
            return []

async def get_user_language(user_id):
    async with aiosqlite.connect(DB_name) as db:
        cursor = await db.execute("SELECT language FROM users WHERE id_user = ? LIMIT 1", (user_id,))
        result = await cursor.fetchone()
        if result is None:
            return None
        return result[0]

async def delete_user():
    async with aiosqlite.connect(DB_name) as db:
        cursor = await db.execute("DROP TABLE users ")
        await db.commit()

async def restart():
    async with aiosqlite.connect(DB_name) as db:
            cursor = await db.execute("SELECT id_user FROM users ")
            result = await cursor.fetchall()
            return result