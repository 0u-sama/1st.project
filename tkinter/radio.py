from tkinter import *

root = Tk()
root.title("radio")


# first type

frame_1 = LabelFrame(root, padx=30, text="first type")
frame_1.grid(row=0, column=0)

i = IntVar()
i.set("2")


def clicked_1(value):
    global my_label
    my_label = Label(frame_1, text="u clicked " + str(value))
    my_label.pack()


Radiobutton(frame_1, text="click me", variable=i, value=1).pack()
Radiobutton(frame_1, text="no click me!", variable=i, value=2).pack()

my_button = Button(frame_1, text="click me", command=lambda: clicked_1(i.get()))

my_button.pack()

# second type

frame_2 = LabelFrame(root, padx=30, text="second type")
frame_2.grid(row=0, column=1)


def clicked_2(value):
    global my_label
    my_label = Label(frame_2, text="u want  " + str(value) + "with ur PIZZA")
    my_label.pack()


MODES = [
    ("Peperoni", "Peperoni"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
    ("Cheese", "Cheese")
]

PIZZA = StringVar()
PIZZA.set("Peperoni")

for text, mode in MODES:
    Radiobutton(frame_2, text=text, variable=PIZZA, value=mode).pack()

button = Button(frame_2, text="submit", command=lambda: clicked_2(PIZZA.get()))


button.pack()


root.mainloop()
