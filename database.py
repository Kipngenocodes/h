from tkinter import *
import sqlite3 as mydatabsemanager

# creating tkinter window.
root = Tk()
# assigning title to tkinter window.
root.title("Welcome to Database Manager")
# assigning dimension to tkinter window.
root.geometry("500x500")

# create a database or connect to existing one.
connexion = mydatabsemanager.connect("MyadressBook.db")

# creation of cursor which allows us to send command to database  to do something.
mycursor = connexion.cursor()

# creating tables in database
'''
mycursor.execute(""" CREATE TABLE adresses (
    First_name text,
    Second_name text,
    adress text,
    city text,
    state text,
    zip_code integer
)

""")
'''


# creation of a commit to changes we are making to a database.
connexion.commit()

# closing the  connection upon completing using the database.
connexion.close()
#running tkinter mainloop
root.mainloop()
