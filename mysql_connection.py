import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kapsabet",
    port="3306",
    database="working_with_pyton"
)

mycursor = mydatabase.cursor()

mycursor.execute("SELECT * FROM users")

users = mycursor.fetchall()

for user in users:
    print(user)