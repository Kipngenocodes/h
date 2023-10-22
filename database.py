import sqlite3 as mydatabsemanager
from tkinter import *

# creating tkinter window.
root = Tk()
# assigning title to tkinter window.
root.title("Welcome to Database Manager")
# assigning dimension to tkinter window.
root.geometry("500x500")


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

# creation of a submit function for database
def submit_fun():
    # create a database or connect to existing one.
    connexion = mydatabsemanager.connect("MyadressBook.db")

    # creation of cursor which allows us to send command to database  to do something.
    mycursor = connexion.cursor()

    # insert into table
    mycursor.execute("INSERT INTO adresses VALUES(:f_name,:l_name,:Adress,:City,:State,:zip_code)",
                     {
                         "f_name": f_name.get(),
                         "l_name": l_name.get(),
                         "Adress": address.get(),
                         "City": city.get(),
                         "State": state.get(),
                         "zip_code": zip_code.get()
                     })

    # creation of a commit to changes we are making to a database.
    connexion.commit()

    # closing the  connection upon completing using the database.
    connexion.close()


    # clear text boxes upon completing entering data to allow
    # entering of the other data value  which are upcoming.
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip_code.delete(0, END)

# creation of a query_fun
def query_fun():
    # create a database or connect to existing one.
    connexion = mydatabsemanager.connect("MyadressBook.db")

    # creation of cursor which allows us to send command to database  to do something.
    mycursor = connexion.cursor()

    mycursor.execute("SELECT *,oid FROM adresses")
    # allows fetching from the database
    myresult = mycursor.fetchall()
    # Getting rid of the print results to allow manipulation of the python tuple
    # print(myresult)

    # create variable print_myresult ad equate it to an empty string
    print_myresult=" "

    # creation of a for loop to loop the query
    # elimate so we the index of [0] allow printing of everythhing
    for results in myresult:
        # manipulation of tuples to get different results
        print_myresult += str(results) +"\n"


    # creatiom of a query label

    query_label =Label(root, text=print_myresult, font=12)
    query_label.grid(row=8, column=0, columnspan=2)

    # creation of a commit to changes we are making to a database.
    connexion.commit()

    # closing the  connection upon completing using the database.
    connexion.close()
    return
# creation of the entry widget to get data to database
f_name = Entry(root, width=40)
f_name.grid(row=0, column=1)

l_name = Entry(root, width=40)
l_name.grid(row=1, column=1)

address = Entry(root, width=40)
address.grid(row=2, column=1)

city =Entry(root, width=40)
city.grid(row=3, column=1)

state = Entry(root, width=40)
state.grid(row=4, column=1)

zip_code = Entry(root, width=40)
zip_code.grid(row=5, column=1)

# Creating labels text boxes
f_name_label=Label(root, text="First Name:")
f_name_label.grid(row=0, column=0)

l_name_label=Label(root, text="Last Name:")
l_name_label.grid(row=1, column=0)

address_label=Label(root, text="Address:")
address_label.grid(row=2, column=0)

city_label=Label(root, text="City:")
city_label.grid(row=3, column=0)

state_label=Label(root, text="State:")
state_label.grid(row=4, column=0)

zip_code_label=Label(root, text="Zip Code:")
zip_code_label.grid(row=5, column=0)

# create a submit button
submit=Button(root, text="Add record into the database", command=submit_fun)
submit.grid(row=6, column=0, columnspan=3, padx=10, pady=10, ipadx=5, ipady=5)

# Creation of a query button
query_button= Button(root, text="Show database", command=query_fun)
query_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10, ipadx=137)

# running tkinter mainloop
root.mainloop()
