from tkinter import *
import sqlite3
from tkinter import ttk

db_list = ["BOOK NAME :", "BOOK WRITER :", "BOOK TYPE :"]


class TField:
    def __init__(self, root, label_text, w, x, y, **kwargs):
        self.label_field = Label(root, text=label_text, anchor="w")
        self.label_field.place(x=x, y=y)
        self.text_field = Entry(root, width=w)
        self.text_field.place(x=x + 80, y=y)


conn = sqlite3.connect("library_database.db")
c = conn.cursor()

# create table
tablebooks = """CREATE TABLE IF NOT EXISTS library_book(book_name text, book_writer text, type_of_book text)"""
c.execute(tablebooks)
conn.commit()
conn.close()


def add_record():
    conn = sqlite3.connect("library_database.db")
    c = conn.cursor()

    c.execute("""
INSERT INTO library_book(book_name,book_writer,type_of_book)
VALUES(?,?,?)
""", (book_name_entry.text_field.get(), book_writer_entry.text_field.get(), book_type_entry.text_field.get()))

    conn.commit()
    conn.close()


def show_records():
    conn = sqlite3.connect("library_database.db")
    c = conn.cursor()
    c.execute("SELECT *, oid FROM library_book")
    records = c.fetchall()

    # Clear existing treeview
    for record in tree_view.get_children():
        tree_view.delete(record)

    # Insert new records
    for index, record in enumerate(records):
        tree_view.insert("", "end", text=index + 1, values=record[:-1])

    conn.close()


root = Tk()
root.geometry("950x400")
root.config(bg="beige")
root.resizable(False, False)
style = ttk.Style()
style.theme_use("clam")  # or any theme as you wish alt,aqua, classic,default,vista, xpnative

# set style to treeview
style.map('Treeview', background=[('selected', 'green')])

root_frame = LabelFrame(root, text="RECORD", width=300, height=300)
root_frame.place(x=10, y=10)
tree_view_frame = LabelFrame(root, text="LIBRARY", width=500, height=300)
tree_view_frame.place(x=320, y=10)

book_name_entry = TField(root_frame, db_list[0], 30, 10, 10)
book_writer_entry = TField(root_frame, db_list[1], 30, 10, 50)
book_type_entry = TField(root_frame, db_list[2], 30, 10, 90)
submit_button = Button(root_frame, text="SUBMIT", width=15, fg="blue", command=add_record)
submit_button.place(x=1, y=130)

# tree view
tree_view = ttk.Treeview(tree_view_frame, columns=("Book Name", "Book Writer", "Book Type"), show="headings")
tree_view.heading("Book Name", text="Book Name")
tree_view.heading("Book Writer", text="Book Writer")
tree_view.heading("Book Type", text="Book Type")
tree_view.pack(fill="both", expand=True)

# show records
show_button = Button(root_frame, text="SHOW RECORDS", fg="blue", command=show_records)
show_button.place(x=160, y=130)

root.mainloop()


