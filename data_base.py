from tkinter import *
import sqlite3

root = Tk()
root.title("data_base")

# create or connect to database

con = sqlite3.connect("address_book.db")

# create cursor
curs = con.cursor()

# create table
'''
curs.execute("""CREATE TABLE addresses(
            first_name text, 
            last_name text,
            address text,
            city text,
            state text,
            zip_code integer
            )""")
'''

# create text box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zip_code = Entry(root, width=30)
zip_code.grid(row=5, column=1)

# text box label
fnl = Label(root, text="First name")
fnl.grid(row=0, column=0)

lnl = Label(root, text="Last name")
lnl.grid(row=1, column=0)

al = Label(root, text="address")
al.grid(row=2, column=0)

cl = Label(root, text="City")
cl.grid(row=3, column=0)

sl = Label(root, text="State")
sl.grid(row=4, column=0)

zcl = Label(root, text="Zipe_code")
zcl.grid(row=5, column=0)


# Submit button


def submit():
    global curs, con
    # create or connect to database
    con = sqlite3.connect("address_book.db")

    # create cursor
    curs = con.cursor()

    # commit changes
    con.commit()

    # close connection
    con.close()

    # insert into the table
    curs.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zip_code)",
                 {
                     'f_name': f_name.get(),
                     'l_name': l_name.get(),
                     'address': address.get(),
                     'city': city.get(),
                     'state': state.get(),
                     'zip_code': zip_code.get()
                 })

    # clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    zip_code.delete(0, END)
    state.delete(0, END)
    city.delete(0, END)


submit_button = Button(root, text="Add record to data_base", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# commit changes
con.commit()

# close connection
con.close()

root.mainloop()
