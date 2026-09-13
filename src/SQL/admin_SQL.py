#----
import aiosqlite
import sqlite3
#----

#-----Использование базы log_admin------------
#
#
DB_name_2="log_admin.db" # <--- Использованная база для записи логов действий администрации через меню администрации
DB_name = "users.db" # <--- Использованная база для просмотра юзеров и админского функционала
#
#
#------------------------------------------------------------------------------------------#
#ЛОГ СТАРТ создает базу данных users при жестком сбросе через админское меню
#------------------------------------------------------------------------------------------#
async def get_users_log_start():
    async with aiosqlite.connect(DB_name) as db:
        try:
            async with db.execute("SELECT id_user from users ORDER BY RANDOM() LIMIT 1;") as cursor:
                result = await cursor.fetchone()
                return result

        except sqlite3.OperationalError:
            query = (
                "CREATE TABLE IF NOT EXISTS users ("
                "id_user INT UNIQUE, "
                "language TEXT,"
                "joinAT timestamp DEFAULT CURRENT_TIMESTAMP )"
            )
            await db.execute(query)
            await db.commit()
            return []

async def log_start():
    async with aiosqlite.connect(DB_name) as db:
        query = (
            "CREATE TABLE IF NOT EXISTS users ("
            "id_user INTEGER UNIQUE, "
            "language TEXT, "
            "joinAT DATETIME DEFAULT CURRENT_TIMESTAMP )"
        )
        await db.execute(query)
        await db.commit()
#------------------------------------------------------------------------------------------#
#Запись действия администратора через инициализацию базы данных "admin_logs" и последующая запись
#------------------------------------------------------------------------------------------#
#Работа с базой "admin_logs"
#------------------------------------------------------------------------------------------#
async def log_admins_logs():
    async with aiosqlite.connect(DB_name_2) as db:
        query = (
            "CREATE TABLE IF NOT EXISTS admins_logs ("
            "id_admin INT, "
            "action TEXT,"
            "Time timestamp DEFAULT CURRENT_TIMESTAMP )"
        )
        await db.execute(query)
        await db.commit()

async def see_admin_logs():
    async with aiosqlite.connect(DB_name_2) as db:
        async with db.execute("SELECT * FROM admins_logs;") as cursor:
            result = await cursor.fetchall()
            if not result:
                return None
            return result

async def do_admins_logs(id_admin: int, action: str):
    async with aiosqlite.connect(DB_name_2) as db:
        await db.execute(
            "INSERT INTO admins_logs (id_admin, action) VALUES (?, ?) ON CONFLICT (id_admin, action) DO NOTHING",
            (id_admin, action)
        )
        await db.commit()

async def drop_logs_table():
    try:
        async with aiosqlite.connect(DB_name_2) as db:
            await db.execute("DROP TABLE IF EXISTS admins_logs")
            await db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")

# ------------------------------------------------------------------------------------------#
# Статистика админского окна после команды /get_menu_with_things
# ------------------------------------------------------------------------------------------#
async def get_stats_last_join():
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("SELECT joinAT FROM users ORDER BY joinAT DESC LIMIT 1;") as cursor:
            result = await cursor.fetchone()
            return result[0] if result else None
# Время последней регистрации

async def get_stats_user_count():
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("SELECT COUNT(id_user) FROM users;") as cursor:
            result = await cursor.fetchone()
            return result[0] if result else None
# Количество пользователей (всех) из базы данных

async def get_stats_user_top_language():
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute(
                "SELECT language, COUNT(*) as total FROM users GROUP BY language ORDER BY total DESC LIMIT 1;") as cursor:
            result = await cursor.fetchone()
            return result[0] if result else None
# Получение ТОП популярного языка в БД

# ------------------------------------------------------------------------------------------#
# Удаление базы данных USERS
# ------------------------------------------------------------------------------------------#
async def drop_user_table():
    try:
        async with aiosqlite.connect(DB_name) as db:
            await db.execute("DROP TABLE IF EXISTS users")
            await db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")

#------------------------------------------------------------------------------------------#
#Удаление пользователя из базы данных + проверки
#------------------------------------------------------------------------------------------#
async def check_delete(id_user: int):
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("SELECT * FROM users WHERE id_user = ?", (id_user,)) as cursor:
            result = await cursor.fetchone()
            if not result:
                return None
            return result

async def delete_user(id_user: int):
    async with aiosqlite.connect(DB_name) as db:
        await db.execute("DELETE FROM users WHERE id_user = ?", (id_user,))
        await db.commit()
#------------------------------------------------------------------------------------------#
#
#------------------------------------------------------------------------------------------#
