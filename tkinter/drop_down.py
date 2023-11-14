from tkinter import *

root = Tk()
root.title("drop_down")
root.geometry("400x400")


def show():
    Label(root, text=clicked.get()).pack()


clicked = StringVar()

weekdays = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

clicked.set(weekdays[2])

drop = OptionMenu(root, clicked, *weekdays)
butt = Button(root, text="show selection", command=show)

drop.pack()
butt.pack()

root.mainloop()
