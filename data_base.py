from tkinter import *
import sqlite3

root = Tk()
root.title("data_base")

# create or connect to database

con = sqlite3.connect("address_book.db")

# create cursor
curs = con.cursor()

# create table

curs.execute("""CREATE TABLE IF NOT EXISTS addresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zip_code integer
            )""")


# create function to delete record


def delete_record():
    global con, curs
    # create or connect to database
    con = sqlite3.connect("address_book.db")

    # create cursor
    curs = con.cursor()

    # Delete a record
    curs.execute("DELETE from addresses WHERE oid=" + delete_box.get())

    # commit changes
    con.commit()

    # close connection
    con.close()


# create text box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, pady=(5, 0))

address = Entry(root, width=30)
address.grid(row=2, column=1, pady=(5, 0))

city = Entry(root, width=30)
city.grid(row=3, column=1, pady=(5, 0))

state = Entry(root, width=30)
state.grid(row=4, column=1, pady=(5, 0))

zip_code = Entry(root, width=30)
zip_code.grid(row=5, column=1, pady=(5, 0))

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# text box label
fnl = Label(root, text="First name")
fnl.grid(row=0, column=0, pady=(10, 0))

lnl = Label(root, text="Last name")
lnl.grid(row=1, column=0, pady=(5, 0))

al = Label(root, text="address")
al.grid(row=2, column=0, pady=(5, 0))

cl = Label(root, text="City")
cl.grid(row=3, column=0, pady=(5, 0))

sl = Label(root, text="State")
sl.grid(row=4, column=0, pady=(5, 0))

zcl = Label(root, text="Zipe_code")
zcl.grid(row=5, column=0, pady=(5, 0))

dbl = Label(root, text="ID number")
dbl.grid(row=9, column=0)


# Submit button


def submit():
    global curs, con
    # create or connect to database
    con = sqlite3.connect("address_book.db")

    # create cursor
    curs = con.cursor()

    # insert into the table
    curs.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zip_code)',
                 {
                     'f_name': f_name.get(),
                     'l_name': l_name.get(),
                     'address': address.get(),
                     'city': city.get(),
                     'state': state.get(),
                     'zip_code': zip_code.get()
                 })

    # commit changes
    con.commit()

    # close connection
    con.close()

    # clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    zip_code.delete(0, END)
    state.delete(0, END)
    city.delete(0, END)


# create query function
def query():
    global curs, con
    # create or connect to database
    con = sqlite3.connect("address_book.db")

    # create cursor
    curs = con.cursor()

    # Query the database
    curs.execute("SELECT *, oid FROM addresses")
    records = curs.fetchall()

    # print(records)
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    # Window for records
    window = Toplevel()
    window.title("Records")

    Label(
        window, text="the record is displayed like this : (First name, Last name, Address, City, Zipe_code, oid)"
    ).pack()
    Label(window, text=print_records).pack()

    # commit changes
    con.commit()

    # close connection
    con.close()


def save():
    global curs, con
    # create or connect to database
    con = sqlite3.connect("address_book.db")

    # create cursor
    curs = con.cursor()

    record_id = delete_box.get()
    curs.execute("""UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zip_code = :zip_code
    
    WHERE oid = :oid""",
                 {"first": f_name_editor.get(),
                  "last": l_name_editor.get(),
                  "address": address_editor.get(),
                  "city": city_editor.get(),
                  "state": state_editor.get(),
                  "zip_code": zip_code_editor.get(),
                  "oid": record_id
                  })

    # commit changes
    con.commit()

    # close connection
    con.close()

    window.destroy()


# Update function
def update_record():

    global window
    window = Tk()
    window.title("Update a record")

    global curs, con
    # create or connect to database
    con = sqlite3.connect("address_book.db")

    # create cursor
    curs = con.cursor()

    record_id = delete_box.get()
    # Query the database
    curs.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = curs.fetchall()

    # create global ver
    global f_name_editor, l_name_editor, address_editor, city_editor, state_editor, zip_code_editor

    # create text box
    f_name_editor = Entry(window, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(window, width=30)
    l_name_editor.grid(row=1, column=1, pady=(5, 0))

    address_editor = Entry(window, width=30)
    address_editor.grid(row=2, column=1, pady=(5, 0))

    city_editor = Entry(window, width=30)
    city_editor.grid(row=3, column=1, pady=(5, 0))

    state_editor = Entry(window, width=30)
    state_editor.grid(row=4, column=1, pady=(5, 0))

    zip_code_editor = Entry(window, width=30)
    zip_code_editor.grid(row=5, column=1, pady=(5, 0))

    # text box label
    fnl_editor = Label(window, text="First name")
    fnl_editor.grid(row=0, column=0, pady=(10, 0))

    lnl_editor = Label(window, text="Last name")
    lnl_editor.grid(row=1, column=0, pady=(5, 0))

    al_editor = Label(window, text="address")
    al_editor.grid(row=2, column=0, pady=(5, 0))

    cl_editor = Label(window, text="City")
    cl_editor.grid(row=3, column=0, pady=(5, 0))

    sl_editor = Label(window, text="State")
    sl_editor.grid(row=4, column=0, pady=(5, 0))

    zcl_editor = Label(window, text="Zipe_code")
    zcl_editor.grid(row=5, column=0, pady=(5, 0))

    save_button = Button(window, text="Add record to data_base", command=save)
    save_button.grid(row=6, column=0, columnspan=2, pady=3, padx=10, ipadx=100)

    # print results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zip_code_editor.insert(0, record[5])


# submit button
submit_button = Button(root, text="Add record to data_base", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=3, padx=10, ipadx=100)

# query button
query_button = Button(root, text="Show records", command=query)
query_button.grid(row=7, columnspan=2, column=0, padx=10, pady=3, ipadx=173)

# Delete button
delete_button = Button(root, text="delete record", command=delete_record)
delete_button.grid(row=10, columnspan=2, column=0, padx=10, pady=3, ipadx=173)

# Update button
update_button = Button(root, text="update record", command=update_record)
update_button.grid(row=11, columnspan=2, column=0, padx=10, pady=3, ipadx=173)

# commit changes
con.commit()

# close connection
con.close()

root.mainloop()

