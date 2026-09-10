#Вся логика SQLite лежит в данном файле.
#! Важно к прочтению что, тут строго SQlite!
import sqlite3
import aiosqlite
from aiogram import Router

#----
router = Router()
#-----

#----Использование базы users----------------
#
#
DB_name = "users.db" #<-------- Использована база для сохранения после того как пользователь пройдет первоначальную регистрацию в боте
#
#
async def log_start():
    async with aiosqlite.connect(DB_name) as db:
        query = (
            "CREATE TABLE IF NOT EXISTS users ("
            "id_user INT UNIQUE, "
            "language TEXT,"
            "joinAT timestamp DEFAULT CURRENT_TIMESTAMP )"
        )
        await db.execute(query)
        await db.commit()
#Инициализация базы

async def add_user(id_user: int, language: str):
    async with aiosqlite.connect(DB_name) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (id_user, language) VALUES (?, ?)",
            (id_user, language)
        )
        await db.commit()
#Добавление пользователя в базу после регистрации

async def get_users_log_start():
    async with aiosqlite.connect(DB_name) as db:
        try:
            async with db.execute("SELECT * FROM users ") as cursor:
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
#Используется для того что бы база данных не ложилась при удалении через админскую панель и создавалась снова

async def get_user_language(user_id:int):
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("SELECT language FROM users WHERE id_user = ? LIMIT 1", (user_id,)) as cursor:
            result = await cursor.fetchone()
            if result is None:
                return None
            return result[0]
#Получение имени пользователя из базы для последующей обработки в языковом выборе

#-------------------------------------------КОНЕЦ