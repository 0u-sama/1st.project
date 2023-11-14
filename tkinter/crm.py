import mysql.connector
from tkinter import *
import csv
from tkinter import ttk, messagebox

# connect to mysql
my_db = mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="0uss4m4",
                                database="db",
                                )

# check to see if connection to mysql was created


# Create a cursor and initialize it
my_cursor = my_db.cursor()

# sql = "DROP TABLE customers"
# my_cursor.execute(sql)

# Create database
my_cursor.execute("CREATE DATABASE IF NOT EXISTS db")
'''
# teste if database was created
# my_cursor.execute("SHOW DATABASES")
# for d in my_cursor:
# print(d)


# Create table
my_cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
                                    first_name VARCHAR(20), 
                                    last_name VARCHAR(20), 
                                    zip_code INT (10), 
                                    price_paid DECIMAL (10, 2), 
                                    user_id INT AUTO_INCREMENT PRIMARY KEY)
                                    """)

# Alter table
my_cursor.execute("""ALTER TABLE customers ADD (
                        user_name VARCHAR(255)

                        
                        )""")


my_cursor.execute("SELECT * FROM customers")

for thing in my_cursor.description:
    print(thing)
'''


# Functions
# Submit function
def submit():
    sql_command = """INSERT INTO customers(
                                    first_name, 
                                    last_name, 
                                    address_1,
                                    address_2,
                                    city,
                                    state,                                    
                                    zip_code, 
                                    country,
                                    phone,
                                    email,
                                    payment_methode,
                                    discount_code,
                                    price_paid,
                                    user_name
                                    ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """

    values = (fn_box.get(),
              ln_box.get(),
              add1_box.get(),
              add2_box.get(),
              cit_box.get(),
              state_box.get(),
              zip_code_box.get(),
              country_box.get(),
              phone_box.get(),
              email_box.get(),
              payment_method_box.get(),
              discount_code_box.get(),
              price_paid_box.get(),
              user_name_box.get()
              )

    my_cursor.execute(sql_command, values)

    # Commit the changes to database
    my_db.commit()

    # Clear fields
    fn_box.delete(0, END)
    ln_box.delete(0, END)
    add1_box.delete(0, END)
    add2_box.delete(0, END)
    cit_box.delete(0, END)
    state_box.delete(0, END)
    zip_code_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    user_name_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)


def write_to_csv(result):
    with open('customers.csv', 'a', newline="") as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)


def list_customers():
    # Checking saved data
    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    up = Tk()
    up.geometry("800x600")
    up.title("list of customers")
    for index, x in enumerate(result):
        num = 0

        for y in x:
            Label(up, text=y).grid(row=index, column=num)
            num += 1
    Button(up, text="save to excel", command=lambda: write_to_csv(result)).grid(row=index + 1, columnspan=14, ipadx=130)


def recherche():
    selected = drop.get()
    sql = ""

    if selected == "user name":
        sql = "SELECT * FROM customers WHERE user_name = %s"
        Label(search_window, text="You searched using user name").grid(row=3, column=0)
    elif selected == "email":
        sql = "SELECT * FROM customers WHERE email = %s"
        Label(search_window, text="You searched using email").grid(row=3, column=0)

    elif selected == "phone number":
        sql = "SELECT * FROM customers WHERE phone = %s"
        Label(search_window, text="You searched using phone number").grid(row=3, column=0)
    elif selected == "customer id":
        sql = "SELECT * FROM customers WHERE user_id = %s"
        Label(search_window, text="You searched using customer id").grid(row=3, column=0)
    else:
        messagebox.showerror("error", "Please select enter a valid info and try again")

    searched = search_box.get()
    # sql = "SELECT * FROM customers WHERE user_name = %s"
    name = (searched,)
    result = my_cursor.execute(sql, name)
    result = my_cursor.fetchall()

    if not result:
        result = "customer not found"
        searched_result = Label(search_window, text=result)
        searched_result.grid(row=4, column=0)
    else:
        for index, x in enumerate(result):
            num = 0
            index += 4
            for y in x:
                searched_result = Label(search_window, text=y)
                searched_result.grid(row=index, column=num)
                num += 1
        Button(search_window, text="save to excel", command=lambda: write_to_csv(result)).grid(row=index + 1, columnspan=14,ipadx=130)


