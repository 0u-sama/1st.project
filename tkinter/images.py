from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('images viewer')
root.iconbitmap('C:/Users/0uss4m4/Pictures/image-gallery.png')

img1 = ImageTk.PhotoImage(Image.open("C:/Users/0uss4m4/Pictures/image-gallery.png"))

img3 = ImageTk.PhotoImage(Image.open("C:/Users/0uss4m4/Pictures/Capture d’écran 2023-05-05 155149.png"))
img4 = ImageTk.PhotoImage(Image.open("C:/Users/0uss4m4/Pictures/yu-zhong-mobile-legends-black-fierce-dragon-uhdpaper"
                                     ".com-4K-5.2107-wp.thumbnail.jpg"))
img5 = ImageTk.PhotoImage(Image.open("C:/Users/0uss4m4/Pictures/Capture d’écran 2023-05-05 155149.png"))

image_list = [img1, img3, img4, img5]

my_label = Label(image=img1)

status = Label(root, text="image 1 of" + str(len(image_list)), bd=1, relief=FLAT, anchor=E)


# functions

def forward_fun(img_num):
    global my_label, button_forward, button_back, status

    my_label.grid_forget()
    my_label = Label(image=image_list[img_num - 1])
    button_forward = Button(root, text='>', command=lambda: forward_fun(img_num + 1))
    button_back = Button(root, text='<', command=lambda: back_fun(img_num - 1))
    status = Label(root, text="image " + str(img_num) + "of" + str(len(image_list)), bd=1, relief=FLAT, anchor=E)

    if img_num == len(image_list):
        button_forward = Button(root, text='>', command=lambda: forward_fun(img_num + 1), state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    status.grid(row=2, column=1, columnspan=3, sticky=W + E)


def back_fun(img_num):
    global my_label, button_forward, button_back, status
    my_label.grid_forget()
    my_label = Label(image=image_list[img_num - 1])
    button_forward = Button(root, text='>', command=lambda: forward_fun(img_num + 1))
    button_back = Button(root, text='<', command=lambda: back_fun(img_num - 1))
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    my_label.grid(row=0, column=0, columnspan=3)
    status = Label(root, text="image " + str(img_num) + "of" + str(len(image_list)), bd=1, relief=FLAT, anchor=E)

    status.grid(row=2, column=1, columnspan=3, sticky=W + E)

    if img_num == 1:
        button_back = Button(root, text="<", state=DISABLED)
        button_back.grid(row=1, column=0)


# buttons

button_back = Button(root, text="<", command=back_fun, state=DISABLED)
button_forward = Button(root, text=">", command=lambda: forward_fun(2))
button_quit = Button(root, text='Exit', command=root.quit)

# putting em on the screen

button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
button_back.grid(row=1, column=0)
my_label.grid(row=0, column=0, columnspan=3)
status.grid(row=2, column=1, columnspan=3, sticky=W+E)

root.mainloop()
