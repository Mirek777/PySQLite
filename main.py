import funcSQLite

# приветствие
if __name__ == '__main__':
    funcSQLite.print_hi("Alex")

# создание базы данных
connection = funcSQLite.create_connection("D:\\sm_app.sqlite")

# создание таблиц
funcSQLite.create_table_user(connection)
funcSQLite.create_table_posts(connection)
funcSQLite.create_table_comments(connection)
funcSQLite.create_table_likes(connection)
