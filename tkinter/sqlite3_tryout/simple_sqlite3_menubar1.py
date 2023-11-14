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

    def delete_form(self):
        self.text_field.delete(0, END)


def add_record():
    conn = sqlite3.connect("library_database.db")
    c = conn.cursor()

    c.execute("""
        INSERT INTO library_book(book_name, book_writer, type_of_book)
        VALUES(?,?,?)
    """, (book_name_entry.text_field.get(), book_writer_entry.text_field.get(), book_type_entry.text_field.get()))

    conn.commit()
    conn.close()

    book_name_entry.delete_form()
    book_writer_entry.delete_form()
    book_type_entry.delete_form()


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


# MENU

def about_program():
    about_window = Toplevel(root)
    about_text = """This program is designed to show beginners how to connect SQLITE3 with tkinter.
You can add search and quit function. Feel free to ball_speed it.
Devrim Savas Yilmaz"""
    about_window.title("About This Program")
    about_window.geometry("420x260")
    info_text = Text(about_window, width=40, height=10, wrap=WORD, borderwidth=1, spacing3=2, font=("Corier", 12))
    info_text.place(x=10, y=10)
    info_text.insert(END, about_text)
    info_text.config(state="disabled", bg="beige")
    close_this = Button(about_window, text="CLOSE THIS WINDOW", command=about_window.destroy)
    close_this.place(x=150, y=230)

    about_window.mainloop()


def donothing():
    pass


def change_style(chosen_style):
    style.theme_use(chosen_style)


root = Tk()
root.geometry("950x400")
root.config(bg="beige")
root.resizable(False, False)
style = ttk.Style()
style.theme_use("clam")  # or any theme as you wish alt,aqua, classic,default,vista, xpnative
style_list = [
    "alt",
    "default",
    "classic",
    "clam",
    "vista",
    "xpnative",
]

# Set style to treeview
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

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

stylemenu = Menu(filemenu, tearoff=0)
for style_name in style_list:
    stylemenu.add_command(label=style_name, command=lambda style=style_name: change_style(style))

filemenu.add_cascade(label="Styles", menu=stylemenu)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=about_program)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()