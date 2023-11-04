import mysql.connector

my_new_database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Kapsabet',
    port='3306',
    database='python_connection'
)
my_cursor = my_new_database.cursor()

my_cursor.execute("SELECT * FROM data_sql")

users = my_cursor.fetchall()

for user in users:
    print(user)