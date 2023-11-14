from tkinter import *

root = Tk()
root.title('check box')
root.geometry("400x400")


def show():
    lbl = Label(root, text=var.get())
    lbl.pack()


var = StringVar()

cb = Checkbutton(root, text="check this box", variable=var, onvalue="ON", offvalue="OFF")
cb.deselect()
butt = Button(root, text="show selection", command=show)

cb.pack()
butt.pack()


root.mainloop()
