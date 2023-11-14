from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("message boxes")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def s_i():
    c = messagebox.showinfo("this is info", "info")
    Label(frame, text=c).pack()


def s_w():
    c = messagebox.showwarning("this is warning", "warning")
    Label(frame, text=c).pack()


def s_e():
    c = messagebox.showerror("this is error", "error")
    Label(frame, text=c).pack()


def a_q():
    c = messagebox.askquestion("this is question", "question")
    Label(frame, text=c).pack()


def ok_ca():
    c = messagebox.askokcancel("this is ok_cancel", "ok_cancel")
    Label(frame, text=c).pack()


def y_n():
    c = messagebox.askyesno("this is yes_no", "yes_no")
    Label(frame, text=c).pack()


def tr_ca():
    c = messagebox.askretrycancel("this is try_cancel", "try_cancel")
    Label(frame, text=c).pack()


def y_n_ca():
    c = messagebox.askyesnocancel("this is yes_no_cancel", "yes_no_cancel")
    Label(frame, text=c).pack()


b_1 = Button(root, text="show_info", command=s_i)
b_2 = Button(root, text="show_warning", command=s_w)
b_3 = Button(root, text="show_error", command=s_e)
b_4 = Button(root, text="ask_question", command=a_q)
b_5 = Button(root, text="ask_ok_cancel", command=ok_ca)
b_6 = Button(root, text="ask_yes_no", command=y_n)
b_7 = Button(root, text="try_cancel", command=tr_ca)
b_8 = Button(root, text="yes_no_cancel", command=y_n_ca)

b_1.grid(row=0, column=0)
b_2.grid(row=0, column=1)
b_3.grid(row=0, column=2)
b_4.grid(row=0, column=3)
b_5.grid(row=1, column=0)
b_6.grid(row=1, column=1)
b_7.grid(row=1, column=2)
b_8.grid(row=1, column=3)

frame = LabelFrame(root, text="output", padx=100, pady=100)
frame.grid(row=2, column=2)

root.mainloop()
