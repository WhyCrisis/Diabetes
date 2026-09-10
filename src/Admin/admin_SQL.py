#----
import aiosqlite
#----

#-----Использование базы log_admin------------
#
#
DB_name_2="log_admin.db" # <--- Использованная база для записи логов действий администрации через меню администрации
DB_name = "users.db" # <--- Использованная база для просмотора юзеров и админского функционала
#
#
async def log_admin():
    async with aiosqlite.connect(DB_name_2) as db:
        query = (
            "CREATE TABLE IF NOT EXISTS admins_logs ("
            "id_admin INT UNIQUE, "
            "action TEXT,"
            "Time timestamp DEFAULT CURRENT_TIMESTAMP )"
        )
        await db.execute(query)
        await db.commit()
#Создание и запуск базы логирования

async def do_admin(id_user: int, action:str):
    async with aiosqlite.connect(DB_name_2) as db:
        await db.execute(
            "INSERT OR IGNORE INTO admins_logs (id_admin, action) VALUES (?, ?)",
            (id_user, action)
        )
        await db.commit()
#Запись действия администратора

#! ВРЕМЕННАЯ ЗАГЛУШКА ДЛЯ ТЕСТОВ (просмотр логов)
async def see_admin():
    async with aiosqlite.connect(DB_name_2) as db:
        async with db.execute("select * from admins_logs;") as cursor:
            result = await cursor.fetchall()
            if not result:
                return None
            return result
#! ВРЕМЕННАЯ ЗАГЛУШКА ДЛЯ ТЕСТОВ (просмотр логов)


#! ВРЕМЕННАЯ ЗАГЛУШКА УДАЛЕНИЯ ПОЛЬЗОВАТЕЛЕЙ
async def delete_user():
    async with aiosqlite.connect(DB_name) as db:
        cursor = await db.execute("DROP TABLE users ")
        await db.commit()
#! ВРЕМЕННАЯ ЗАГЛУШКА УДАЛЕНИЯ ПОЛЬЗОВАТЕЛЕЙ




#Статистика админского окна

async def get_stats_last_join():
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("SELECT joinAT FROM users ORDER BY joinAT DESC LIMIT 1;") as cursor:
            result = await cursor.fetchone()
            return result[0] if result else None
#Время последней регистрации

async def get_stats_user_count():
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("SELECT COUNT(id_user) FROM users;") as cursor:
            result = await cursor.fetchall()
            return result[0][0] if result else None
#Количество пользователей (всех) из базы данных

async def get_stats_user_top_language():
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("SELECT language, COUNT(*) as total FROM users GROUP BY language ORDER BY total DESC LIMIT 1;") as cursor:
            result = await cursor.fetchone()
            return result[0] if result else None
#Самый популярный язык
#
#
#Проверка на удаление нужного пользователя из админской панели
#
#

async def check_delete(id_user: int):
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("select * from users where id_user = ?", (id_user,)) as cursor:
            result = await cursor.fetchone()
            if not result:
                return None
            return result

async def confirm_delete(id_user: int):
    async with aiosqlite.connect(DB_name) as db:
        async with db.execute("DELETE FROM users where id_user = ?", (id_user,)):
            await db.commit()

#