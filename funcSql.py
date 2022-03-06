import sqlite3
from sqlite3 import Error
import querySql
import addSqlData

# печать приветствия
def print_hi(name):
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.

# запуск сервера
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successfull")
    except Error as e:
        print(f"The error '{e} occurred")
    return connection

# функция для формирование таблиц
def excecute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query excecuted successfuly")
    except Error as e:
        print(f"The error '{e} occured")

# функция для создания таблицы юзеров
def create_table_user(conn):
    excecute_query(conn, querySql.create_users_table)

# функция для создания таблицы постов
def create_table_posts(conn):
    excecute_query(conn, querySql.create_posts_table)

# функция для создания таблицы комментариев
def create_table_comments(conn):
    excecute_query(conn, querySql.create_comments_table)

# функция для создания таблицы лайков
def create_table_likes(conn):
    excecute_query(conn, querySql.create_likes_table)

# функция для добавления данных в таблицу юзеров
def create_data_users(conn):
    excecute_query(conn, addSqlData.create_users)

# функция для добавления данных в таблицу постов
def create_data_posts(conn):
    excecute_query(conn, addSqlData.create_posts)

# функция для добавления данных в таблицу комментариев
def create_data_comments(conn):
    excecute_query(conn, addSqlData.create_comments)

# функция для добавления данных в таблицу лайков
def create_data_likes(conn):
    excecute_query(conn, addSqlData.create_likes)
