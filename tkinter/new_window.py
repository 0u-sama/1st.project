from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("window1")

img4 = ""


def second():
    global img4

    top = Toplevel(bg="black")
    top.title("window2")

    img4 = ImageTk.PhotoImage(
        Image.open("C:/Users/0uss4m4/Pictures/yu-zhong-mobile-legends-black-fierce-dragon-uhdpaper"
                   ".com-4K-5.2107-wp.thumbnail.jpg")
    )
    Label(top, image=img4).pack()
    Button(top, text="adios", command=top.destroy).pack()


Label(root, text="hola").grid(row=0, column=0)
Button(root, text="open window2", command=second).grid(row=1, column=0)
Button(root, text="destroy me", command=root.destroy).grid(row=1, column=1)


root.mainloop()