def search():
    global search_box, search_window, drop

    search_window = Tk()
    search_window.geometry("1000x600")
    search_window.title("search for customers")

    # Entry box for search for customer
    search_box = Entry(search_window, width=30)
    search_box.grid(row=1, column=0, padx=10, pady=10)

    # Entry box for search for customer
    Label(search_window, text="Search for customer by ").grid(row=0, column=0, pady=5, padx=5, sticky=W)

    # Search button
    Button(search_window, text="recherche", command=recherche).grid(row=2, padx=10, pady=10, column=0, columnspan=2)

    # Drop down box
    drop = ttk.Combobox(search_window,
                        values=["Search for customer by :", "user name", "email", "phone number", "customer id"],
                        width=30)
    drop.current(0)
    drop.grid(row=0, column=0, pady=5, padx=5, sticky=W)


# creating gui


root = Tk()
root.title("crm")
root.geometry("370x490")

title_label = Label(root, text="Customers Database", font=("Helvetica", 13), fg="#c8bdaf")
title_label.grid(columnspan=2, column=0, row=0, padx=20)

# Create main_form to enter costumer data
fn_label = Label(root, text="First Name")
ln_label = Label(root, text="Last Name")
add1_label = Label(root, text="Address_1")
add2_label = Label(root, text="Address_2")
cit_label = Label(root, text="City")
state_label = Label(root, text="State")
zip_code_label = Label(root, text="Zip Code")
country_label = Label(root, text="Country")
phone_label = Label(root, text="Phone number")
email_label = Label(root, text="Email")
user_name_label = Label(root, text="User Name")
payment_method_label = Label(root, text="Payment Method")
discount_code_label = Label(root, text="Discount Code")
price_paid_label = Label(root, text="Price Paid")

# Putting main_form in the screen
fn_label.grid(row=1, column=0, sticky=W, padx=10)
ln_label.grid(row=2, column=0, sticky=W, padx=10)
add1_label.grid(row=3, column=0, sticky=W, padx=10)
add2_label.grid(row=4, column=0, sticky=W, padx=10)
cit_label.grid(row=5, column=0, sticky=W, padx=10)
state_label.grid(row=6, column=0, sticky=W, padx=10)
zip_code_label.grid(row=7, column=0, sticky=W, padx=10)
country_label.grid(row=8, column=0, sticky=W, padx=10)
phone_label.grid(row=9, column=0, sticky=W, padx=10)
email_label.grid(row=10, column=0, sticky=W, padx=10)
user_name_label.grid(row=11, column=0, sticky=W, padx=10)
payment_method_label.grid(row=12, column=0, sticky=W, padx=10)
discount_code_label.grid(row=13, column=0, sticky=W, padx=10)
price_paid_label.grid(row=14, column=0, sticky=W, padx=10)

# Creating entry box
fn_box = Entry(root, width=30)
ln_box = Entry(root, width=30)
add1_box = Entry(root, width=30)
add2_box = Entry(root, width=30)
cit_box = Entry(root, width=30)
state_box = Entry(root, width=30)
zip_code_box = Entry(root, width=30)
country_box = Entry(root, width=30)
phone_box = Entry(root, width=30)
email_box = Entry(root, width=30)
user_name_box = Entry(root, width=30)
payment_method_box = Entry(root, width=30)
discount_code_box = Entry(root, width=30)
price_paid_box = Entry(root, width=30)

# Putting entry box into the screen
fn_box.grid(row=1, column=1, pady=3)
ln_box.grid(row=2, column=1, pady=3)
add1_box.grid(row=3, column=1, pady=3)
add2_box.grid(row=4, column=1, pady=3)
cit_box.grid(row=5, column=1, pady=3)
state_box.grid(row=6, column=1, pady=3)
zip_code_box.grid(row=7, column=1, pady=3)
country_box.grid(row=8, column=1, pady=3)
phone_box.grid(row=9, column=1, pady=3)
email_box.grid(row=10, column=1, pady=3)
user_name_box.grid(row=11, column=1, pady=3)
payment_method_box.grid(row=12, column=1, pady=3)
discount_code_box.grid(row=13, column=1, pady=3)
price_paid_box.grid(row=14, column=1, pady=3)

# Submit Button
Button(root, text="Submit", command=submit).grid(row=15, column=0, columnspan=2, padx=10, pady=3, ipadx=100)

# list of customers button
Button(root, text="list of costumers", command=list_customers).grid(row=16, column=0, columnspan=2, padx=10, pady=3,
                                                                    ipadx=100)

# Search for customer button
Button(root, text="search for customer", command=search).grid(row=17, column=0, columnspan=2, pady=3, padx=10,
                                                              ipadx=100)

root.mainloop()
