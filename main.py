import sqlFunc

# приветствие
if __name__ == '__main__':
    sqlFunc.print_hi("Alex")

# создание базы данных
connection = sqlFunc.create_connection("D:\\sm_app.sqlite")

# создание таблиц
# sqlFunc.create_table_user(connection)
# sqlFunc.create_table_posts(connection)
# sqlFunc.create_table_comments(connection)
# sqlFunc.create_table_likes(connection)

# заполнение данными
# sqlFunc.create_data_users(connection)
# sqlFunc.create_data_comments(connection)
# sqlFunc.create_data_posts(connection)
# sqlFunc.create_data_likes(connection)

# чтение данных
sqlFunc.read_table_users(connection)
print("")
sqlFunc.read_table_posts(connection)
