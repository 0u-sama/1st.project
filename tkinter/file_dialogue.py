from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title('file_dialogue')


def openfile():
    global Image
    root.filename = filedialog.askopenfilename(
        initialdir="C:/Users/0uss4m4/Pictures", title="select a file", filetypes=(("jpg files", "*.jpg"),
                                                                                  "All files, "
                                                                                  "*.py")
    )

    Image = ImageTk.PhotoImage(Image.open(root.filename))
    image = Label(image=Image)

    Label(root, text=root.filename).pack()
    image.pack()


Button(root, text="open file", command=openfile).pack()

root.mainloop()
