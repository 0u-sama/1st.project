from tkinter import *


root = Tk()
root.title("frames")


frame_1 = LabelFrame(root, text="hello world", bg="blue", foreground="brown", padx=100, pady=100)
frame_2 = LabelFrame(root, text="hello world", bg="blue", foreground="brown", padx=100, pady=100)
b_1 = Button(frame_1, text="click me", bg="white")
b_2 = Button(frame_2, text="no click me", bg="black", foreground="white")


frame_1.grid(row=0, column=0)
frame_2.grid(row=0, column=1)
b_2.pack(padx=2, pady=5)
b_1.pack(padx=12, pady=5)


root.mainloop()
