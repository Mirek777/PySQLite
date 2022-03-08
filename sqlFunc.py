import sqlite3
from sqlite3 import Error
import sqlQueryCreate
import sqlQueryAddData
import sqlQueryRead

# ___Обшие___


# печать приветствия
def print_hi(name):
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# ___SQL___

# запуск сервера
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successfull")
    except Error as e:
        print(f"The error '{e} occurred")
    return connection


# общая функция для формирование таблиц
def excecute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query excecuted successfuly")
    except Error as e:
        print(f"The error '{e} occured")


# ___SQL Создание таблиц___

# функция для создания таблицы юзеров
def create_table_user(conn):
    excecute_query(conn, sqlQueryCreate.create_users_table)


# функция для создания таблицы постов
def create_table_posts(conn):
    excecute_query(conn, sqlQueryCreate.create_posts_table)


# функция для создания таблицы комментариев
def create_table_comments(conn):
    excecute_query(conn, sqlQueryCreate.create_comments_table)


# функция для создания таблицы лайков
def create_table_likes(conn):
    excecute_query(conn, sqlQueryCreate.create_likes_table)


# ___SQL Добавление данных___

# функция для добавления данных в таблицу юзеров
def create_data_users(conn):
    excecute_query(conn, sqlQueryAddData.create_users)


# функция для добавления данных в таблицу постов
def create_data_posts(conn):
    excecute_query(conn, sqlQueryAddData.create_posts)


# функция для добавления данных в таблицу комментариев
def create_data_comments(conn):
    excecute_query(conn, sqlQueryAddData.create_comments)


# функция для добавления данных в таблицу лайков
def create_data_likes(conn):
    excecute_query(conn, sqlQueryAddData.create_likes)


# ___SQL Извлечение данных___

# общая функция извлечения данных
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# функция извлечения данных из таблицы всех юзеров
def read_table_users(conn):
    users = execute_read_query(conn, sqlQueryRead.select_users)
    for user in users:
        print(user)


# функция извлечения данных из таблицы всех постов
def read_table_posts(conn):
    posts = execute_read_query(conn, sqlQueryRead.select_posts)
    for post in posts:
        print(post)
