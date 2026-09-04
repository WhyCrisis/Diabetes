#Логика взята из конструктора из моего проекта, и что ты мне сделаешь а?
#Думаю что тут буду хранить логику SQlite что бы быстрее к ней обращаться, а основное будет лежать в PG
import sqlite3
from argparse import Action

import aiosqlite
from aiogram import Router

#----
router = Router()
#-----

DB_name = "users.db"
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

async def add_user(id_user, language):
    async with aiosqlite.connect(DB_name) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (id_user, language) VALUES (?, ?)",
            (id_user, language)
        )
        await db.commit()

async def get_user_anket():
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

async def get_user_language(user_id):
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("SELECT language FROM users WHERE id_user = ? LIMIT 1", (user_id,)) as cursor:
            result = await cursor.fetchone()
            if result is None:
                return None
            return result[0]



#Админские команды

DB_name_2="log_admin"

#-----Использование базы users-------------

async def delete_user():
    async with aiosqlite.connect(DB_name) as db:
        cursor = await db.execute("DROP TABLE users ")
        await db.commit()

async def spam():
    async with aiosqlite.connect(DB_name) as db:
            async with db.execute("SELECT id_user FROM users ") as cursor:
                result = await cursor.fetchall()
                return result

async def admins():
    async with aiosqlite.connect(DB_name_2) as db:
        query = (
            "CREATE TABLE IF NOT EXISTS admins ("
            "id_user INT UNIQUE, "
            "role TEXT(20),"
            "assigned_at timestamp DEFAULT CURRENT_TIMESTAMP,"
            "assigned_by TEXT(20) )"
        )
        await db.execute(query)
        await db.commit()
        return []

#Использование (статистика) для админского окна
async def get_stats_last_join():
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("SELECT joinAT FROM users ORDER BY joinAT DESC LIMIT 1;") as cursor:
            result = await cursor.fetchone()
            return result[0] if result else None

async def get_stats_user_count():
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("SELECT COUNT(id_user) FROM users;") as cursor:
            result = await cursor.fetchall()
            return result[0][0] if result else None

async def get_stats_user_language():
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("SELECT language, COUNT(*) as total FROM users GROUP BY language ORDER BY total DESC LIMIT 1;") as cursor:
            result = await cursor.fetchone()
            return result[0] if result else None


#-------------------------------------------КОНЕЦ


#-----Использование базы admins--------------

async def log_admin():
    async with aiosqlite.connect(DB_name_2) as db:
        query = (
            "CREATE TABLE IF NOT EXISTS admins_logs ("
            "id_user INT UNIQUE, "
            "action TEXT,"
            "Time timestamp DEFAULT CURRENT_TIMESTAMP )"
        )
        await db.execute(query)
        await db.commit()

async def do_admin(id_user, action):
    async with aiosqlite.connect(DB_name_2) as db:
        await db.execute(
            "INSERT OR IGNORE INTO admins_logs (id_user, action) VALUES (?, ?)",
            (id_user, action)
        )
        await db.commit()

async def see_admin():
    async with aiosqlite.connect(DB_name_2) as db:
        async with db.execute("select * from admins_logs;") as cursor:
            result = await cursor.fetchall()
            if not result:
                return None
            return result
#-------------------------------------------КОНЕЦ