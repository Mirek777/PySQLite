import funcSql

# приветствие
if __name__ == '__main__':
    funcSql.print_hi("Alex")

# создание базы данных
connection = funcSql.create_connection("D:\\sm_app.sqlite")

# создание таблиц
funcSql.create_table_user(connection)
funcSql.create_table_posts(connection)
funcSql.create_table_comments(connection)
funcSql.create_table_likes(connection)
funcSql.create_data_users(connection)
funcSql.create_data_comments(connection)
funcSql.create_data_posts(connection)
funcSql.create_data_likes(connection)
