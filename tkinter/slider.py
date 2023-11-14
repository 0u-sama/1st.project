from tkinter import *

root = Tk()
root.title("slide")

vertical = Scale(root, from_=0, to=200, orient=VERTICAL)

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)


vertical.pack(anchor=E)
horizontal.pack(anchor=S)


def update():
    Label(root, text=horizontal.get()).pack()


Button(root, text="click me", command=update).pack()

root.mainloop()
